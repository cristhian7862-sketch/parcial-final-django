from django import forms
from .models import Programa


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ["codigo", "nombre", "facultad", "estado"]
        labels = {
            "codigo": "Código",
            "nombre": "Nombre del programa",
            "facultad": "Facultad",
            "estado": "Activo",
        }
        widgets = {
            "codigo": forms.TextInput(attrs={"placeholder": "Ej: ING-SIS"}),
            "nombre": forms.TextInput(attrs={"placeholder": "Ej: Ingeniería de Sistemas"}),
            "facultad": forms.TextInput(attrs={"placeholder": "Ej: Facultad de Ingeniería"}),
        }
        error_messages = {
            "codigo": {"unique": "Ya existe un programa con este código."},
        }
