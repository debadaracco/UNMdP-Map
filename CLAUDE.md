@AGENTS.md

## Notas para Claude Code

- Respondé y escribí commits, comentarios y textos de UI en español.
- Nunca edites `index.html`, `datos/carreras.json` ni `datos/unmdp-map_fceys.xlsx` a mano. Si un cambio tiene que verse en el sitio, hacelo en `datos/visor_template.html` o en `datos/*.py` y corré `python3 generar.py` desde `datos/`.
- Después de tocar datos, corré `python3 carreras.py` desde `datos/` antes de regenerar.
- Si falta `openpyxl`, avisá en vez de saltear la planilla: los tres archivos generados tienen que quedar en sync.
- Para verificar cambios de UI, serví la raíz con `python3 -m http.server 8000` y revisala en el navegador integrado: consola limpia, modo claro y oscuro, y 375 px de ancho. Seguí el checklist de **Verificación** de AGENTS.md.
- Antes de cambiar cualquier cosa de `localStorage`, del formato del hash o de los `id` de facultades y carreras, frená y consultá: esos cambios pueden borrar el avance de los usuarios.
