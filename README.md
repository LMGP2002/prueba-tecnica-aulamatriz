
# Documentación del Proyecto de Gestión de Tareas con Django

## Descripción General

Este proyecto es una aplicación web desarrollada con Django que permite a los usuarios gestionar tareas de manera eficiente. Incluye funcionalidades completas de CRUD (Crear, Leer, Actualizar, Eliminar) para tareas.

### Estructura del Proyecto

El proyecto cuenta con una sola app principal llamada `gestion_tareas`. A continuación, se describe la funcionalidad clave implementada:

- **Listar tareas**: Muestra todas las tareas asociadas al usuario autenticado.
- **Crear tareas**: Permite a los usuarios registrar nuevas tareas con detalles como título, descripción, prioridad y fecha límite.
- **Actualizar tareas**: Facilita la edición de tareas existentes basadas en su ID.
- **Eliminar tareas**: Permite borrar tareas específicas identificadas por su ID.

---

## Archivos y Código

### Modelos

El modelo `Tarea` define la estructura de la tabla en la base de datos y sus atributos clave:

```python
from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    prioridad_opciones = [('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    prioridad = models.CharField(choices=prioridad_opciones, default='alta', max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo
```

### Formularios

El formulario `TareaForm` facilita la validación y captura de datos para las tareas.

```python
from django import forms
from django.forms import ModelForm
from gestion_tareas.models import Tarea

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_limite', 'prioridad']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'})
        }
```

### Vistas

Las vistas gestionan la lógica de la aplicación.

- **Listar tareas**:

```python
def listar(request):
    tareas = Tarea.objects.filter(user=request.user)
    return render(request, 'listar.html', {
        'tareas': tareas
    })
```

- **Crear tareas**:

```python
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
```

- **Actualizar tareas**:

```python
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
```

- **Eliminar tareas**:

```python
def eliminar(request, id):
    tarea = get_object_or_404(Tarea, pk=id)
    tarea.delete()
    return redirect('/')
```

### Administración

El modelo `Tarea` está registrado en el panel de administración para una gestión más sencilla.

```python
from django.contrib import admin
from gestion_tareas.models import Tarea

admin.site.register(Tarea)
```

---

## Configuración del Proyecto

### `settings.py`

El archivo `settings.py` incluye las configuraciones básicas del proyecto, como las apps instaladas, bases de datos y middleware.

```python
INSTALLED_APPS = [
    ...
    'gestion_tareas',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

---

## Plantillas

El proyecto utiliza plantillas para el renderizado dinámico del contenido.

- `layout.html`: Base para todas las páginas.
- `listar.html`: Página para listar tareas.
- `crear.html`: Página para crear una tarea nueva.
- `actualizar_eliminar.html`: Página para actualizar o eliminar tareas.

---

## Consideraciones Finales

Este proyecto es extensible y permite agregar más funcionalidades, como notificaciones de recordatorio de tareas, opciones de filtro y búsqueda, y mejoras de seguridad.

### Requerimientos
- **Python 3.x**
- **Django 5.x**
- **SQLite** (por defecto)

---

**Autor**: [Tu Nombre]  
**Última Actualización**: [Fecha]
