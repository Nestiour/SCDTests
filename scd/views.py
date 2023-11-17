from django.shortcuts import render, redirect
from .models import *
from .utils import *
from django.contrib import messages
from datetime import datetime
import pytz
# DB
from django.db.utils import IntegrityError
from django.db.models import Case, When
# Login
from django.contrib.auth.decorators import login_required
# Create your views here.
from accounts.views import user_has_required_group, access_denied

from django.contrib.auth.decorators import user_passes_test


# ---------- ---------- ---------- ---------- ---------- Inicio
def inicio(request):
    bienvenida = saludo()
    # Verificar si el usuario está logueado y es un docente
    if request.user.is_authenticated and request.user.groups.filter(name='Docente').exists():
        return redirect('consultarAsistencia')
    else:
        clases = Clase.objects.all()
        return render(request, 'inicio.html', {'saludo': bienvenida, 'clases':clases})

def consultarAsistencia(request):
    if request.method == "GET":
        messages.warning(request, ' ')
        return render(request, 'Asistencia\\consultarAsistencia.html')
    else:
        cuil = request.POST['cuil']
        asistencia = Asistencia.objects.filter(id_cla__id_dm__id_doc__cuil=cuil).exists()

        if asistencia:
            asistencias = Asistencia.objects.filter(id_cla__id_dm__id_doc__cuil=cuil)
            messages.success(request, ' ')
            return render(request, 'Asistencia\\consultarAsistencia.html', {'asistencias':asistencias})
        else:
            messages.error(request, 'No se encontró el CUIL.')
            return render(request, 'Asistencia\\consultarAsistencia.html')

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
@user_passes_test(user_has_required_group, login_url='access_denied')
def gestionCurso(request):
    cursos = Curso.objects.all().order_by('anio', 'division', 'turno')
    return render(request, 'Curso\\gestionCurso.html', {'cursos': cursos})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def registrarCurso(request):
    if request.method == 'GET':
        return render(request, 'Curso\\gestionCurso.html')
    else:
        anio = request.POST['anio']
        division = request.POST['division']
        especialidad = request.POST['especialidad']
        turno = request.POST['turno']
        # -
        # Verificar si ya existe un curso con los mismos datos (variable es True o False)
        curso_existente = Curso.objects.filter(anio=anio, division=division, especialidad=especialidad, turno=turno).exists()

        if not curso_existente:
            try:
                # Si no existe, crea y guarda el objeto Curso en la DB
                curso = Curso.objects.create(anio=anio, division=division, especialidad=especialidad, turno=turno)
                messages.success(request, '¡Registrado!')
            except Exception as e:
                messages.error(request, f"¡Ocurrió un error! {e}")
        else:
            messages.warning(request, '¡Ya existe el curso!')
        # -
    return redirect('gestionCurso')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def eliminarCurso(request, id_cur):
    curso = Curso.objects.get(id_cur=id_cur)
    curso.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionCurso')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def edicionCurso(request, id_cur):
    curso = Curso.objects.get(id_cur=id_cur)
    return render(request, "Curso\\edicionCurso.html", {"curso": curso})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
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
@user_passes_test(user_has_required_group, login_url='access_denied')
def gestionDocente(request):
    docentes = Docente.objects.all().order_by('apellido')
    return render(request, 'Docente\\gestionDocente.html', {'docentes': docentes})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def registrarDocente(request):
    if request.method == 'GET':
        return render(request, 'Docente\\gestionDocente.html')
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
@user_passes_test(user_has_required_group, login_url='access_denied')
def eliminarDocente(request, id_doc):
    docente = Docente.objects.get(id_doc=id_doc)
    docente.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionDocente')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def edicionDocente(request, id_doc):
    docente = Docente.objects.get(id_doc=id_doc)
    return render(request, "Docente\\edicionDocente.html", {"docente": docente})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
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
@user_passes_test(user_has_required_group, login_url='access_denied')
def gestionClase(request):
    clases = Clase.objects.all()
    horarios = Horario.objects.all()
    cursos = Curso.objects.all()
    DMs = doc_mat.objects.all()
    return render(request, 'Clase\\gestionClase.html', {'clases': clases, 'horarios':horarios, 'cursos':cursos, 'DMs':DMs})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def registrarClase(request):
    if request.method == 'GET':
        return render(request, 'Clase\\gestionClase.html')
    else:
        id_hor = request.POST['id_hor']
        id_cur = request.POST['id_cur']
        id_dm = request.POST['id_dm']
        # -
        horario = Horario.objects.get(id_hor=id_hor)
        curso = Curso.objects.get(id_cur=id_cur)
        clase_existente = Clase.objects.filter(id_hor=horario, id_cur=curso).exists()
        if not clase_existente:
            try:
                # Si no existe, crea y guarda el objeto en la DB
                DM = doc_mat.objects.get(id_dm=id_dm)
                clase = Clase.objects.create(id_hor=horario, id_cur=curso, id_dm=DM)
                messages.success(request, '¡Registrado!')
            except Exception as e:
                messages.error(request, f"¡Ocurrió un error! {e}")
        else:
            messages.warning(request, '¡Ya existe la Clase!')
        # -
        
    return redirect('gestionClase')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def eliminarClase(request, id_cla):
    clase = Clase.objects.get(id_cla=id_cla)
    clase.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionClase')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def edicionClase(request, id_cla):
    clase = Clase.objects.get(id_cla=id_cla)
    h = clase.id_hor
    c = clase.id_cur
    dm = clase.id_dm
    horarios = Horario.objects.all()
    cursos = Curso.objects.all()
    DMs = doc_mat.objects.all()
    return render(request, "Clase\\edicionClase.html", {"clase": clase, 'h':h, 'c':c, 'dm':dm, 'horarios':horarios, 'cursos':cursos, 'DMs':DMs})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
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
@user_passes_test(user_has_required_group, login_url='access_denied')
def gestionHorario(request):
    """Retorna los días según el orden lógico."""
    dias_laborales_ordenados = ['L', 'M', 'X', 'J', 'V']
    # Consulta para obtener los registros ordenados por los dias laborales
    horarios_ordenados = Horario.objects.order_by(
        Case(
            *[When(dia=dia, then=posicion) for posicion, dia in enumerate(dias_laborales_ordenados)]
        ), 'h_i', 'h_f'
    )
    return render(request, 'Horario\\gestionHorario.html', {'horarios': horarios_ordenados})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def registrarHorario(request):
    if request.method == 'GET':
        return render(request, 'Horario\\gestionHorario.html')
    else:
        dia = request.POST['dia']
        h_i = request.POST['h_i']
        h_f = request.POST['h_f']
        # -
        horario_existente = Horario.objects.filter(dia=dia, h_i=h_i, h_f=h_f).exists()

        if not horario_existente:
            try:
                # Si no existe, crea y guarda el objeto en la DB
                horario = Horario.objects.create(dia=dia, h_i=h_i, h_f=h_f)
                messages.success(request, '¡Registrado!')
            except Exception as e:
                messages.error(request, f"¡Ocurrió un error! {e}")
        else:
            messages.warning(request, '¡Ya existe el Horario!')
        # -

    return redirect('gestionHorario')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def eliminarHorario(request, id_hor):
    horario = Horario.objects.get(id_hor=id_hor)
    horario.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionHorario')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def edicionHorario(request, id_hor):
    horario = Horario.objects.get(id_hor=id_hor)
    return render(request, "Horario\\edicionHorario.html", {"horario": horario})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
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
@user_passes_test(user_has_required_group, login_url='access_denied')
def gestionAsistencia(request):
    fecha_actual = datetime.now()
    # -
    dias_abreviados = {
        'Monday': 'L',
        'Tuesday': 'M',
        'Wednesday': 'X',
        'Thursday': 'J',
        'Friday': 'V',
    }
    nombre_dia = fecha_actual.strftime('%A')  # Devuelve "Monday", ..., "Friday", etc
    dia = dias_abreviados.get(nombre_dia, 'SD')
    if dia != 'SD':
        clases = Clase.objects.filter(id_hor__dia=dia)
    else:
        clases = Clase.objects.all()
    # -
    docentes = Docente.objects.values('id_doc', 'nombre', 'apellido', 'cuil').order_by('apellido').filter(estado='A')
    return render(request, 'Asistencia\\gestionAsistencia.html', {'docentes':docentes, 'clases':clases})

