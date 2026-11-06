# Sistema de Reporte de Fallas de Equipos de Cómputo

UNAN-León · Proyecto Integrador I · Hito 9 · CTIS25-SABE2-GP2

1. Integrantes del equipo

- Gleyssi Nereyda Barrera Pérez
- Andy Dayana Hernández Urrieta
- Jeisling María Muñoz Vallejos
- Alexandra Paola Lira Blandón

2. Descripción del proyecto

El proyecto consiste en el diseño de un sistema para reportar y dar seguimiento a las fallas que presentan los equipos de cómputo de los laboratorios de la universidad. Su propósito es facilitar el registro de problemas, la consulta de reportes y el seguimiento de las soluciones.

En este Hito 9 se presenta el prototipo de las interfaces, la estructura inicial del proyecto, la documentación técnica y el diseño de la base de datos. La conexión completa entre las capas se desarrollará en el siguiente hito.

3. Enlace del prototipo en Figma

"Ver prototipo del Sistema de Reporte de Fallas" (https://www.figma.com/design/YlSnNloiDYtkuojdrUjIkb?node-id=6-5)

El prototipo contiene diez pantallas editables que representan el recorrido principal del sistema, desde el acceso hasta el registro y seguimiento de las fallas. También incluye ejemplos de validaciones y consultas sin resultados.

4. Estructura del repositorio

docs/
src/
  presentation/
  business/
  data/
tests/
.gitignore
README.md

Descripción de las carpetas

- docs/: contiene la documentación técnica, el modelo de datos, el script SQL y las evidencias del prototipo.
- src/presentation/: contiene el código relacionado con la presentación e interfaces del sistema.
- src/business/: destinada a la lógica de negocio y al procesamiento de las solicitudes.
- src/data/: destinada a la administración y conexión con los datos.
- tests/: contiene la documentación de las pruebas realizadas al sistema.

Las carpetas que contienen archivos ".gitkeep" se conservan para mantener la estructura del proyecto, aunque todavía no tengan código implementado.

5. Documentación y evidencias

Dentro de la carpeta "docs/" se encuentran los siguientes recursos:

- Modelo_original_clase8.pdf: documento del modelo recuperado de la entrega de Classroom.
- schema_derivado_clase8.sql: script DDL de MySQL elaborado a partir del diccionario de datos. Se identifica como un esquema derivado porque no se encontró un archivo SQL original en el documento adjunto.
- PI1_Hito9_Memoria.docx y PDF: memoria técnica con la explicación de la arquitectura, el modelo de datos y las evidencias.
- wireframes/: contiene los archivos SVG de las diez pantallas del prototipo.
- evidencias/: contiene las capturas del trabajo realizado en Figma.

6. Recorrido del prototipo

El recorrido principal del sistema es el siguiente:

1. Acceso al sistema.
2. Visualización del tablero principal.
3. Registro de una falla.
4. Confirmación del reporte registrado.
5. Consulta y seguimiento del reporte.
6. Registro de la solución.
7. Consulta de reportes mediante filtros.

El prototipo también presenta ejemplos de validaciones y consultas sin resultados. Los campos y datos utilizados son simulados, por lo tanto, las pantallas representan el funcionamiento propuesto, pero no realizan autenticación ni almacenan información real.

7. Arquitectura del sistema

El proyecto se organiza mediante una arquitectura de tres capas:

- Capa de presentación: encargada de mostrar las interfaces y permitir la interacción del usuario.
- Capa de lógica de negocio: encargada de procesar las solicitudes y aplicar las reglas del sistema.
- Capa de datos: encargada de almacenar, consultar y administrar la información.

Esta separación permite organizar el código y facilita el desarrollo y mantenimiento del sistema.

8. Instalación y ejecución

Para ejecutar el sistema localmente se necesita tener Python instalado.

Primero, se debe instalar Flask desde la terminal:

pip install Flask

Después, desde la carpeta principal del proyecto, ejecutar:

python src/presentation/app.py

Luego, abrir en el navegador la dirección local que muestra Flask, normalmente:

http://127.0.0.1:5000

9. Preparación para el siguiente hito

Para continuar con el desarrollo del proyecto se deberán realizar las siguientes actividades:

1. Clonar el repositorio y preparar el entorno de trabajo.
2. Revisar la documentación de la arquitectura y el modelo de datos.
3. Comparar el esquema SQL derivado con el documento original.
4. Crear una base de datos vacía en MySQL y seleccionar su nombre antes de ejecutar el script DDL.
5. Desarrollar las vistas, los servicios y los repositorios por separado.
6. Implementar la conexión entre la capa de datos y la lógica de negocio.

El script SQL está preparado para MySQL 8.0.16 o posterior y no contiene instrucciones para eliminar tablas ni credenciales de acceso.

10. Verificación y colaboración

La navegación del prototipo puede comprobarse desde la opción Presentar de Figma. El diseño de la base de datos se revisó tomando como referencia las ocho entidades del diccionario de datos; sin embargo, el script SQL todavía no se ha ejecutado en MySQL.

Cada integrante deberá aportar sus propios cambios y commits al repositorio, conservando el historial de trabajo del equipo. Para organizar los mensajes de confirmación se pueden utilizar los prefijos "docs:", "feat:" y "fix:".

11. Estado actual del proyecto

Este repositorio contiene la documentación, el prototipo de interfaces, el diseño de datos y la estructura inicial de las tres capas solicitadas para el Hito 9. La implementación completa y la conexión real entre la capa de datos y la lógica de negocio corresponden al siguiente hito.
