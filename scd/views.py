from django.shortcuts import render, redirect
from .models import *
from .utils import *
# DB
from django.db.utils import IntegrityError
from django.db.models import Case, When
# -
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# ---------- ---------- ---------- ---------- ---------- Inicio
#@login_required
def inicio(request):
    bienvenida = saludo()
    return render(request, 'inicio.html', {'saludo': bienvenida})

# ---------- ---------- ---------- ---------- ---------- Calendario
@login_required
def calendario(request):
    return render(request, 'Extras\\calendario.html')

# ---------- ---------- ---------- ---------- ---------- En_desarrollo
def en_desarrollo(request):
    return render(request, 'Extras\\en_desarrollo.html')

# ---------- ---------- ---------- ---------- ---------- Access_denied
def access_denied(request):
    return render(request, 'Extras\\access_denied.html')

# ---------- ---------- ---------- ---------- ---------- Buscaminas
def buscaminas(request):
    return render(request, 'Extras\\buscaminas.html')

# ---------- ---------- ---------- ---------- ---------- Noticias
def noticias(request):
    noticias = obtener_noticias_rss()
    horoscopos = obtener_horoscopos()
    return render(request, 'Extras\\noticias.html', {'noticias':noticias, 'horoscopos': horoscopos})


# ---------- ---------- ---------- ---------- ---------- Curso
@login_required
def gestionCurso(request):
    cursos = Curso.objects.all().order_by('anio', 'division', 'turno')
    return render(request, 'Curso\gestionCurso.html', {'cursos': cursos})

@login_required
def registrarCurso(request):
    if request.method == 'GET':
        return render(request, 'Curso\gestionCurso.html')
    else:
        anio = request.POST['anio']
        division = request.POST['division']
        especialidad = request.POST['especialidad']
        turno = request.POST['turno']
        try:
            curso = Curso.objects.create(anio=anio, division=division, especialidad=especialidad, turno=turno)
            messages.success(request, '¡Registrado!')
        except:
            messages.error(request, "¡Ocurrió un error!")
    return redirect('gestionCurso')

@login_required
def eliminarCurso(request, id_cur):
    curso = Curso.objects.get(id_cur=id_cur)
    curso.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionCurso')

@login_required
def edicionCurso(request, id_cur):
    curso = Curso.objects.get(id_cur=id_cur)
    return render(request, "Curso\edicionCurso.html", {"curso": curso})

@login_required
def editarCurso(request):
    id_cur = request.POST['id_cur']
    anio = request.POST['anio']
    division = request.POST['division']
    especialidad = request.POST['especialidad']
    turno = request.POST['turno']
    # -
    curso = Curso.objects.get(id_cur=id_cur)
    curso.anio = anio
    curso.division = division
    curso.especialidad = especialidad
    curso.turno = turno
    curso.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('gestionCurso')

# ---------- ---------- ---------- ---------- ---------- Docente
@login_required
def gestionDocente(request):
    docentes = Docente.objects.all().order_by('apellido')
    return render(request, 'Docente\gestionDocente.html', {'docentes': docentes})

@login_required
def registrarDocente(request):
    if request.method == 'GET':
        return render(request, 'Docente\gestionDocente.html')
    else:
        cuil = request.POST['cuil']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        celular = request.POST['celular']
        email = request.POST['email']
        domicilio = request.POST['domicilio']
        localidad = request.POST['localidad']
        provincia = request.POST['provincia']
        genero = request.POST['genero']
        estado = request.POST['estado']
        try:
            docente = Docente.objects.create(cuil=cuil, nombre=nombre, apellido=apellido, celular=celular, email=email, domicilio=domicilio, localidad=localidad, provincia=provincia, genero=genero, estado=estado)
            messages.success(request, '¡Registrado!')
        except IntegrityError as e:
            messages.error(request, '¡Ya existe un Docente con este CUIL!')
        except Exception as e:
            messages.error(request, f"¡Ocurrió un error! {e}")
    return redirect('gestionDocente')

@login_required
def eliminarDocente(request, id_doc):
    docente = Docente.objects.get(id_doc=id_doc)
    docente.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionDocente')

@login_required
def edicionDocente(request, id_doc):
    docente = Docente.objects.get(id_doc=id_doc)
    return render(request, "Docente\edicionDocente.html", {"docente": docente})

@login_required
def editarDocente(request):
    id_doc = request.POST['id_doc']
    cuil = request.POST['cuil']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    celular = request.POST['celular']
    email = request.POST['email']
    domicilio = request.POST['domicilio']
    localidad = request.POST['localidad']
    provincia = request.POST['provincia']
    genero = request.POST['genero']
    estado = request.POST['estado']
    #-
    docente = Docente.objects.get(id_doc=id_doc)
    docente.cuil = cuil
    docente.nombre = nombre
    docente.apellido = apellido
    docente.celular = celular
    docente.email = email
    docente.domicilio = domicilio
    docente.localidad = localidad
    docente.provincia = provincia
    docente.genero= genero
    docente.estado = estado
    docente.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('gestionDocente')

