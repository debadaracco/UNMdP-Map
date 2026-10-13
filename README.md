# UNMdP Map

**UNMdP Map** es una herramienta para que los estudiantes de la Universidad Nacional de Mar del Plata vean de un vistazo el plan de su carrera y sepan qué materias pueden cursar.

## Por qué existe

Los planes de estudio se publican como tablas largas, con las correlatividades indicadas por código. Para saber qué te habilita una materia, o qué te falta para anotarte en otra, hay que ir desde el sistema Guaraní y verificar en la materia correspondiente, sin una opción gráfica clara.

Este proyecto arma esas mismas tablas como un mapa: cada materia es un recuadro y cada flecha une una correlativa con la materia que habilita. La idea es ahorrarles tiempo y dudas a los alumnos para que puedan planificar su carrera con más claridad.

## Qué podés hacer

- Elegir tu facultad y tu carrera.
- Tocar una materia para ver qué correlativas necesita y qué materias habilita.
- Marcar cada materia como *cursada aprobada* o *aprobada* (con final o promoción) y ver al instante cuáles podés cursar, cuáles siguen bloqueadas y qué finales ya podés rendir.
- El estado de cada materia siempre es coherente con el de sus correlativas. Una materia nunca puede figurar aprobada si alguna correlativa no lo está, porque no se puede rendir un final sin tener aprobadas sus correlativas. Por eso, al marcar una materia se marcan también sus correlativas, y si bajás el estado de una correlativa se ajustan en cadena las materias posteriores que dependen de ella.
- Elegir la regla para cursar: si alcanza con la cursada aprobada de las correlativas o si se pide el final. Los planes no lo aclaran, así que por defecto se usa la cursada aprobada. Para rendir un final siempre se piden las correlativas aprobadas.
- Cambiar de carrera sin volver a cargar todo: una materia aprobada cuenta en todas las carreras de la misma facultad que la comparten (por ejemplo, gran parte del ciclo básico de Contador y de la Licenciatura en Administración). Sirve si estás pensando en cambiarte de carrera o en cursar dos a la vez.
- Volver cuando quieras y retomar donde dejaste.

### Dónde se guarda tu avance

Las materias que marcás como aprobadas se guardan solo en el navegador que estás usando. No se envían a ningún servidor ni requieren cuenta. Por eso tu avance depende del dispositivo y del navegador:

- Si entrás desde otro dispositivo (por ejemplo, del celular a la computadora) o desde otro navegador, vas a ver el plan sin materias marcadas.
- Si usás una ventana de incógnito o borrás los datos de navegación, el avance se pierde.

## Carreras disponibles

Por ahora están las 10 carreras de grado de la **Facultad de Ciencias Económicas y Sociales**:

- Contador Público
- Licenciatura en Administración
- Licenciatura en Economía
- Licenciatura en Turismo
- Profesorado Universitario en Economía
- Tecnicatura Universitaria Contable
- Tecnicatura Universitaria en Comercialización
- Tecnicatura Universitaria en Comercio Exterior
- Tecnicatura Universitaria en Periodismo Digital
- Tecnicatura Universitaria en Turismo

La intención es sumar de a poco las carreras del resto de las facultades.

## De dónde salen los datos

Las materias y correlatividades se transcribieron de los planes de estudio que publica cada facultad en su sitio oficial. Cuando una tabla oficial tiene alguna inconsistencia, se aclara en las notas de esa carrera.

Este no es un sitio oficial de la universidad. Ante cualquier duda, la información válida es la de tu facultad.

## ¿Encontraste un error o querés sumar tu carrera?

Este es un proyecto abierto y cualquiera puede colaborar:

- **Abrí un *issue*** si encontrás una correlativa mal cargada, una materia que falta o algo que no funciona. Incluí el link al plan oficial donde figura el dato correcto.
- **Enviá un *pull request*** si querés corregirlo vos o sumar las carreras de otra facultad. Los datos de cada plan están en la carpeta `datos`.

Cualquier ayuda para que la herramienta les sirva a más estudiantes es bienvenida.
