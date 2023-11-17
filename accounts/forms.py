from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(BaseUserCreationForm):
    # ... otros campos del modelo
    nombre = forms.CharField(max_length=255, required=True)
    apellido = forms.CharField(max_length=255, required=True)
    correo_electronico = forms.EmailField(required=True)

    GROUP_CHOICES = [
        ('Preceptor', 'Preceptor'),
        ('Docente', 'Docente'),
    ]
    group = forms.ChoiceField(choices=GROUP_CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = User  # Aquí debes especificar el modelo de usuario, que en este caso es el modelo por defecto de Django
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido', 'correo_electronico', 'group']

    def clean(self):
        cleaned_data = super().clean()
        group = cleaned_data.get('group')

        if not group:
            raise forms.ValidationError("Debes seleccionar un grupo.")

        return cleaned_data