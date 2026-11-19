from django.shortcuts import render, redirect
from .models import Tarea
from django.http import HttpResponse

# def inicio(request):
#     return HttpResponse("Hola, esta es mi aplicación de tareas")


def inicio(request):
    tareas = Tarea.objects.all()

    return render(request, "tareasapp/inicio.html", {"tareas": tareas})



def crear_tarea(request):

    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        completada = 'completada' in request.POST

        Tarea.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            completada=completada
        )

        return redirect('inicio')
    return render(request, 'tareasapp/crear.html')


def detalle_tarea(request, id):

    tarea = Tarea.objects.get(id=id)

    return render(request, 'tareasapp/detalle.html', {
        'tarea': tarea
    })

def editar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == "POST":
        tarea.titulo = request.POST["titulo"]
        tarea.descripcion = request.POST["descripcion"]
        tarea.completada = "completada" in request.POST
        tarea.save()
        return redirect("inicio")
    return render(request, "tareasapp/editar.html", {"tarea": tarea})

def eliminar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == "POST":
        tarea.delete()
        return redirect("inicio")
    return render(request, "tareasapp/eliminar.html", {"tarea": tarea})