# Planes de estudio de las carreras de grado de la FCEyS - UNMdP
# Transcriptos de las páginas oficiales de eco.mdp.edu.ar (octubre 2026).
# Formato de cada fila: ciclo | año | cuat | área | cód | denominación | grupo | hs/sem | hs bim | hs cuat | correlativas | orientación
# "cuat" puede ser "1/2/3" (se dicta en varios cuatrimestres; el primero es el sugerido).
from plan import MATERIAS as _CP

BASE = "https://eco.mdp.edu.ar/component/content/article/"

def _contador():
    out = []
    for (ciclo, orient, anio, cuat, area, cod, nombre, grupo, hs, bim, hc, corr) in _CP:
        ciclo = {"Básico": "Ciclo básico", "Profesional": "Ciclo profesional",
                 "Orientación": "Ciclo de orientación", "Requisito instrumental": "Requisitos instrumentales"}[ciclo]
        out.append(f"{ciclo}|{anio or ''}|{cuat or ''}|{area}|{cod}|{nombre}|{grupo}|{hs or ''}|{bim or ''}|{hc or ''}|{' '.join(map(str, corr))}|{orient}")
    return out

CB, CP, CO, RI = "Ciclo básico", "Ciclo profesional", "Ciclo de orientación", "Requisitos instrumentales"
IN, FG = "Ciclo introductorio", "Formación general"

