# DIAGRAMA ENTIDAD-RELACION (DER)

SISTEMA DE REPORTE DE FALLAS DE COMPUTADORAS DE LABORATORIO

1. DESCRIPCION

El diagrama representa la estructura de los datos del sistema. Está compuesto por ocho entidadesque permiten 
registrar usuarios, laboratorios, equipos, categoríasde fallas, reportes, estados, seguimientos y soluciones.

2. ENTIDADES

TBL_USUARIO
- usu_id (PK)
- usu_codigo (UQ)
- usu_nombre_completo
- usu_correo (UQ)
- usu_telefono
- usu_rol

TBL_LABORATORIO
- lab_id (PK)
- lab_nombre
- lab_edificio
- lab_capacidad

TBL_EQUIPO
- equ_id (PK)
- equ_codigo_inventario (UQ)
- equ_tipo
- equ_marca
- equ_modelo
- equ_estado
- lab_id (FK)

TBL_CATEGORIA_FALLA
- cat_id (PK)
- cat_nombre (UQ)
- cat_descripcion

TBL_REPORTE_FALLA
- rep_id (PK)
- rep_fecha
- rep_descripcion
- usu_id (FK)
- equ_id (FK)
- cat_id (FK)
- est_id (FK)

TBL_ESTADO_FALLA
- est_id (PK)
- est_nombre (UQ)

TBL_SEGUIMIENTO
- seg_id (PK)
- rep_id (FK)
- usu_id_personal (FK)
- seg_fecha
- seg_comentario
- est_id (FK)

TBL_SOLUCION
- sol_id (PK)
- rep_id (FK, UQ)
- usu_id_personal (FK)
- sol_fecha
- sol_descripcion
- sol_tiempo_horas

3. RELACIONES

- Un laboratorio tiene muchos equipos (1:N).
- Un usuario puede generar muchos reportes (1:N).
- Un equipo puede tener muchos reportes (1:N).
- Una categoría puede relacionarse con muchos reportes (1:N).
- Un estado puede relacionarse con muchos reportes y seguimientos (1:N).
- Un reporte puede tener muchos seguimientos (1:N).
- Un reporte puede tener cero o una solución (1:0..1).
- Un usuario puede registrar muchos seguimientos y soluciones (1:N).

4. SIGNIFICADO DE LAS CLAVES

PK: clave primaria.
FK: clave foránea.
UQ: campo único.

5. CONCLUSION

El modelo permite organizar la información de los equipos y sus fallas, consultar el historial
de seguimiento y registrar las soluciones realizadas por el personal de mantenimiento.
