# Plan de Estudio Contador Público 2005 (Plan E) - FCEyS UNMdP
# Fuente: https://eco.mdp.edu.ar/component/content/article/206-plan-de-estudio-contador-publico-2005-plan-e-oca-n-880-04
# Campos: ciclo, orientacion, anio, cuat, area, cod, nombre, grupo, hs_sem, hs_bim, hs_cuat, correlativas

B, P, O, R = "Básico", "Profesional", "Orientación", "Requisito instrumental"

MATERIAS = [
    # CICLO BÁSICO
    (B, "", 1, 1, "EC", 101, "Introducción a la Economía", "I", 6, None, 96, []),
    (B, "", 1, 1, "AD", 104, "Principios de Administración", "I", 6, None, 96, []),
    (B, "", 1, 1, "MA", 102, "Matemática I", "I", 6, None, 96, []),
    (B, "", 1, 2, "CO", 103, "Contabilidad I", "I", 6, None, 96, []),
    (B, "", 1, 2, "CS", 180, "Historia Económica y Social I", "II", 4, None, 64, []),
    (B, "", 1, 2, "CS", 205, "Sociología", "II", 4, None, 64, []),
    (B, "", 1, 2, "MA", 209, "Matemática II", "I", 5, None, 80, [102]),
    (B, "", 2, 1, "EC", 314, "Macroeconomía I", "I", 6, None, 96, [101, 209]),
    (B, "", 2, 1, "AD", 308, "Funciones Organizacionales", "I", 6, None, 96, [104]),
    (B, "", 2, 1, "CS", 280, "Historia Económica y Social II", "II", 4, None, 64, [180]),
    (B, "", 2, 1, "JU", 202, "Derecho Constitucional", "II", 4, 32, None, []),
    (B, "", 2, 1, "JU", 307, "Derecho Administrativo", "II", 4, 32, None, []),
    (B, "", 2, 2, "CO", 210, "Contabilidad II", "I", 6, None, 96, [103]),
    (B, "", 2, 2, "EC", 208, "Microeconomía I", "I", 6, None, 96, [101, 209]),
    (B, "", 2, 2, "MA", 250, "Estadística", "I", 6, None, 96, [209]),
    # CICLO PROFESIONAL
    (P, "", 3, 1, "CO", 402, "Contabilidad III", "I", 5, None, 80, [210]),
    (P, "", 3, 1, "AD", 330, "Sistemas de Información", "I", 6, None, 96, [103, 308]),
    (P, "", 3, 1, "MA", 424, "Matemática Financiera", "I", 5, None, 80, [250]),
    (P, "", 3, 1, "JU", 340, "Derecho Privado", "II", 4, None, 64, [202, 307]),
    (P, "", 3, 2, "CO", 401, "Costos", "I", 6, None, 96, [210]),
    (P, "", 3, 2, "CO", 349, "Economía y Org. del Sector Público", "I", 6, None, 96, [202, 314]),
    (P, "", 3, 2, "JU", 503, "Sociedades", "II", 4, None, 64, [340]),
    (P, "", 3, 2, "CS", 201, "Metodología de las Ciencias Sociales", "III", 3, None, 48, [250]),
    (P, "", 4, 1, "CO", 430, "Análisis Económico y Financiero", "I", 6, None, 96, [308, 314, 402, 424, 401]),
    (P, "", 4, 1, "CO", 460, "Impuestos I", "I", 6, None, 96, [307, 402, 349]),
    (P, "", 4, 1, "JU", 425, "Derecho del Trabajo y de la Seg. Social", "II", 4, None, 64, [307, 340]),
    (P, "", 4, 2, "AD", 490, "Elementos de Adm. de Personal", "I", 4, 32, None, [308]),
    (P, "", 4, 2, "AD", 491, "Elementos de Adm. de Comercialización", "I", 4, 32, None, [308, 314, 250]),
    (P, "", 4, 2, "CO", 527, "Auditoría", "I", 6, None, 96, [402, 330, 401, 503]),
    (P, "", 4, 2, "SA", 499, "Ética y Responsabilidad Social", "III", 2, None, 32, []),
    (P, "", 5, 1, "CO", 525, "Impuestos II", "I", 6, None, 96, [460]),
    (P, "", 5, 1, "AD", 602, "Información para Control Gerencial", "I", 6, None, 96, [330, 430]),
    (P, "", 5, 1, "JU", 590, "Empresas en Crisis. Títulos de Créd.", "II", 4, None, 64, [503, 430, 425, 527]),
    (P, "", 5, 2, "CO", 805, "Práctica Profesional", "III", 6, None, 100, [527, 590, 525]),
    # CICLO DE ORIENTACIÓN (se elige una)
    (O, "Teoría Contable Avanzada", 5, 2, "CO", 510, "Normas Contables Comparadas", "", 4, None, 64, [525, 527]),
    (O, "Gestión Pública", 5, 2, "AD", 560, "Org. y Adm. Financiera del Estado", "", 4, None, 64, [349, 460]),
    (O, "Gestión de Org. de la Economía Regional", 5, 2, "AD", 565, "Creación de Empresas", "", 4, None, 64, [430, 425, 490, 491]),
    (O, "Derecho Empresario (Jurídico-Contable)", 5, 2, "JU", 592, "Contratos Especiales", "", 4, None, 64, []),
    (O, "Gestión Financiera", 5, 2, "EC", 504, "Análisis y Evaluación de Proyectos", "", 4, None, 64, [430]),
    # REQUISITOS INSTRUMENTALES OBLIGATORIOS
    (R, "", None, None, "SA", 595, "Nivel de Inglés Técnico I", "", None, None, None, []),
    (R, "", None, None, "AD", 300, "Nivel de Computación", "", None, None, None, []),
    (R, "", None, None, "SA", 299, "Taller Uso de Programas de Computación", "", None, None, None, []),
    (R, "", None, None, "SI", 296, "Acreditar 30 horas de Investigación", "", None, None, None, []),
    (R, "", None, None, "SE", 368, "Seminario de Práctica Sociocomunitaria", "", None, None, None, []),
    (R, "", None, None, "SA", 298, "Acreditar 30 hs Pasantías o Prácticas Profesionales Académicas", "", None, None, None, []),
]

FIELDS = ["ciclo", "orientacion", "anio", "cuat", "area", "cod", "nombre", "grupo",
          "hs_sem", "hs_bim", "hs_cuat", "corr"]

def as_dicts():
    return [dict(zip(FIELDS, m)) for m in MATERIAS]

if __name__ == "__main__":
    codes = {m[5] for m in MATERIAS}
    for m in MATERIAS:
        for c in m[11]:
            assert c in codes, (m, c)
    print(len(MATERIAS), "materias OK")
