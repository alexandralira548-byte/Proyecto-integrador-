from datetime import datetime

def calcular_resumen(computadoras):
    funcionan = sum(1 for pc in computadoras if pc["estado"] == "Funciona")
    fallas = sum(1 for pc in computadoras if pc["estado"] == "Con falla")
    revision = sum(1 for pc in computadoras if pc["estado"] == "En revisión")
    return funcionan, fallas, revision

def filtrar_computadoras(computadoras, filtro):
    if filtro == "Todas":
        return computadoras
    return [pc for pc in computadoras if pc["estado"] == filtro]

def actualizar_reporte(computadoras, numero, tipo, descripcion):
    for pc in computadoras:
        if pc["id"] == numero:
            pc["estado"] = "En revisión"
            pc["tipo"] = tipo
            pc["descripcion"] = descripcion
            pc["fecha"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            break
    return computadoras
  
