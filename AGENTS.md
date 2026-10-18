# AGENTS.md — UNMdP Map

Guía para agentes (y personas) que trabajan en este repo. Para qué sirve la herramienta y qué ve el usuario: [README.md](README.md).

**UNMdP Map** es un sitio estático de una sola página que muestra el plan de estudios de cada carrera de la UNMdP como un grafo de correlatividades. El estudiante marca materias y el grafo calcula qué puede cursar y qué finales puede rendir. No hay backend: el avance de cada estudiante se guarda en `localStorage`.

## Estructura

| Archivo | Qué es | ¿Se edita a mano? |
|---|---|---|
| `datos/visor_template.html` | Toda la UI: CSS, HTML y JS del visor. `__DATA__` se reemplaza por los datos. | **Sí**, la fuente del front |
| `datos/facultades.py` | Unidades académicas, regla por defecto, vigencia y notas por facultad | **Sí** |
| `datos/carreras.py` | Carreras de FCEyS y sus materias (`filas`), parser y validador | **Sí** |
| `datos/plan.py` | Contador Público en formato tupla (legado, lo convierte `_contador()` en `carreras.py`) | **Sí** |
| `datos/generar.py` | Arma `index.html`, `carreras.json` y la planilla | Rara vez |
| `datos/build_xlsx_all.py` | Planilla Excel con fórmulas equivalentes al visor (requiere `openpyxl`) | Rara vez |
| `index.html` | Sitio publicado = template + datos + `<head>` | **No, se genera** |
| `datos/carreras.json` | Volcado de los datos | **No, se genera** |
| `datos/unmdp-map_fceys.xlsx` | Planilla descargable | **No, se genera** |

No hay npm, bundler ni tests automáticos. Las únicas dependencias externas son Google Fonts (Archivo, Source Sans 3, JetBrains Mono) y, para generar, Python 3 + `openpyxl`.

## Flujo de trabajo

1. Editar la fuente: `datos/visor_template.html` para la UI o `datos/*.py` para los datos. **Nunca** `index.html` directo: se pisa al regenerar.
2. Validar los datos:
   ```bash
   cd datos && python3 carreras.py
   ```
   Lista cada carrera con su cantidad de materias, códigos duplicados y correlativas que no figuran en el plan. Hoy la única que aparece es `598` en Turismo, que ya está explicada en sus `notas`.
3. Regenerar (desde `datos/`, porque usa rutas relativas):
   ```bash
   pip install openpyxl
   python3 generar.py
   ```
4. Commitear la fuente y los tres archivos generados **en el mismo commit**. El sitio publicado y la planilla tienen que coincidir siempre con la fuente.

## Formato de datos

Cada carrera en `CARRERAS` (`datos/carreras.py`):

```python
dict(id="economia", nombre="Licenciatura en Economía", plan="Plan E (2005) · RM 1281/2019", horas=2906,
     url=BASE + "...",            # plan oficial
     notas=["..."],               # aclaraciones e inconsistencias del plan oficial
     filas=f"""
{CB}|1|1|EC|101|Introducción a la Economía|I|6||96||
""")
```

Cada línea de `filas` tiene **12 campos** separados por `|` (el parser lo verifica con un assert):

```
ciclo | año | cuat | área | cód | nombre | grupo | hs/sem | hs bim | hs cuat | correlativas | orientación
```

- `ciclo`: usar las constantes (`CB`, `CP`, `CO`, `RI`, `IN`, `FG`) o `"Optativas"`. `"Ciclo de orientación"` y `"Optativas"` se dibujan con borde punteado.
- `año`: número; `O1`/`O2` para optativas grupo I/II; vacío para requisitos instrumentales (van en la última fila del grafo).
- `cuat`: `1`, `2`, vacío (ingreso / anual) o `1/2/3` cuando se dicta en varios cuatrimestres (el primero es el sugerido y define la fila).
- `cód`: es la identidad de la materia y queda como **string**. Mismo código = misma materia en todas las carreras de la facultad.
- `correlativas`: códigos separados por espacio. Un código que no figura en el plan se muestra pero no se tiene en cuenta; si pasa, explicarlo en `notas`.
- La planilla admite como máximo 5 correlativas por materia (hay un assert en `build_xlsx_all.py`).

## Sumar una carrera o una facultad

1. Transcribir el plan desde el sitio oficial de la facultad. Poner la URL en `url` y la ordenanza/resolución en `plan`.
2. Agregar el `dict` a `CARRERAS`. Para otra facultad, conviene un módulo propio (por ejemplo `datos/carreras_<facultad>.py`) con el mismo formato y reusando `parse()`.
3. En `datos/facultades.py`, asignar `carreras=` a la facultad y definir `regla` (`"reg"` o `"ok"`), `vigencia` y `notas` si corresponde. Una facultad sin carreras aparece como "(próximamente)".
4. En `build_xlsx_all.py`, agregar el nombre corto de la carrera en `SHORT` (es el nombre de la hoja; Excel admite hasta 31 caracteres). La planilla y el título de la hoja Resumen hoy están armados solo para FCEyS: generalizarlos si se suma otra facultad.
5. En `visor_template.html`, el texto del link de fuente (`build()`) dice "eco.mdp.edu.ar" fijo: sacar el dominio de `C.url` antes de publicar otra facultad.
6. Validar, regenerar y probar en el navegador (ver **Verificación**).
7. Actualizar la lista de carreras disponibles en el README.

