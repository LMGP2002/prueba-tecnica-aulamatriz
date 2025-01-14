from django.shortcuts import redirect, render, get_object_or_404

from gestion_tareas.forms import TareaForm
from gestion_tareas.models import Tarea

# Create your views here.
# Función que se encarga de listar las tareas de la BD en la interfaz


def listar(request):
    tareas = Tarea.objects.filter(user=request.user)
    return render(request, 'listar.html', {
        'tareas': tareas
    })

# Función que se encarga de crear las tareas en la BD desde la interfaz


def crear(request):
    if request.method == 'GET':
        return render(request, 'crear.html', {
            'form': TareaForm
        })
    else:
        form = TareaForm(request.POST)
        tarea = form.save(commit=False)
        tarea.user = request.user
        tarea.save()
        return redirect('/')

# Función que se encarga de actualizar una tarea teniendo en cuenta su id


def actualizar(request, id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk=id)
        form = TareaForm(instance=tarea)
        return render(request, 'actualizar_eliminar.html', {
            'tarea': tarea,
            'form': form
        })
    else:
        tarea = get_object_or_404(Tarea, pk=id)
        form = TareaForm(request.POST, instance=tarea)
        form.save()
        return redirect('/')


# Función que se encarga de eliminar una tarea teniendo en cuenta su id

def eliminar(request, id):
    tarea=get_object_or_404(Tarea,pk=id)
    tarea.delete()
    return redirect('/')
