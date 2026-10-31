from flask import Flask, request, render_template_string
from datos.datos import cargar_computadoras, guardar_computadoras
from negocio.logica import calcular_resumen, filtrar_computadoras, actualizar_reporte

app = Flask(__name__)

PAGINA = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Reporte de Fallas</title>
    <style>
        * { box-sizing: border-box; }
        body { margin: 0; padding: 25px; font-family: Arial, sans-serif; background: #e8ebf0; color: #172334; }
        .contenedor { max-width: 1200px; margin: auto; padding: 30px; background: #f3f6fc; border-radius: 12px; }
        header { display: flex; justify-content: space-between; align-items: center; gap: 15px; flex-wrap: wrap; margin-bottom: 25px; }
        h1 { font-size: 28px; margin-bottom: 5px; }
        .subtitulo { color: #6b7280; margin-top: 0; }
        button, select, input, textarea { padding: 11px; border: 1px solid #dce2eb; border-radius: 8px; font-size: 14px; }
        button { cursor: pointer; }
        .boton { background: #2563eb; color: white; border: none; font-weight: bold; }
        .resumen { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 25px; }
        .resumen-card { background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; }
        .numero { font-size: 34px; font-weight: bold; }
        .verde { color: #16804a; }
        .rojo { color: #b42332; }
        .amarillo { color: #946200; }
        .barra { display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
        .filtros { display: flex; flex-wrap: wrap; gap: 8px; }
        .filtro { background: white; color: #555; text-decoration: none; padding: 10px 15px; border: 1px solid #dce2eb; border-radius: 25px; }
        .activo { background: #102d50; color: white; }
        .computadoras { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 14px; }
        .pc { background: white; padding: 16px; border: 1px solid #e2e8f0; border-radius: 12px; }
        .pc h3 { margin: 0 0 12px; }
        .estado { display: inline-block; padding: 6px 10px; border-radius: 20px; font-size: 13px; }
        .estado-funciona { background: #dcfce7; color: #16804a; }
        .estado-falla { background: #fee2e2; color: #b42332; }
        .estado-revision { background: #fef3c7; color: #946200; }
        .detalle { margin-top: 12px; color: #2563eb; font-size: 13px; }
        .modal { display: none; position: fixed; inset: 0; background: #0007; justify-content: center; align-items: center; padding: 15px; }
        .formulario { background: white; padding: 25px; border-radius: 12px; width: 100%; max-width: 550px; }
        .formulario label { display: block; margin: 15px 0 7px; font-weight: bold; }
        .formulario select, .formulario textarea { width: 100%; }
        textarea { min-height: 100px; resize: vertical; }
        .acciones { display: flex; justify-content: flex-end; gap: 10px; margin-top: 20px; }
        .mensaje { background: white; padding: 30px; border-radius: 12px; text-align: center; max-width: 600px; margin: 70px auto; }
        .nota { color: #6b7280; font-size: 12px; margin-top: 25px; }
    </style>
</head>
<body>
{% if confirmacion %}
    <div class="mensaje">
        <h1 style="color: #16804a;">✓ Reporte enviado</h1>
        <p>La PC {{ pc_reporte }} quedó En revisión.</p>
        <a href="/" class="boton" style="display:inline-block; padding:12px; text-decoration:none;">Volver al panel</a>
    </div>
{% else %}
<main class="contenedor">
    <header>
        <div>
            <h1>Sistema de Reporte de Fallas</h1>
            <p class="subtitulo">Panel del docente · UNAN-León</p>
        </div>
        <button onclick="abrirFormulario()" class="boton">Reportar falla</button>
    </header>
    <section class="resumen">
        <div class="resumen-card"><div class="numero verde">{{ funcionan }}</div><p>Funcionan</p></div>
        <div class="resumen-card"><div class="numero rojo">{{ fallas }}</div><p>Con falla</p></div>
        <div class="resumen-card"><div class="numero amarillo">{{ revision }}</div><p>En revisión</p></div>
    </section>
    <div class="barra">
        <nav class="filtros">
            {% for nombre, valor in filtros %}
                <a class="filtro {% if filtro == valor %}activo{% endif %}" href="/?estado={{ valor }}">{{ nombre }}</a>
            {% endfor %}
        </nav>
        <button onclick="abrirFormulario()" class="boton">Reportar falla</button>
    </div>
    <section class="computadoras">
        {% for pc in computadoras %}
            <article class="pc">
                <h3>PC {{ pc.id }}</h3>
                <span class="estado {% if pc.estado == 'Funciona' %}estado-funciona{% elif pc.estado == 'Con falla' %}estado-falla{% else %}estado-revision{% endif %}">{{ pc.estado }}</span>
                <p class="detalle">{{ pc.tipo if pc.tipo else 'Sin detalles' }}</p>
            </article>
        {% endfor %}
    </section>
    <p class="nota">Prototipo académico. Los estados deben verificarse físicamente.</p>
</main>
<div class="modal" id="modal">
    <form class="formulario" method="POST" action="/reportar">
        <h2>Reportar falla</h2>
        <label for="computadora">Computadora</label>
        <select name="computadora" id="computadora" required>
            {% for numero in range(1, 13) %}<option value="{{ numero }}">PC {{ numero }} · Laboratorio 1</option>{% endfor %}
        </select>
        <label for="tipo">Tipo de falla</label>
        <select name="tipo" id="tipo" required>
            <option value="">Selecciona una falla</option>
            <option>No enciende</option>
            <option>Problema con el teclado o mouse</option>
            <option>Problema de internet</option>
            <option>Pantalla sin imagen</option>
            <option>Problema con los programas</option>
            <option>Otro problema</option>
        </select>
        <label for="descripcion">Descripción</label>
        <textarea name="descripcion" id="descripcion" required></textarea>
        <div class="acciones">
            <button type="button" onclick="cerrarFormulario()">Cancelar</button>
            <button type="submit" class="boton">Enviar reporte</button>
        </div>
    </form>
</div>
<script>
function abrirFormulario() { document.getElementById("modal").style.display = "flex"; }
function cerrarFormulario() { document.getElementById("modal").style.display = "none"; }
</script>
{% endif %}
</body>
</html>
"""

@app.route("/")
def inicio():
    computadoras = cargar_computadoras()
    filtro = request.args.get("estado", "Todas")
    funcionan, fallas, revision = calcular_resumen(computadoras)
    visibles = filtrar_computadoras(computadoras, filtro)
    filtros = [("Todas", "Todas"), ("Funcionan", "Funciona"), ("Con falla", "Con falla"), ("En revisión", "En revisión")]
    return render_template_string(PAGINA, computadoras=visibles, funcionan=funcionan, fallas=fallas, revision=revision, filtro=filtro, filtros=filtros, confirmacion=False)

@app.route("/reportar", methods=["POST"])
def reportar():
    computadoras = cargar_computadoras()
    numero = request.form.get("computadora", type=int)
    tipo = request.form.get("tipo", "").strip()
    descripcion = request.form.get("descripcion", "").strip()
    if not tipo or not descripcion or numero is None:
        return "Datos incompletos", 400
    actualizar_reporte(computadoras, numero, tipo, descripcion)
    guardar_computadoras(computadoras)
    return render_template_string(PAGINA, confirmacion=True, pc_reporte=numero)

if __name__ == "__main__":
    app.run(debug=True)
  