## Reglas de dominio (no romper)

- Estados por materia: sin marcar → `reg` (cursada aprobada) → `ok` (aprobada con final o promoción). Estados derivados para mostrar: `go` (puedo cursar) y `no` (bloqueada).
- **Para cursar**, cada correlativa necesita `reg` u `ok` según la `regla` (`"reg"` por defecto, el usuario la puede cambiar). **Para rendir el final** siempre se piden las correlativas `ok`.
- Coherencia: una materia nunca puede tener un estado mayor que el que permiten sus correlativas.
  - Subir una materia sube también, en cadena, todas sus correlativas al mínimo necesario (`setEstado`).
  - Bajar una materia baja en cadena las posteriores que quedaron por encima de lo permitido (`ajustarPosteriores` / `maxPermitido`).
  - Cuando el sistema cambia otras materias, avisa con `note`.
- El estado se guarda **por facultad y por código**, así que lo marcado en una carrera cuenta para todas las que comparten esa materia.
- La planilla Excel replica estas mismas reglas con fórmulas. Si cambia una regla en el visor, cambiarla también en `build_xlsx_all.py`.

## Compatibilidad con los usuarios actuales

- **Claves de `localStorage`**: `<pre>-estados` y `<pre>-regla`, donde `pre()` es `"fceys"` para `eco` y el `id` para las demás facultades. `load()` además migra las claves viejas (`<pre>-aprobadas`, `<pre>-aprobadas:<carrera>`, `cp-aprobadas`). No renombrar ni cambiar el formato sin una migración: el avance de los usuarios vive solo ahí.
- **Links directos**: `#<facultad>.<carrera>` (por ejemplo `#eco.contador`); también se acepta el formato viejo `#<carrera>`. No cambiar los `id` de facultades ni de carreras, porque rompen links compartidos y el estado guardado.
- Todo acceso a `localStorage` / `history` va en `try/catch`: la página tiene que funcionar en incógnito o con el almacenamiento bloqueado.

## Convenciones del front

- JS vanilla, sin dependencias ni paso de build. Todo inline en `visor_template.html`.
- El grafo es un `<svg>` armado a mano: filas por período (`periodKey` / `periodLabel`), hasta `PER_LINE` = 6 nodos por línea, orden por baricentro para reducir cruces y aristas como curvas Bézier.
- Colores solo con los tokens de `:root`. Cada token nuevo se define también en las dos variantes oscuras (`@media (prefers-color-scheme: dark)` con `:root:not([data-theme="light"])` y `:root[data-theme="dark"]`).
- Escapar con `esc()` todo texto que vaya a `innerHTML`.
- Accesibilidad: los nodos son `role="button"` con `tabindex`, `aria-label` y soporte de Enter/Espacio; `:focus-visible` visible; se respeta `prefers-reduced-motion`; el selector de estado usa `aria-pressed`.
- Móvil: el contenedor tiene 16px de margen lateral y el grafo hace scroll horizontal dentro de `.graph` (`min-width: 900px`). La página en sí nunca debe scrollear en horizontal.
- Textos de la UI en español rioplatense, en segunda persona con voseo ("tocá", "podés", "marcá"), claros para un estudiante de primer año.
- El código es compacto (funciones flecha de una línea, nombres cortos en español: `mats`, `by`, `deps`, `est`, `lvl`). Seguir ese estilo y comentar en español solo lo que no es obvio.

## Verificación

No hay tests automáticos. Antes de dar un cambio por terminado:

1. `cd datos && python3 carreras.py` sin duplicados nuevos ni correlativas faltantes sin explicar.
2. `python3 generar.py` y revisar `git diff` (un cambio solo de UI no debería modificar `carreras.json`).
3. Servir la raíz y abrir `http://localhost:8000`:
   ```bash
   python3 -m http.server 8000
   ```
4. Revisar en el navegador que la consola esté limpia y probar:
   - cambiar de facultad y de carrera, y abrir un link directo (`#eco.turismo`);
   - seleccionar una materia (resaltado azul = necesita, naranja = habilita);
   - marcar "Aprobada" en una materia avanzada (tienen que subir sus correlativas) y después bajar una correlativa (tienen que ajustarse las posteriores);
   - cambiar la regla para cursar, recargar y ver que todo se conserva;
   - "Desmarcar todo";
   - modo oscuro y ancho de celular (375 px).

## Git

- `master` es la rama publicada. Trabajar en una rama por cambio y abrir un PR (CODEOWNERS: @debadaracco).
- En los PR que corrigen o suman datos, incluir el link al plan oficial de donde sale cada dato.
