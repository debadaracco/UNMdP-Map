"""Regenera index.html, carreras.json y la planilla a partir de facultades.py y carreras.py.
Uso (desde la carpeta datos):  python generar.py"""
import json, subprocess, sys
from facultades import todas_facultades

datos = todas_facultades()
t = open("visor_template.html", encoding="utf-8").read().replace("__DATA__", json.dumps(datos, ensure_ascii=False))
i = t.index('<div class="wrap">')
head = t[:i].replace("<style>", "<style>\nbody{margin:0;font-size:15px}*,*::before,*::after{box-sizing:border-box}", 1)
html = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="description" content="UNMdP Map: correlatividades de las carreras de la UNMdP para ver qué materias podés cursar.">\n'
        f'{head.strip()}\n</head>\n<body>\n{t[i:].strip()}\n</body>\n</html>\n')
open("../index.html", "w", encoding="utf-8").write(html)
json.dump(datos, open("carreras.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, "build_xlsx_all.py"], check=True)
print("index.html, carreras.json y unmdp-map_fceys.xlsx actualizados")
