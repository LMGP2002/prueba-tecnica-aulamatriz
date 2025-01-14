from django import forms
from django.forms import ModelForm

from gestion_tareas.models import Tarea

# Clase que crea la estructura del formulario para crear tareas
class TareaForm(ModelForm):
    class Meta:
        model=Tarea
        fields=['titulo','descripcion','fecha_limite','prioridad']
        widgets ={
            'fecha_limite': forms.DateInput(attrs={'type':'date'})
        }