# ---------- ---------- ---------- ---------- ---------- Clase
@login_required
def gestionClase(request):
    clases = Clase.objects.all()
    horarios = Horario.objects.all()
    cursos = Curso.objects.all()
    DMs = doc_mat.objects.all()
    return render(request, 'Clase\gestionClase.html', {'clases': clases, 'horarios':horarios, 'cursos':cursos, 'DMs':DMs})

@login_required
def registrarClase(request):
    if request.method == 'GET':
        return render(request, 'Clase\gestionClase.html')
    else:
        id_hor = request.POST['id_hor']
        id_cur = request.POST['id_cur']
        id_dm = request.POST['id_dm']
        try:
            horario = Horario.objects.get(id_hor=id_hor)
            curso = Curso.objects.get(id_cur=id_cur)
            DM = doc_mat.objects.get(id_dm=id_dm)
            clase = Clase.objects.create(id_hor=horario, id_cur=curso, id_dm=DM)
            messages.success(request, '¡Registrado!')
        except:
            messages.error(request, "¡Ocurrió un error!")
    return redirect('gestionClase')

@login_required
def eliminarClase(request, id_cla):
    clase = Clase.objects.get(id_cla=id_cla)
    clase.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionClase')

@login_required
def edicionClase(request, id_cla):
    clase = Clase.objects.get(id_cla=id_cla)
    h = clase.id_hor
    c = clase.id_cur
    dm = clase.id_dm
    horarios = Horario.objects.all()
    cursos = Curso.objects.all()
    DMs = doc_mat.objects.all()
    return render(request, "Clase\edicionClase.html", {"clase": clase, 'h':h, 'c':c, 'dm':dm, 'horarios':horarios, 'cursos':cursos, 'DMs':DMs})

@login_required
def editarClase(request):
    id_cla = request.POST['id_cla']
    id_hor = request.POST['id_hor']
    id_cur = request.POST['id_cur']
    id_dm = request.POST['id_dm']
    # -
    horario = Horario.objects.get(id_hor=id_hor)
    curso = Curso.objects.get(id_cur=id_cur)
    DM = doc_mat.objects.get(id_dm=id_dm)
    # -
    clase = Clase.objects.get(id_cla=id_cla)
    clase.id_hor = horario
    clase.id_cur = curso
    clase.id_dm = DM
    clase.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('gestionClase')

# ---------- ---------- ---------- ---------- ---------- Horario
@login_required
def gestionHorario(request):
    """Retorna los días según el orden lógico."""
    dias_laborales_ordenados = ['L', 'M', 'X', 'J', 'V']
    # Consulta para obtener los registros ordenados por los dias laborales
    horarios_ordenados = Horario.objects.order_by(
        Case(
            *[When(dia=dia, then=posicion) for posicion, dia in enumerate(dias_laborales_ordenados)]
        )
    )
    return render(request, 'Horario\gestionHorario.html', {'horarios': horarios_ordenados})

@login_required
def registrarHorario(request):
    if request.method == 'GET':
        return render(request, 'Horario\gestionHorario.html')
    else:
        dia = request.POST['dia']
        h_i = request.POST['h_i']
        h_f = request.POST['h_f']
        try:
            horario = Horario.objects.create(dia=dia, h_i=h_i, h_f=h_f)
            messages.success(request, '¡Registrado!')
        except:
            messages.error(request, "¡Ocurrió un error!")
    return redirect('gestionHorario')

@login_required
def eliminarHorario(request, id_hor):
    horario = Horario.objects.get(id_hor=id_hor)
    horario.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionHorario')

@login_required
def edicionHorario(request, id_hor):
    horario = Horario.objects.get(id_hor=id_hor)
    return render(request, "Horario\edicionHorario.html", {"horario": horario})

@login_required
def editarHorario(request):
    id_hor = request.POST['id_hor']
    dia = request.POST['dia']
    h_i = request.POST['h_i']
    h_f = request.POST['h_f']
    # -
    horario = Horario.objects.get(id_hor=id_hor)
    horario.dia = dia
    horario.h_i = h_i
    horario.h_f = h_f
    horario.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('gestionHorario')

# ---------- ---------- ---------- ---------- ---------- Asistencia
@login_required
def gestionAsistencia(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'Asistencia\gestionAsistencia.html', {'asistencias': asistencias})

