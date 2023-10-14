"""
URL configuration for sistema_control_docente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from scd import views
from django.contrib.auth.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('', include('accounts.urls')),
    # Extras
    path('calendario/', views.calendario, name='calendario'),
    path('en_desarrollo/', views.en_desarrollo, name='en_desarrollo'),
    path('access_denied/', views.access_denied, name='access_denied'),
    path('buscaminas/', views.buscaminas, name='buscaminas'),
    path('noticias/', views.noticias, name='noticias'),
    # Curso
    path('gestionCurso/', views.gestionCurso, name='gestionCurso'),
    path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
    path('eliminarCurso/<id_cur>', views.eliminarCurso, name='eliminarCurso'),
    path('edicionCurso/<id_cur>', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso, name='editarCurso'),
    # Docente
    path('gestionDocente/', views.gestionDocente, name='gestionDocente'),
    path('registrarDocente/', views.registrarDocente, name='registrarDocente'),
    path('eliminarDocente/<id_doc>', views.eliminarDocente, name='eliminarDocente'),
    path('edicionDocente/<id_doc>', views.edicionDocente, name='edicionDocente'),
    path('editarDocente/', views.editarDocente, name='editarDocente'),
    # Clase
    path('gestionClase/', views.gestionClase, name='gestionClase'),
    path('registrarClase/', views.registrarClase, name='registrarClase'),
    path('eliminarClase/<id_cla>', views.eliminarClase, name='eliminarClase'),
    path('edicionClase/<id_cla>', views.edicionClase, name='edicionClase'),
    path('editarClase/', views.editarClase, name='editarClase'),
    # Horario (DESARROLLAR - views, templates)
    path('gestionHorario/', views.gestionHorario, name='gestionHorario'),
    path('registrarHorario/', views.registrarHorario, name='registrarHorario'),
    path('eliminarHorario/<id_hor>', views.eliminarHorario, name='eliminarHorario'),
    path('edicionHorario/<id_hor>', views.edicionHorario, name='edicionHorario'),
    path('editarHorario/', views.editarHorario, name='editarHorario'),
    # Asistencia (templates)
    path('gestionAsistencia/', views.gestionAsistencia, name='gestionAsistencia'),
    path('registrarAsistencia/', views.registrarAsistencia, name='registrarAsistencia'),
    path('eliminarAsistencia/<id_asi>', views.eliminarAsistencia, name='eliminarAsistencia'),
    path('edicionAsistencia/<id_asi>', views.edicionAsistencia, name='edicionAsistencia'),
    path('editarAsistencia/', views.editarAsistencia, name='editarAsistencia'),
    # Materia (DESARROLLAR - views, templates)
    path('gestionMateria/', views.gestionMateria, name='gestionMateria'),
    path('registrarMateria/', views.registrarMateria, name='registrarMateria'),
    path('eliminarMateria/<id_mat>', views.eliminarMateria, name='eliminarMateria'),
    path('edicionMateria/<id_mat>', views.edicionMateria, name='edicionMateria'),
    path('editarMateria/', views.editarMateria, name='editarMateria'),
    # doc_mat (DESARROLLAR - views, templates)
    path('gestionDM/', views.gestionDM, name='gestionDM'),
    path('registrarDM/', views.registrarDM, name='registrarDM'),
    path('eliminarDM/<id_dm>', views.eliminarDM, name='eliminarDM'),
    path('edicionDM/<id_dm>', views.edicionDM, name='edicionDM'),
    path('editarDM/', views.editarDM, name='editarDM'),
]