CARRERAS = [
 dict(id="contador", nivel="grado", nombre="Contador Público", plan="Plan E (2005) · OCS 446/2018", horas=2820,
      url=BASE + "206-plan-de-estudio-contador-publico-2005-plan-e-oca-n-880-04?Itemid=817&catid=184",
      notas=["Ciclo de orientación: se cursa una de las cinco materias, más una electiva obligatoria y optativas."],
      filas=_contador()),

 dict(id="administracion", nivel="grado", nombre="Licenciatura en Administración", plan="Plan C (2005) · OCS 881/2004", horas=2720,
      url=BASE + "208-plan-de-estudio-lic-en-administracion-2005-plan-c-oca-n-881-04?Itemid=818&catid=184",
      notas=["Ciclo de orientación: se cursa una de las cinco materias, más una electiva obligatoria (192 hs) y optativas."],
      filas=f"""
{CB}|1|1|EC|101|Introducción a la Economía|I|6||96||
{CB}|1|1|AD|104|Principios de Administración|I|6||96||
{CB}|1|1|MA|102|Matemática I|I|6||96||
{CB}|1|2|CO|103|Contabilidad I|I|6||96||
{CB}|1|2|CS|180|Historia Económica y Social I|II|4||64||
{CB}|1|2|CS|205|Sociología|II|4||64||
{CB}|1|2|MA|209|Matemática II|I|5||80|102|
{CB}|2|1|EC|314|Macroeconomía I|I|6||96|101 209|
{CB}|2|1|AD|308|Funciones Organizacionales|I|6||96|104|
{CB}|2|1|CS|280|Historia Económica y Social II|II|4||64|180|
{CB}|2|1|JU|202|Derecho Constitucional|II|4|32|||
{CB}|2|1|JU|307|Derecho Administrativo|II|4|32|||
{CB}|2|2|CO|226|Valuación y Exposición Contable|I|6||96|103|
{CB}|2|2|EC|208|Microeconomía I|I|6||96|101 209|
{CB}|2|2|MA|250|Estadística|I|6||96|209|
{CP}|3|1|AD|330|Sistema de Información|I|6||96|308 103|
{CP}|3|1|MA|424|Matemática Financiera|I|5||80|250|
{CP}|3|1|JU|425|Derecho del Trab. y de la Seg. Social|II|4||64|202 307|
{CP}|3|1|AD|380|Comportamiento Organizacional|I|4||64|308|
{CP}|3|2|SA|499|Ética y Responsabilidad Social|III|2||32||
{CP}|3|2|AD|333|Costos para la toma de decisiones|I|6||96|226|
{CP}|3|2|CO|348|Finanzas y Org. del Sector Público|I|4||64|202 314|
{CP}|3|2|AD|381|Investigac. de Operaciones en Administ.|I|4||64|308 250|
{CP}|4|1|JU|244|Derecho Económico|II|6||96|202 307|
{CP}|4|1|AD|435|Decisiones financieras de corto plazo|I|4||64|330 424|
{CP}|4|1|CO|470|Administración Tributaria|II|4||64|348|
{CP}|4|2|AD|441|Administración de Operaciones|I|4||64|333 381|
{CP}|4|2|AD|437|Administración de la Comercialización|I|6||96|250 330 333|
{CP}|4|2|AD|442|Administración de Recursos Humanos|I|6||96|330 425 380 499|
{CP}|4|2|CS|201|Metodología de las Ciencias Sociales|III|2||32|381|
{CP}|5|1|AD|535|Decisiones financieras de largo plazo|I|4||64|435|
{CP}|5|1|AD|542|Teoría de las Decisiones|I|4||64|435 441 437 442|
{CP}|5|1|AD|540|Conduc. Estratég. y Control de Gestión|I|6||96|435 441 437 442|
{CP}|5|1|JU|591|Práct. Profesional en el ámbito judicial|III|2||32|425 244 470|
{CO}|5|2|AD|570|Análisis organizacional||4||64|435 437 441 442|Gestión Estratégica
{CO}|5|2|AD|571|Investigación de Mercado||4||64|201 437|Comercialización
{CO}|5|1|EC|504|Análisis y Evaluación de Proyectos||4||64|208 314 435|Gestión Financiera
{CO}|5|2|EC|550|Administración del Estado y Políticas Públicas||4||64|470|Gestión Pública
{CO}|5|2|AD|565|Creación de empresas||4||64|435 437 441 442|Gestión de Org. de la Economía Regional
{RI}|||SA|595|Nivel de Inglés Técnico I||||||
{RI}|||AD|300|Nivel de Computación||||||
{RI}|||SA|285|Taller Uso de Programas de Computación||||||
{RI}|||SI|296|Acreditar 30 horas de Investigación||||||
{RI}|||SE|367|Seminario de Práctica Sociocomunitaria||||||
{RI}|||SA|286|Acreditar 30 horas Pasantías o Prácticas Profesionales Académicas||||||
"""),

 dict(id="economia", nivel="grado", nombre="Licenciatura en Economía", plan="Plan E (2005) · RM 1281/2019", horas=2906,
      url=BASE + "207-plan-de-estudio-lic-en-economia-2005-plan-e-oca-n-882-04?Itemid=819&catid=184",
      notas=["Ciclo de orientación: se cursa una de las tres materias, más una electiva obligatoria (192 hs) y optativas.",
             "En la página, la fila de Política Económica II (505) tiene las horas corridas de columna; se tomó 4 hs/sem y 64 hs cuatrimestrales.",
             "Estadística para Economistas (302) pide 300, que es el requisito Nivel de Computación."],
      filas=f"""
{CB}|1|1|EC|101|Introducción a la Economía|I|6||96||
{CB}|1|1|AD|104|Principios de Administración|I|6||96||
{CB}|1|2|MA|102|Matemática I|I|6||96||
{CB}|1|2|CO|103|Contabilidad I|I|6||96||
{CB}|1|2|CS|180|Historia Económica y Social I|II|4||64||
{CB}|1|2|MA|108|Matemática para Economistas I|I|6||96|102|
{CB}|2|1|EC|314|Macroeconomía I|I|6||96|101 108|
{CB}|2|1|CS|280|Historia Económica y Social II|II|4||64|180|
{CB}|2|1|JU|202|Derecho Constitucional|II|4|32|||
{CB}|2|1|JU|307|Derecho Administrativo|II|4|32|||
{CB}|2|2|EC|208|Microeconomía I|I|6||96|101 108|
{CB}|2|2|MA|206|Estadística Metodológica|I|6||96|108|
{CB}|2|2|CS|218|Teoría Social y Política|II|6||96||
{CP}|3|1|MA|424|Matemática Financiera|I|5||80|108|
{CP}|3|1|MA|328|Matemática para Economistas II|I|6||96|108|
{CP}|3|1|CS|356|Metodología de la Investigación|III|4||64||
{CP}|3|1|JU|244|Derecho Económico|II|4||64|202 307|
{CP}|3|2|EC|448|Macroeconomía II|I|6||96|314 328|
{CP}|3|2|EC|346|Microeconomía II|I|6||96|208 328|
{CP}|3|2|MA|302|Estadística para Economistas|I|6||96|206 300|
{CP}|3|2|SA|499|Ética y Responsabilidad Social|III|2||32||
{CP}|4|1|AD|408|Análisis Económico-Financiero de Emp.|I|6||96|103 424|
{CP}|4|1|EC|418|Dinero, Crédito y Bancos|I|4||64|448|
{CP}|4|1|EC|407|Economía Internacional|I|5||80|448 346|
{CP}|4|1|EC|447|Economía Ambiental|II|4||64|448 346|
{CP}|4|2|EC|409|Política Económica I|II|4||64|346|
{CP}|4|2|EC|410|Econometría I|I|6||96|302|
{CP}|4|2|EC|419|Economía Política|II|4||64|314 208 218|
{CP}|4|2|CO|349|Economía y Org. del Sector Público|I|6||96|202 314|
{CP}|5|1|EC|504|Análisis y Evaluación de Proyectos|I|4||64|328 408|
{CP}|5|1|EC|553|Historia del Pensamiento Económico|II|6||96|314 280 208 419|
{CP}|5|1|EC|556|Desarrollo Económico|II|4||64|448 407|
{CP}|5|1|EC|505|Política Económica II|II|4||64|314 280 218 409|
{CP}|5|2|EC|520|Metodología de la Invest. Aplicada|III|4|32||346 356 410 419 448|
{CO}|5|2|EC|548|Desarrollo Regional||4||64|556|Desarrollo Regional
{CO}|5|2|EC|549|Teoría de la Firma y de la Organización Industrial||4||64|409|Economía de Empresas
{CO}|5|2|EC|550|Administración del Estado y Políticas Públicas||4||64|349|Estado y Políticas Públicas
{RI}|||SA|598|Nivel de Inglés Técnico I||||||
{RI}|||SA|599|Nivel de Inglés Técnico II||||||
{RI}|||AD|300|Nivel de Computación||||||
{RI}|||SA|289|Taller Uso de Programas de Computación||||||
{RI}|||SI|296|Acreditar 30 horas de Investigación||||||
{RI}|||SE|365|Seminario de Práctica Sociocomunitaria||||||
{RI}|||SA|290|Acreditar 30 horas Pasantías o Prácticas Profesionales Académicas||||||
{RI}|||EC|607|Tesina de Graduación||||||
"""),

 dict(id="turismo", nivel="grado", nombre="Licenciatura en Turismo", plan="Plan E (2005) · OCS 370/2004 y 513/2009", horas=2688,
      url="https://eco.mdp.edu.ar/plan-de-estudio-turismo",
      notas=["Ciclo de orientación: se cursa una de las tres materias, más una electiva obligatoria (192 hs) y optativas.",
             "Inglés Técnico (399) figura con correlativas 598 y 597. El 598 no aparece en este plan (el Inglés Técnico I de Turismo es 596): verificalo con la facultad."],
      filas=f"""
{CB}|1|1|EC|101|Introducción a la Economía|I|6||96||
{CB}|1|1|TU|161|Introducción al Turismo|I|4||64||
{CB}|1|1|MA|114|Introducción a la Matemática|I|6||96||
{CB}|1|2|CS|180|Historia Económica y Social I|II|4||64||
{CB}|1|2|CS|158|Sociología Aplicada|II|4||64||
{CB}|1|2|TU|216|El Arte en la cultura|II|3||48||
{CB}|1|2|AD|104|Principios de Administración|I|6||96||
{CB}|2|1|JU|202|Derecho Constitucional|II|4|32|||
{CB}|2|1|JU|307|Derecho Administrativo|II|4|32|||
{CB}|2|1|CS|280|Historia Económica y Social II|II|4||64|180|
{CB}|2|1|CO|308|Funciones Organizacionales|I|6||96|104|
{CB}|2|1|CS|215|Antropología cultural|II|3||48||
{CB}|2|2|TU|277|Espacios Turísticos Mundiales|I|6||96||
{CB}|2|2|MA|251|Estadística Aplicada|I|6||96|114|
{CB}|2|2|CO|227|Contabilidad General|I|6||96|104|
{CP}|3|1|TU|323|Espacios Turísticos Americanos|II|6||96|277|
{CP}|3|1|EC|324|Economía Aplicada|I|4||64|101|
{CP}|3|1|TU|112|Recursos Naturales|II|4||64||
{CP}|3|1|CS|356|Metodología de la Investigación|III|4||64||
{CP}|3|2|TU|113|Teoría del Turismo y la Recreación|I|6||96|161|
{CP}|3|2|TU|325|Organizaciones de Alojamiento y Recreación|II|4||64|308|
{CP}|3|2|TU|207|Recursos Culturales|II|4||64|216 215|
{CP}|3|2|CS|465|Psicología de Grupos|II|4||64||
{CP}|4|1|CO|349|Economía y Org. del Sector Público|I|6||96|202 324|
{CP}|4|1|AD|432|Adm. Financiera de Organizaciones Turísticas|I|4||64|104 324|
{CP}|4|1|TU|481|Agencias de Viajes y Transportes|II|4||64||
{CP}|4|1|AD|433|Comercialización Aplicada|II|4||64|308|
{CP}|4|2|SA|399|Inglés Técnico|II|4||64|598 597|
{CP}|4|2|TU|482|Gestión Pública de Turismo|I|4||64|349|
{CP}|4|2|TU|483|Investigación Aplicada al Turismo|III|4||64|356|
{CP}|4|2|TU|434|Gestión de Personal de Organizac. Turísticas|I|4||64|308 465|
{CP}|5|1|TU|508|Política y planificación|I|6||96|113|
{CP}|5|1|TU|583|Proyectos Turísticos|III|6||96|349 432|
{CP}|5|1|SA|499|Ética y Responsabilidad Social|III|2||32||
{CP}|5|2|TU|509|Práctica profesional en Turismo|III|4||64|325 481 482|
{CO}|5|2|EC|550|Administración del Estado y Políticas Públicas||4||64|349 482|Sector Público
{CO}|5|2|AD|570|Análisis Organizacional||4||64|432 433 434|Sector Privado
{CO}|5|1|EC|511|Gestión Ambiental||4||64|112 483|Ambiental
{RI}|||SA|596|Nivel de Inglés Técnico I||||||
{RI}|||SA|597|Nivel de Inglés Técnico II||||||
{RI}|||AD|300|Nivel de Computación||||||
{RI}|||SA|287|Taller Uso de Programas de Computación||||||
{RI}|||SI|296|Acreditar 30 horas de Investigación||||||
{RI}|||SE|364|Seminario de Práctica Sociocomunitaria||||||
{RI}|||SA|288|Acreditar 30 horas Pasantías o Prácticas Profesionales Académicas||||||
"""),

 dict(id="profesorado", nivel="pregrado", nombre="Profesorado Universitario en Economía", plan="OCA 2344/2011 y 125/2018", horas=2750,
      url=BASE + "209-plan-de-estudio-profesorado-universitario-en-economia-a?Itemid=821&catid=184",
      notas=["Optativas: 96 hs del Grupo I y 64 hs del Grupo II. En el plan no tienen año asignado; acá aparecen al final."],
      filas=f"""
{CB}|1|1|EC|101|Introducción a la Economía|I|6||96||
{CB}|1|1|AD|104|Principios de Administración|I|6||96||
{CB}|1|1|MA|102|Matemática I|I|6||96||
{CB}|1|2|CO|103|Contabilidad I|I|6||96||
{CB}|1|2|CS|180|Historia Económica y Social I|II|4||64||
{CB}|1|2|MA|108|Matemática para Economistas I|I|6||96|102|
{CB}|1|2|SA|1001|Problemática Educativa||6||96||
{CB}|2|1|EC|314|Macroeconomía I|I|6||96|101 108|
{CB}|2|1|CS|280|Historia Económica y Social II|II|4||64|180|
{CB}|2|1|JU|202|Derecho Constitucional|II|4|32|||
{CB}|2|1|SA|1002|Sistema Educativo y Curriculum||||96|1001|
{CB}|2|2|EC|208|Microeconomía I|I|6||96|101 108|
{CB}|2|2|MA|206|Estadística Metodológica|I|6||96|108|
{CB}|2|2|CS|218|Teoría Social y Política|II|6||96||
{CB}|3|1|SA|1003|Planeamiento y Gestión Institucional||6||96|1002|
{CB}|3|1|CS|356|Metodología de la Investigación|III|4||64||
{CB}|3|1|SA|1004|Adolescencia, Educación y Cultura||6||96||
{CB}|3|1|AD|308|Funciones Organizacionales|I|6||96|104|
Ciclo superior|3|2|SA|1005|Didáctica General||10||160|1003|
Ciclo superior|3|2|EC|419|Economía Política|II|4||64|314 208 218|
Ciclo superior|3|2|SA|499|Ética y Responsabilidad Social|III|2||32||
Ciclo superior|4|1|EC|553|Historia del Pensamiento Económico|II|6||96|314 280 208 419|
Ciclo superior|4|1|EC|1010|Política Económica Argentina|II|4||64|314 280 218|
Ciclo superior|4|1|SA|1006|Didáctica y Práctica de la Enseñanza I|III|9||144|1005 103 308 419|
Ciclo superior|4|2|SA|1007|Didáctica y Práctica de la Enseñanza II|III|9||144|1006|
Ciclo superior|4|2|CO|349|Economía y Org. del Sector Público|I|6||96|103 314 202|
Optativas|O1|1|FH|1011|Introducción a las Ciencias Políticas||6||96|280 419|Grupo I
Optativas|O1|1|FH|1012|Filosofía de la Educación||6||96||Grupo I
Optativas|O1|1|FH|1013|Introducción a la Psicología||6||96||Grupo I
Optativas|O1|1|FH|1014|Psicología de la Educación||6||96||Grupo I
Optativas|O1|1|FH|1015|Sociología del Desarrollo||6||96|218 419|Grupo I
Optativas|O1|1|FH|1016|Pensamiento Social Latinoamericano||6||96|218 419|Grupo I
Optativas|O2|2|EC|1030|Adm. del Estado y Políticas Públicas|I|4||64|349|Grupo II
Optativas|O2|2|EC|1031|Teoría de la Firma y de la Org. Industrial|I|4||64|208 314|Grupo II
Optativas|O2|1|EC|1032|Desarrollo Económico|I|4||64|208 314|Grupo II
Optativas|O2|2|EC|1033|Mercado de Trabajo y Relaciones Laborales|III|4||64|208 314|Grupo II
Optativas|O2|2|EC|1034|Economía Ambiental|II|4||64|208 314|Grupo II
Optativas|O2|1|EC|1035|Las Organizaciones Asociativas y la Economía Solidaria|III|4||64|419|Grupo II
Optativas|O2|1|AD|1036|Sistemas de Información|I|6||96|103 308|Grupo II
Optativas|O2|2|EC|1037|Sector Pesquero y Org. Industrial|III|2||32|208 314|Grupo II
Optativas|O2|2|EC|1038|Políticas Pesqueras|III|2|32||208 314|Grupo II
Optativas|O2|1|EC|1039|Estructura Económica Mundial y Argentina|III|2||32|208 314|Grupo II
Optativas|O2|2|EC|1040|Economía de los Mercados Agrarios|III|2||32|208 314|Grupo II
Optativas|O2|2|AD|1041|Creación de Empresas|I|4||64|308 103|Grupo II
Optativas|O2|2|EC|1042|Metodología de la Investigación Aplicada|III|2||32|208 314 356|Grupo II
{RI}||1|SA|598|Nivel de Inglés Técnico I||4||64||
{RI}||1|AD|300|Nivel de Computación||2||32||
{RI}||1|SA|1050|Taller de Nuevas Tecnologías de la Información y la Conectividad||4||64||
{RI}||1|SA|1051|Taller de Sistemas de Información Contable||2||32|103|
{RI}||1|SE|366|Seminario de Práctica Sociocomunitaria||||30|1005|
"""),

 dict(id="tec-contable", nivel="pregrado", nombre="Tecnicatura Universitaria Contable", plan="RM 435/2020", horas=1666,
      url="https://eco.mdp.edu.ar/carreras/4551-plan-de-estudio-tec-universitaria-contable",
      notas=["Las materias marcadas 1/2/3 se dictan en más de un cuatrimestre; se ubican en el primero indicado."],
      filas=f"""
{IN}|1||SA|291|Taller de Introducción a la Vida Universitaria|III|1||16||
{IN}|1||SA|292|Aproximación a las Ciencias Económicas y Sociales|III|4||64||
{IN}|1||SA|293|Aproximación a las Matemáticas|III|2||32||
{FG}|1|1/2/3|EC|101|Introducción a la Economía|I|6||96|291 292 293|
{FG}|1|1/2/3|JU|1123|Principios de Derecho Público|II|4||64|291 292 293|
{FG}|1|1/2/3|CO|103|Contabilidad I|I|6||96|291 292 293|
{FG}|1|2/1/3|AD|104|Principios de Administración|I|6||96|291 292 293|
{FG}|1|2/1/3|JU|340|Derecho Privado|II|4||64|1123|
{FG}|1|2/1/3|MA|114|Introducción a la Matemática|I|6||96|291 292 293|
{FG}|2|1/2/3|AD|3001|Sistemas de información de la organización|I|6||96|104 103 300|
{FG}|2|1/2/3|JU|1081|Derecho Comercial|II|4||64|340|
{FG}|2|1/2/3|CO|3004|Contabilidad Avanzada|I|6||96|103 300|
{FG}|2|2/1/3|CO|3005|Elementos de costos|I|6||96|104 3004|
{FG}|2|2/1/3|MA|3000|Nociones de Estadística y de Cálculo Financiero|I|6||96|114 300|
{FG}|2|2/1/3|CO|3003|Entidades sin fines de lucro|I|4||64|3004 1081|
{FG}|3|1/2/3|CO|3006|Elementos de Práctica Tributaria|I|6||96|1123 3004|
{FG}|3|1/2/3|JU|425|Derecho del Trabajo y la Seguridad Social|II|4||64|1081|
{FG}|3|2/1/3|AD|3002|Nociones de administración financiera|I|5||80|3004 3000|
{FG}|3|2/1/3|CO|3007|Seminario de Prácticas Integradas|I|6||96|3006 3001 425|
{RI}|||AD|300|Nivel de Computación||||32||
{RI}|||SA|299|Taller de uso de computación||||32|300 103|
{RI}|||CO|3009|Taller de uso de aplicativos impositivos||||48|3006|
{RI}|||CO|3008|Taller de liquidación de sueldos y jornales||||32|425|
{RI}|||SE|369|Seminario de Práctica Sociocomunitaria||||50|3003|
"""),

 dict(id="tec-comercializacion", nivel="pregrado", nombre="Tecnicatura Universitaria en Comercialización", plan="OCS 1569/2015 · RM 875/2016", horas=1634,
      url="https://eco.mdp.edu.ar/tuc", notas=[],
      filas=f"""
{IN}|1||SA|291|Taller de Introducción a la vida Universitaria|III|1||16||
{IN}|1||SA|292|Aproximación a las Ciencias Económicas y Sociales|III|4||64||
{IN}|1||SA|293|Aproximación a la Matemática|III|2||32||
{FG}|1|1|EC|101|Introducción a la Economía|I|6||96|291 292 293|
{FG}|1|1|AD|104|Principios de Administración|I|6||96|291 292 293|
{FG}|1|1|MA|114|Introducción a la Matemática|I|6||96|291 292 293|
{FG}|1|2|CO|227|Contabilidad General|I|6||96|291 292 293|
{FG}|1|2|AD|1080|Administración de la Comercialización|I|6||96|104|
{FG}|1|2|AD|1082|Taller de Competitividad y Posicionamiento|I|2||32|104|
{FG}|2|1|JU|1081|Derecho Comercial|II|4||64|291 292 293|
{FG}|2|1|AD|1084|Precios y Costos|I|6||96|1082|
{FG}|2|1|CS|1085|Comunicación y Medios|II|4||64|104|
{FG}|2|2|SA|499|Ética y Responsabilidad Social|III|2||32|291 292 293|
{FG}|2|2|MA|251|Estadística Aplicada|I|6||96|114|
{FG}|2|2|AD|1083|Gestión de Productos y Servicios|I|4||64|1082|
{FG}|3|1|AD|1087|Comportamiento del Consumidor|I|4||64|101 1082|
{FG}|3|1|AD|380|Comportamiento Organizacional|I|4||64|104 1081|
{FG}|3|1|AD|1086|Logística y Distribución|I|4||64|1082 1083|
{FG}|3|2|AD|1089|Planificación y Control Comercial|I|4||64|1083 1084 1085 1086|
{FG}|3|2|AD|571|Investigación de Mercados|I|4||64|251 1082 1087|
{FG}|3|2|AD|1088|Seminario de Práctica Profesional|III|6||96|1083 1084 1085 1087|
{RI}|||SA|595|Nivel de Inglés Técnico I||4||64||
{RI}|||AD|300|Nivel de Computación||2||32||
{RI}|||SE|282|Taller de Uso de Programas (SPSS)||2||32|300|
{RI}|||SE|361|Seminario de Práctica Sociocomunitaria||||50||
"""),

 dict(id="tec-comercio-exterior", nivel="pregrado", nombre="Tecnicatura Universitaria en Comercio Exterior", plan="OCS 2226/2016 · RM 2625/2017", horas=1762,
      url="https://eco.mdp.edu.ar/tuce",
      notas=["Las correlativas 291, 292 y 293 son los Requisitos Curriculares Obligatorios comunes a los ingresantes (112 hs). El plan no los detalla; se usan los nombres de las otras tecnicaturas.",
             "Marketing Internacional (1113) pide 1084, pero en este plan Precios y Costos figura como 1084B. Se tomó 1084B."],
      filas=f"""
{IN}|1||SA|291|Taller de Introducción a la Vida Universitaria|III|1||16||
{IN}|1||SA|292|Aproximación a las Ciencias Económicas y Sociales|III|4||64||
{IN}|1||SA|293|Aproximación a la Matemática|III|2||32||
{FG}|1|1|EC|101|Introducción a la Economía|I|6||96|291 292 293|
{FG}|1|1|MA|114|Introducción a la Matemática|I|6||96|291 292 293|
{FG}|1|1|AD/EC|1110|Introducción al Comercio Internacional|I|6||96|291 292 293|
{FG}|1|2|JU|1123|Principios de Derecho Público|II|4||64|291 292 293|
{FG}|1|2|AD|104|Principios de Administración|I|6||96|291 292 293|
{FG}|1|2|CO|227|Contabilidad General|I|6||96|291 292 293|
{FG}|2|1|SA|499|Ética y Responsabilidad Social|III|2||32|291 292 293|
{FG}|2|1|JU|1244|Derecho Económico|II|4||64|1123|
{FG}|2|1|AD|1111|Estrategias de Comercio Internacional|I|4||64|104 1110|
{FG}|2|1|CO|1084B|Precios y Costos|I|6||96|104|
{FG}|2|2|MA|251|Estadística Aplicada|I|6||96|114|
{FG}|2|2|JU|1112|Régimen Aduanero|II|4||64|1123 1244|
{FG}|2|2|CO|1114|Operatoria de Comercio Exterior|I|6||96|1110|
{FG}|3|1|AD/CO|1115|Logística Internacional|I|4||64|1110|
{FG}|3|1|AD|1117|Investigación de Mercados Internacionales|I|6||96|101 1111 251|
{FG}|3|1|EC|1116|Teoría del Comercio y Finanzas Internacionales|I|4||64|101 1110|
{FG}|3|2|AD|1113|Marketing Internacional|I|4||64|1084B 1117|
{FG}|3|2|AD|1118|Seminario de Práctica Profesional|I|6||96|1114 1115 1117|
{FG}|3|2|AD|1122|Internacionalización de Pymes Regionales|I|4||64|1114 1116|
{RI}|||SA|598|Nivel de Inglés Técnico I||4||64||
{RI}|||AD|1119|Nivel de Computación Sistema María-Malvina|III|2||32||
{RI}|||SE|360|Seminario de Práctica Sociocomunitaria||||50||
"""),

 dict(id="tec-periodismo", nivel="pregrado", nombre="Tecnicatura Universitaria en Periodismo Digital", plan="OCS 2322/2017", horas=1810,
      url="https://eco.mdp.edu.ar/tupd",
      notas=["Además se acreditan 112 hs de Requisitos Curriculares Obligatorios, comunes a todos los ingresantes.",
             "Las materias marcadas 1/2/3 se dictan en más de un cuatrimestre; se ubican en el primero indicado."],
      filas=f"""
{FG}|1|1/2/3|CS|1093|Taller de lectura y escritura académica|III|2||32||
{FG}|1|1/2/3|EC|101|Introducción a la Economía|I|6||96||
{FG}|1|1/2/3|CS|1091|Teoría de la Comunicación|I|4||64||
{FG}|1|1/2/3|AD|104|Principios de Administración|I|6||96||
{FG}|1|2/1/3|CS|1092|Introducción a los medios de comunicación|I|4||64||
{FG}|1|2/1/3|AD|1104|Tecnologías de la Información|I|4||64||
{FG}|1|2/1/3|CS|218|Teoría Social y Política|II|6||96||
{FG}|1|2/1/3|JU|1090|Derecho y Políticas de Comunicación|I|4||64||
{FG}|2|1/2/3|CS|1105|Comunicación y Medios|II|4||64|1091 1093 1104|
{FG}|2|1/2/3|CS|1094|Lenguajes del periodismo multimedial|I|4||64|1092 1093|
{FG}|2|1/2/3|CS|1103|Semiótica|I|6||96|1093|
{FG}|2|1/2/3|CS|215|Antropología Cultural|II|3||48|1093|
{FG}|2|2/1/3|CS|1099|Taller de periodismo gráfico|I|4||64|1094|
{FG}|2|2/1/3|CS|1098|Taller de contenidos en redes sociales|I|4||64|1094 1104|
{FG}|2|2/1/3|AD|1106|Creación de Empresas|III|4||64|104 1093|
{FG}|2|2/1/3|AD|1108|Opinión Pública|III|4||64|1090 1105|
{FG}|3|1/2/3|CS|1095|Taller de redacción periodística para medios digitales|I|4||64|1099 1104|
{FG}|3|1/2/3|CS|1096|Taller de periodismo radial|I|4||64|1094|
{FG}|3|1/2/3|CS|1097|Taller de periodismo televisivo|I|4||64|1094|
{FG}|3|1/2/3|AD|1107|Las organizaciones asociativas y la economía solidaria|III|4||64|104 1093|
{FG}|3|2/1/3|CS|1109|Diseño de Proyectos Digitales Colaborativos|III|4||64|1090 1094|
{FG}|3|2/1/3|CS|1101|Gestión de la Información en Red|III|4||64|1098 1105 1090|
{FG}|3|2/1/3|CS|1102|Seminario de Práctica Profesional|III|6||96|1090 1095 1096 1097 1098|
{RI}|||SA|598|Nivel de Inglés Técnico I||4||64||
{RI}|||SE|397|Acreditar 50 horas de Práctica Profesional Comunitaria||||50||
"""),

 dict(id="tec-turismo", nivel="pregrado", nombre="Tecnicatura Universitaria en Turismo", plan="OCA 1902/2015 · RM 518/2017", horas=1794,
      url=BASE + "2214-plan-de-estudio-tec-turismo?catid=184:planes-de-estudio&Itemid=1106", notas=[],
      filas=f"""
{IN}|1||SA|291|Taller de Introducción a la Vida Universitaria|III|1||16||
{IN}|1||SA|292|Aproximación a las Ciencias Económicas y Sociales|III|4||64||
{IN}|1||SA|294|Principios Turísticos y Recreativos|III|2||32||
{CB}|1|1|EC|101|Introducción a la Economía|I|6||96|291 292 294|
{CB}|1|1|CO|127|Contabilidad|I|6||96|291 292 294|
{CB}|1|1|TU|161|Introducción al Turismo|I|4||64|291 292 294|
{CB}|1|2|TU|277|Espacios Turísticos Mundiales|I|6||96|161|
{CB}|1|2|MA|151|Estadística Aplicada al Turismo|I|6||96|291 292 294|
{CB}|1|2|AD|104|Principios de Administración|I|6||96|291 292 294|
{CB}|2|1|JU|2001|Turismo y Legislación|II|4||64|291 292 294|
{CB}|2|1|TU|219|Turismo y Naturaleza|II|4||64|161|
{CB}|2|1|TU|323|Espacios Turísticos Americanos|II|6||96|277|
{CB}|2|2|TU|235|Alojamiento y Recreación|II|4||64|104 161|
{CB}|2|2|TU|237|Turismo y Cultura|II|4||64|161|
{CB}|2|2|TU|2002|Animación sociocultural|I|4||64|161|
{CB}|3|1|TU|391|Viajes y Transporte|II|4||64|104 161|
{CB}|3|1|AD|413|Comercialización Turística|II|4||64|104 235|
{CB}|3|1|TU|2003|Práctica Profesional Técnica I|III|4||64|235|
{CB}|3|2|TU|341|Turismo de Reuniones|I|4||64|104 235|
{CB}|3|2|TU|2004|Sector Público y Turismo|I|4||64|104 2001|
{CB}|3|2|TU|2005|Práctica Profesional Técnica II|III|4||64|391|
{RI}|||SA|596|Inglés Técnico I||4||64||
{RI}|||SA|597|Inglés Técnico II||4||64||
{RI}|||SA|2006|Nivel de Portugués||4||64||
{RI}|||AD|300|Nivel de Computación||2||32||
{RI}|||SA|283|Uso de Programas de Computación I||2||32|391|
{RI}|||SA|284|Uso de Programas de Computación II||2||32|235|
{RI}|||SE|362|Seminario de Práctica Sociocomunitaria||||50||
"""),
]

