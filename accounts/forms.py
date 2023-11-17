from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(BaseUserCreationForm):
    # ... otros campos del modelo

    GROUP_CHOICES = [
        ('Preceptor', 'Preceptor'),
        ('Docente', 'Docente'),
    ]
    group = forms.ChoiceField(choices=GROUP_CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = User  # Aquí debes especificar el modelo de usuario, que en este caso es el modelo por defecto de Django
        fields = ['username', 'password1', 'password2', 'group']

    def clean(self):
        cleaned_data = super().clean()
        group = cleaned_data.get('group')

        if not group:
            raise forms.ValidationError("Debes seleccionar un grupo.")

        return cleaned_data