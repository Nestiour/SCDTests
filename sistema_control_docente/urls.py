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
    path('consultar/Asistencia/', views.consultarAsistencia, name='consultarAsistencia'),
    path('', include('accounts.urls')),
    # Extras
    path('calendario/', views.calendario, name='calendario'),
    path('en_desarrollo/', views.en_desarrollo, name='en_desarrollo'),
    path('access_denied/', views.access_denied, name='access_denied'),
    path('buscaminas/', views.buscaminas, name='buscaminas'),
    path('noticias/', views.noticias, name='noticias'),
    path('ayuda/', views.ayuda, name='ayuda'),
    # Curso
    path('gestion/Curso/', views.gestionCurso, name='gestionCurso'),
    path('registrar/Curso/', views.registrarCurso, name='registrarCurso'),
    path('eliminar/Curso/<id_cur>', views.eliminarCurso, name='eliminarCurso'),
    path('edicion/Curso/<id_cur>', views.edicionCurso, name='edicionCurso'),
    path('editar/Curso/', views.editarCurso, name='editarCurso'),
    path('horario/Curso/<id_cur>', views.horarioCurso, name='horarioCurso'),
    # Docente
    path('gestion/Docente/', views.gestionDocente, name='gestionDocente'),
    path('registrar/Docente/', views.registrarDocente, name='registrarDocente'),
    path('eliminar/Docente/<id_doc>', views.eliminarDocente, name='eliminarDocente'),
    path('edicion/Docente/<id_doc>', views.edicionDocente, name='edicionDocente'),
    path('editar/Docente/', views.editarDocente, name='editarDocente'),
    # Clase
    path('gestion/Clase/', views.gestionClase, name='gestionClase'),
    path('registrar/Clase/', views.registrarClase, name='registrarClase'),
    path('eliminar/Clase/<id_cla>', views.eliminarClase, name='eliminarClase'),
    path('edicion/Clase/<id_cla>', views.edicionClase, name='edicionClase'),
    path('editar/Clase/', views.editarClase, name='editarClase'),
    # Horario
    path('gestion/Horario/', views.gestionHorario, name='gestionHorario'),
    path('registrar/Horario/', views.registrarHorario, name='registrarHorario'),
    path('eliminar/Horario/<id_hor>', views.eliminarHorario, name='eliminarHorario'),
    path('edicion/Horario/<id_hor>', views.edicionHorario, name='edicionHorario'),
    path('editar/Horario/', views.editarHorario, name='editarHorario'),
    # Asistencia
    path('gestion/Asistencia/', views.gestionAsistencia, name='gestionAsistencia'),
    path('gestion/Asistencia/hoy', views.verAsistencia, name='verAsistencia'),
    path('gestion/Docente/Asistencia/<id_doc>', views.gestionDA, name='gestionDA'),
    path('registrar/Asistencia/', views.registrarAsistencia, name='registrarAsistencia'),
    path('eliminar/Asistencia/<id_asi>', views.eliminarAsistencia, name='eliminarAsistencia'),
    path('edicion/Asistencia/<id_asi>', views.edicionAsistencia, name='edicionAsistencia'),
    path('editar/Asistencia/', views.editarAsistencia, name='editarAsistencia'),
    # Materia
    path('gestion/Materia/', views.gestionMateria, name='gestionMateria'),
    path('registrar/Materia/', views.registrarMateria, name='registrarMateria'),
    path('eliminar/Materia/<id_mat>', views.eliminarMateria, name='eliminarMateria'),
    path('edicion/Materia/<id_mat>', views.edicionMateria, name='edicionMateria'),
    path('editar/Materia/', views.editarMateria, name='editarMateria'),
    # doc_mat
    path('gestion/DM/', views.gestionDM, name='gestionDM'),
    path('registrar/DM/', views.registrarDM, name='registrarDM'),
    path('eliminar/DM/<id_dm>', views.eliminarDM, name='eliminarDM'),
    path('edicion/DM/<id_dm>', views.edicionDM, name='edicionDM'),
    path('editar/DM/', views.editarDM, name='editarDM'),
]