@login_required
def verAsistencia(request):
    """Devuelve las Asistencias que se tomaron en el día."""
    # modificar para mostrar solo las asistencias que se tomaron en el dia (ahora muestra todas)
    asistencias = Asistencia.objects.all()
    return render(request, 'Asistencia\\verAsistencia.html', {'asistencias':asistencias})

def gestionDA(request, id_doc):
    """Devuelve solamente las asistencias de determinado Docente mediante un 'id_doc'."""
    if request.method == 'GET':
        asistencias = Asistencia.objects.filter(id_cla__id_dm__id_doc__id_doc=id_doc).order_by('-id_asi')
        return render(request, "Asistencia\\gestionDA.html", {"asistencias": asistencias})
    else:
        orden = request.POST['orden']
        if orden == '1':
            asistencias = Asistencia.objects.filter(id_cla__id_dm__id_doc__id_doc=id_doc).order_by('-id_asi')
            return render(request, "Asistencia\\gestionDA.html", {"asistencias": asistencias})
        else:
            asistencias = Asistencia.objects.filter(id_cla__id_dm__id_doc__id_doc=id_doc).order_by('-fecha')
            return render(request, "Asistencia\\gestionDA.html", {"asistencias": asistencias})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def registrarAsistencia(request):
    if request.method == 'GET':
        return render(request, 'Asistencia\\gestionAsistencia.html')
    else:
        try:
            #zona_hor_bsas = pytz.timezone('America/Argentina/Buenos_Aires')
            #hora_fecha = datetime.now(zona_hor_bsas)
            # La zona horaria de la DB está mal, se deben restar 3 horas
            #fecha = hora_fecha - timedelta(hours=3)
            articulo = request.POST['articulo']
            responsable = request.user.username
            asistencia = request.POST['asistencia']
            if asistencia != 'A':
                articulo = '-'
            # Verifica si 'id_cla' está presente en request.POST (cuando asistencia es != 'A')
            if 'id_cla' in request.POST:
                id_cla = request.POST['id_cla']
                clase = Clase.objects.get(id_cla=id_cla)
                asistencia = Asistencia.objects.create(asistencia=asistencia, articulo=articulo, id_cla=clase, responsable=responsable) #, fecha=fecha,
            else:
                asistencia = Asistencia.objects.create(asistencia=asistencia, articulo=articulo, responsable=responsable)
            messages.success(request, '¡Registrado!')
        except Exception as e:
            messages.error(request, f"¡Ocurrió un error! {e}")
    return redirect('gestionAsistencia')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def eliminarAsistencia(request, id_asi):
    asistencia = Asistencia.objects.get(id_asi=id_asi)
    asistencia.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionAsistencia')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def edicionAsistencia(request, id_asi):
    asistencia = Asistencia.objects.get(id_asi=id_asi)
    return render(request, "Asistencia\\edicionAsistencia.html", {"asistencia": asistencia})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def editarAsistencia(request):
    id_asi = request.POST['id_asi']
    # -
    zona_hor_bsas = pytz.timezone('America/Argentina/Buenos_Aires')
    hora_fecha = datetime.now(zona_hor_bsas)
    fecha = hora_fecha
    #asistencia = request.POST['asistencia']
    articulo = request.POST['articulo']
    #id_cla = request.POST['id_cla']
    # -    
    asistencia = Asistencia.objects.get(id_asi=id_asi)
    asistencia.fecha = fecha
    #asistencia.asistencia = asistencia
    asistencia.articulo = articulo
    asistencia.responsable = request.user.username
    #asistencia.id_cla = id_cla
    asistencia.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('verAsistencia')

