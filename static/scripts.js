
async function MostrarAlumnos() {
    const res = await fetch("/mostrar")
    const data = await res.json()


    const lista = document.getElementById("lista")
    lista.textContent = JSON.stringify(data,null,2)
}


async function cargarNota(event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value
    const materia = document.getElementById("materia").value
    const nota = document.getElementById("nota").value

    const res = await fetch("/cargar",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({nombre,materia,nota})
    })

    const data = await res.json()
    const mensaje = document.getElementById("mensaje")

    mensaje.textContent = data.mensaje
    MostrarAlumnos()
}

