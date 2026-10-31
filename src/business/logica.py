def procesar_reporte(descripcion, categoria):
    if not descripcion or not categoria:
        return {"exito": False, "mensaje": "La descripción y la categoría son obligatorias."}
    
    reporte_procesado = {
        "categoria": categoria.strip().capitalize(),
        "descripcion": descripcion.strip(),
        "estado": "Registrado"
    }
    
    return {"exito": True, "datos": reporte_procesado}
  
