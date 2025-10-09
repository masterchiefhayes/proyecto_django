from django import forms
from .models import Comentario, Estudiante

# Formulario de comentarios (asignación automática del estudiante)
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Escribe tu comentario aquí...'
            }),
        }

# Formulario de login de estudiante (crea automáticamente si no existe)
class LoginEstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=200, label="Dirección", widget=forms.TextInput(attrs={'class': 'form-control'}))
    carne = forms.CharField(max_length=20, label="Carné", widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        direccion = cleaned_data.get("direccion")
        carne = cleaned_data.get("carne")

        # Buscar o crear el estudiante automáticamente
        estudiante, created = Estudiante.objects.get_or_create(
            nombre=nombre,
            direccion=direccion,
            carne=carne
        )
        cleaned_data['estudiante'] = estudiante
        return cleaned_data
