# Unidades académicas de la UNMdP (según www.mdp.edu.ar, octubre 2026).
# Solo las que tienen "carreras" cargadas se pueden elegir en el sitio; el resto figura como "próximamente".
from carreras import todas

FACULTADES = [
    dict(id="faud", nombre="Arquitectura, Urbanismo y Diseño", url="http://faud.mdp.edu.ar/"),
    dict(id="agrarias", nombre="Ciencias Agrarias", url="https://fca.mdp.edu.ar/sitio/"),
    dict(id="salud", nombre="Ciencias de la Salud y Trabajo Social", url="https://salud.mdp.edu.ar"),
    dict(id="eco", nombre="Ciencias Económicas y Sociales", sigla="FCEyS", url="https://eco.mdp.edu.ar/", carreras=todas(),
         # regla por defecto para cursar: "reg" = alcanza con la cursada aprobada de las correlativas; "ok" = final aprobado
         regla="reg",
         vigencia="La cursada aprobada tiene un año de vigencia (OCA 357/2025).",
         notas=["Los planes no indican si para cursar alcanza con la cursada aprobada de las correlativas o si se pide el final, "
                "y no lo encontramos en el régimen académico (OCA 810/2022 y OCA 357/2025). Por defecto se usa la cursada aprobada; "
                "podés cambiar la regla arriba del grafo. Para rendir el final se piden las correlativas aprobadas."]),
    dict(id="exactas", nombre="Ciencias Exactas y Naturales", url="http://exactas.mdp.edu.ar"),
    dict(id="derecho", nombre="Derecho", url="https://derecho.mdp.edu.ar"),
    dict(id="humanidades", nombre="Humanidades", url="https://humanidades.mdp.edu.ar/"),
    dict(id="ingenieria", nombre="Ingeniería", url="http://www.fi.mdp.edu.ar/"),
    dict(id="medicina", nombre="Medicina", url="http://medicina.mdp.edu.ar/"),
    dict(id="psicologia", nombre="Psicología", url="https://psicologia.mdp.edu.ar/"),
]

def todas_facultades():
    return [dict(f, carreras=f.get("carreras", [])) for f in FACULTADES]