@login_required
def registrarAsistencia(request):
    if request.method == 'GET':
        return render(request, 'Asistencia\gestionAsistencia.html')
    else:
        fecha = request.POST['fecha']
        asistencia = request.POST['asistencia']
        articulo = request.POST['articulo']
        id_cla = request.POST['id_cla']
        try:
            Asistencia = Asistencia.objects.create(fecha=fecha, asistencia=asistencia, articulo=articulo, id_cla=id_cla)
            messages.success(request, '¡Registrado!')
        except:
            messages.error(request, "¡Ocurrió un error!")
    return redirect('gestionAsistencia')

@login_required
def eliminarAsistencia(request, id_asi):
    asistencia = Asistencia.objects.get(id_asi=id_asi)
    asistencia.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionAsistencia')

@login_required
def edicionAsistencia(request, id_asi):
    asistencia = Asistencia.objects.get(id_asi=id_asi)
    return render(request, "Asistencia\edicionAsistencia.html", {"asistencia": asistencia})

@login_required
def editarAsistencia(request):
    id_asi = request.POST['id_asi']
    fecha = request.POST['fecha']
    asistencia = request.POST['asistencia']
    articulo = request.POST['articulo']
    id_cla = request.POST['id_cla']
    # -    
    asistencia = Asistencia.objects.get(id_asi=id_asi)
    asistencia.fecha = fecha
    asistencia.asistencia = asistencia
    asistencia.articulo = articulo
    asistencia.id_cla = id_cla
    asistencia.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('gestionAsistencia')

# ---------- ---------- ---------- ---------- ---------- Materia
@login_required
def gestionMateria(request):
    materias = Materia.objects.all().order_by('nombre')
    return render(request, 'Materia\gestionMateria.html', {'materias': materias})

@login_required
def registrarMateria(request):
    if request.method == 'GET':
        return render(request, 'Materia\gestionMateria.html')
    else:
        nombre = request.POST['nombre']
        try:
            materia = Materia.objects.create(nombre=nombre)
            messages.success(request, '¡Registrado!')
        except:
            messages.error(request, "¡Ocurrió un error!")
    return redirect('gestionMateria')

@login_required
def eliminarMateria(request, id_mat):
    materia = Materia.objects.get(id_mat=id_mat)
    materia.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionMateria')

@login_required
def edicionMateria(request, id_mat):
    materia = Materia.objects.get(id_mat=id_mat)
    return render(request, "Materia\edicionMateria.html", {"materia": materia})

@login_required
def editarMateria(request):
    id_mat = request.POST['id_mat']
    nombre = request.POST['nombre']
    # -
    materia = Materia.objects.get(id_mat=id_mat)
    materia.nombre = nombre
    materia.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('gestionMateria')

# ---------- ---------- ---------- ---------- ---------- doc_mat
@login_required
def gestionDM(request):
    DMs = doc_mat.objects.all()
    docentes = Docente.objects.values('id_doc', 'nombre', 'apellido', 'cuil')
    materias = Materia.objects.all()
    return render(request, 'DM\gestionDM.html', {'DMs': DMs, 'docentes':docentes, 'materias':materias})

@login_required
def registrarDM(request):
    if request.method == 'GET':
        return render(request, 'DM\gestionDM.html')
    else:
        id_doc = int(request.POST['id_doc'])
        id_mat = int(request.POST['id_mat'])
        try:
            docente = Docente.objects.get(id_doc=id_doc)
            materia = Materia.objects.get(id_mat=id_mat)
            DM = doc_mat.objects.create(id_doc=docente, id_mat=materia)
            messages.success(request, '¡Registrado!')
        except Exception as e:
            messages.error(request, f"¡Ocurrió un error! {e}")
    return redirect('gestionDM')

@login_required
def eliminarDM(request, id_dm):
    DMs = doc_mat.objects.get(id_dm=id_dm)
    DMs.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionDM')

@login_required
def edicionDM(request, id_dm):
    DM = doc_mat.objects.get(id_dm=id_dm)
    d = DM.id_doc
    m = DM.id_mat
    docentes = Docente.objects.values('id_doc', 'nombre', 'apellido', 'cuil')
    materias = Materia.objects.all()
    return render(request, 'DM\edicionDM.html', {'DM': DM, 'docentes':docentes, 'materias':materias, 'd':d, 'm':m})

@login_required
def editarDM(request):
    id_dm = request.POST['id_dm']
    id_doc = request.POST['id_doc']
    id_mat = request.POST['id_mat']
    #
    docente = Docente.objects.get(id_doc=id_doc)
    materia = Materia.objects.get(id_mat=id_mat)
    #
    DM = doc_mat.objects.get(id_dm=id_dm)
    DM.id_doc = docente
    DM.id_mat = materia
    DM.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('gestionDM')
