from django.shortcuts import render, redirect


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import UserCreationForm
# Create your views here.


# ---------- ---------- ---------- ---------- ---------- Verificador de Permisos

def is_administrator(user):
    return user.groups.filter(name='Administrador').exists()

def user_has_required_group(user):
    return user.groups.filter(name='Preceptor').exists() or user.groups.filter(name='Administrador').exists()

# ---------- ---------- ---------- ---------- ---------- Views


@user_passes_test(is_administrator, login_url='access_denied')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()

                # Obtén el grupo seleccionado en el formulario
                group_name = form.cleaned_data['group']

                # Asigna el usuario al grupo correspondiente
                group = Group.objects.get(name=group_name)
                user.groups.add(group)

                return redirect('inicio')
        except ValidationError as e:
            # Captura la excepción ValidationError y agrega el mensaje de error al formulario
            form.add_error('group', e.message)
                
    else:
        form = UserCreationForm()

    return render(request, 'accounts/registration/signup.html', {"form": form})


def signin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario es válido, inicia sesión
            login(request, user)
            # 'inicio' es la URL predeterminada si 'next' no está presente
            next_url = request.POST.get('next', 'inicio')
            return redirect(next_url)
        else:
            # El usuario no es válido, muestra un mensaje de error
            messages.error(
                request, 'Nombre de usuario o contraseña incorrectos.')

    # Si el método de solicitud es GET o si la autenticación falla, muestra el formulario de inicio de sesión
    return render(request, 'accounts/registration/signin.html', {
        "form":form
    })


#@login_required
def signout(request):
    logout(request)
    #return redirect('home')
    return redirect('inicio')



# ---------- ---------- ---------- ---------- ---------- Views Permisos
def access_denied(request):
    return render(request, 'accounts/registration/access_denied.html')