def _num(x):
    return int(x) if x.isdigit() else (x or None)

def parse(c):
    filas = c["filas"] if isinstance(c["filas"], list) else [l for l in c["filas"].strip().splitlines() if l.strip()]
    out = []
    for l in filas:
        p = [x.strip() for x in l.split("|")]
        assert len(p) == 12, l
        ciclo, anio, cuat, area, cod, nom, grupo, hs, bim, hc, corr, orient = p
        out.append(dict(ciclo=ciclo, anio=anio, cuat=cuat, area=area, cod=cod, nombre=nom, grupo=grupo,
                        hs_sem=_num(hs), hs_bim=_num(bim), hs_cuat=_num(hc),
                        corr=corr.split() if corr else [], orientacion=orient))
    return out

def todas():
    res = []
    for c in CARRERAS:
        d = {k: v for k, v in c.items() if k != "filas"}
        d["materias"] = parse(c)
        res.append(d)
    return res

if __name__ == "__main__":
    for c in todas():
        assert c.get("nivel") in ("grado", "pregrado"), f'{c["id"]}: falta nivel ("grado" o "pregrado")'
        codes =[m["cod"] for m in c["materias"]]
        dup = {x for x in codes if codes.count(x) > 1}
        miss = sorted({x for m in c["materias"] for x in m["corr"] if x not in codes})
        print(f'{c["id"]:24} {len(codes):3} materias  duplicados={dup or "-"}  correlativas sin materia={miss or "-"}')
