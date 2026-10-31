def guardar_reporte(reporte):
    if not reporte:
        return False
    
    with open("registros_fallas.txt", "a") as archivo:
        archivo.write(f"{reporte['categoria']} - {reporte['descripcion']} - {reporte['estado']}\n")
    
    return True

