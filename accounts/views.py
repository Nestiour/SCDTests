from django.shortcuts import render, redirect


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
# Create your views here.


# ---------- ---------- ---------- ---------- ---------- Verificador de Permisos

def is_administrator(user):
    return user.groups.filter(name='Administrador').exists()



# ---------- ---------- ---------- ---------- ---------- Views

# ----- Acceso denegado
@login_required
def denegado(request): #denegado
    return render(request, 'accounts/denegado.html')

@login_required
@user_passes_test(is_administrator, login_url='/accounts/access_denied')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
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