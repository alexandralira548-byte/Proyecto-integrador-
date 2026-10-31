import json
import os

ARCHIVO = "computadoras.json"

estados_iniciales = [
    "Funciona", "Funciona", "Con falla", "Funciona",
    "Funciona", "En revisión", "Funciona", "Con falla",
    "Funciona", "Funciona", "En revisión", "Funciona"
]

def cargar_computadoras():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    computadoras = []
    for numero, estado in enumerate(estados_iniciales, start=1):
        computadoras.append({
            "id": numero,
            "estado": estado,
            "tipo": "",
            "descripcion": "",
            "fecha": ""
        })

    guardar_computadoras(computadoras)
    return computadoras

def guardar_computadoras(computadoras):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(computadoras, archivo, ensure_ascii=False, indent=4)
      