# ---------- ---------- ---------- ---------- ---------- Materia
@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def gestionMateria(request):
    materias = Materia.objects.all().order_by('nombre')
    return render(request, 'Materia\\gestionMateria.html', {'materias': materias})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def registrarMateria(request):
    if request.method == 'GET':
        return render(request, 'Materia\\gestionMateria.html')
    else:
        nombre = request.POST['nombre']
        # -
        materia_existente = Materia.objects.filter(nombre=nombre).exists()
        if not materia_existente:
            try:
                # Si no existe, crea y guarda el objeto en la DB
                materia = Materia.objects.create(nombre=nombre)
                messages.success(request, '¡Registrado!')
            except Exception as e:
                messages.error(request, f"¡Ocurrió un error! {e}")
        else:
            messages.warning(request, '¡Ya existe la Materia!')
        # -
    return redirect('gestionMateria')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def eliminarMateria(request, id_mat):
    materia = Materia.objects.get(id_mat=id_mat)
    materia.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionMateria')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def edicionMateria(request, id_mat):
    materia = Materia.objects.get(id_mat=id_mat)
    return render(request, "Materia\\edicionMateria.html", {"materia": materia})

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
    docentes = Docente.objects.values('id_doc', 'nombre', 'apellido', 'cuil').filter(estado='A')
    materias = Materia.objects.all()
    return render(request, 'DM\\gestionDM.html', {'DMs': DMs, 'docentes':docentes, 'materias':materias})

@login_required
def registrarDM(request):
    if request.method == 'GET':
        return render(request, 'DM\\gestionDM.html')
    else:
        id_doc = int(request.POST['id_doc'])
        id_mat = int(request.POST['id_mat'])
        # -
        docente = Docente.objects.get(id_doc=id_doc)
        materia = Materia.objects.get(id_mat=id_mat)
        DM_existente = doc_mat.objects.filter(id_doc=docente, id_mat=materia).exists()

        if not DM_existente:
            try:
                # Si no existe, crea y guarda el objeto en la DB
                DM = doc_mat.objects.create(id_doc=docente, id_mat=materia)
                messages.success(request, '¡Registrado!')
            except Exception as e:
                messages.error(request, f"¡Ocurrió un error! {e}")
        else:
            messages.warning(request, '¡Ya existe la Asociación!')
        # -
    return redirect('gestionDM')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def eliminarDM(request, id_dm):
    DMs = doc_mat.objects.get(id_dm=id_dm)
    DMs.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('gestionDM')

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
def edicionDM(request, id_dm):
    DM = doc_mat.objects.get(id_dm=id_dm)
    d = DM.id_doc
    m = DM.id_mat
    docentes = Docente.objects.values('id_doc', 'nombre', 'apellido', 'cuil')
    materias = Materia.objects.all()
    return render(request, 'DM\\edicionDM.html', {'DM': DM, 'docentes':docentes, 'materias':materias, 'd':d, 'm':m})

@login_required
@user_passes_test(user_has_required_group, login_url='access_denied')
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