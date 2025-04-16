from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

alumnos = [
    ['Juan' , [['Matematicas',8], ['Lengua',9], ['Sociales',7], ['Naturales',7]]],
    ['Ana'  , [['Lengua',9], ['Matematicas',10], ['Sociales',8], ['Naturales',6]]]
]

@app.route("/")
def index():
    return render_template("index.html")

# Agregar alumno o editar materia con nota
@app.route("/cargar", methods = ["POST"])
def cargar():
    data = request.get_json()
    nombre = data["nombre"]
    materia = data["materia"]
    nota = int(data["nota"])

    for alumno in alumnos:
        if alumno[0].lower() == nombre.lower():
            for m in alumno[1]:
                if m[0].lower() == materia.lower():
                    m[1] = nota
                    return jsonify({"mensaje":"Nota actualizada correctamente"})
            alumno[1].append([materia,nota])
            return jsonify({"mensaje":"Materia agregata correctamente"})
    alumnos.append([nombre, [[materia, nota]]])
    return jsonify({"mensaje": "Alumno creado correctamente."})

# Envia a los alumnos
@app.route("/mostrar", methods = ["GET"])
def mostrar():
    return jsonify(alumnos)


if __name__ == "__main__":
    app.run(debug=True)

