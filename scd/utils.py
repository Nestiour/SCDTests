# Contiene funciones y utilidades útiles para la aplicación.

import datetime
import feedparser
import random


# --------------------------------------------------------------------- Saludo
def saludo():
    """
    Esta funcion obtiene los digitos correspondientes a la hora del sistema y retorna un saludo (string)
    correspondiente a la hora.
    """
    saludo = ""
    hora_actual = datetime.datetime.now().time()
    hora_str = hora_actual.strftime('%H')
    hora_digitos = int(hora_str)
    if 6 <= hora_digitos < 12:
        saludo = "Buenos días"
    elif 12 <= hora_digitos < 20:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    return saludo

# --------------------------------------------------------------------- NOTICIAS
def obtener_noticias_rss():
    """
    Obtiene las noticias en formato XML a partir de una URL.
    Retorna todos los elementos de la noticia: titulo, enlace, descripcion, etc.
    """
    # Link del portal de noticias La Nacion
    url_rss = 'https://www.lanacion.com.ar/arc/outboundfeeds/rss/?outputType=xml'
    # Otra opcion, Clarin: https://www.clarin.com/rss/lo-ultimo/ (https://www.clarin.com/rss.html)
    noticias = []
    feed = feedparser.parse(url_rss)
    # Define el límite de pares clave-valor
    limite = 5 #30
    # Controla el retorno de links de imagenes (para fines de aligerar carga en test)
    devolver_img = False
    # Verificar si el diccionario tiene más elementos que el límite
    if len(feed.entries) > limite:
    # Si hay más elementos que el límite, elimina los elementos adicionales
        feed.entries = feed.entries[:limite]
    
    for entry in feed.entries:
        titulo = entry.title
        enlace = entry.link
        # -
        list_descripcion = entry.get('content', entry.get('summary', ''))
        dicc_descripcion = list_descripcion[0]
        descripcion = dicc_descripcion.get("value")
        # -
        fecha_publicacion = entry.get('published', '')
        # La etiqueta 'published' corresponde a pubDate en la fuente RSS.
        
        # Para acceder a la imagen, podemos buscar la etiqueta 'media:content'
        # que contenga el atributo 'medium' con valor 'image'.
        imagen = None
        descripcion_imagen = None
        media_content = entry.get('media_content', [])
        for media in media_content:
            if devolver_img and media.get('type', '').startswith('image/'):
                imagen = media.get('url', '')
                descripcion_imagen = media.get('media:description', '')
                break  # Rompemos el ciclo si encontramos la primera imagen.
        noticias.append({
            'titulo': titulo,
            'enlace': enlace,
            'descripcion': descripcion,
            'fecha_publicacion': fecha_publicacion,
            'imagen': imagen,
            'descripcion_imagen': descripcion_imagen
        })
    return noticias

# --------------------------------------------------------------------- HOROSCOPO
frases_amor = [
    "Expresa tus sentimientos abiertamente hoy.",
    "Comparte momentos especiales con tu ser amado.",
    "Fortalece los lazos con tus seres queridos.",
    "Demuestra tu cariño con pequeños gestos de amor.",
    "Escucha con atención a tu pareja para fortalecer la comunicación.",
    "Atrévete a ser vulnerable y mostrar tu verdadero yo.",
    "Busca la armonía y la comprensión en tus relaciones.",
    "Disfruta del romance y la pasión en tu vida amorosa.",
    "Ama con intensidad y entrega en cada momento.",
    "Sé el apoyo incondicional de tu pareja en momentos difíciles.",
    "Comparte tus sueños y metas con tu ser amado.",
    "Sorprende a tu pareja con detalles significativos.",
    "Cultiva la confianza mutua en la relación.",
    "Valora la individualidad y la autonomía de tu pareja.",
    "Demuestra gratitud por el amor que recibes.",
    "Acepta las diferencias y aprende de ellas en pareja.",
    "Comparte tus emociones y vulnerabilidades con sinceridad.",
    "Fortalece la complicidad y el compañerismo en la relación.",
    "Brinda apoyo emocional en los momentos de alegría y tristeza.",
    "Busca momentos de conexión íntima y cercana con tu pareja.",
    "Aprovecha cada oportunidad para crear recuerdos especiales.",
    "Escucha con empatía y sin juzgar a tu ser amado.",
    "Dale espacio y tiempo a tu pareja para crecer individualmente.",
    "Comparte tus intereses y hobbies para fortalecer la unión.",
    "Sé paciente y comprensivo/a en las discusiones y desacuerdos.",
    "Celebra las virtudes y logros de tu ser amado.",
    "Reaviva la pasión y el romance en la relación con sorpresas.",
    "Muestra aprecio y gratitud por los pequeños gestos de amor.",
    "Acepta y aprende de los errores cometidos en la relación.",
    "Exprésate con palabras amorosas y afectuosas hacia tu pareja."
]

frases_trabajo = [
    "Enfócate en tus metas profesionales y persíguelas con determinación.",
    "Aprovecha las oportunidades laborales que se presenten en tu camino.",
    "Confía en tus habilidades y capacidades para superar los desafíos laborales.",
    "Mantén una actitud positiva y proactiva en tu entorno laboral.",
    "Aprende de tus errores y utilízalos como oportunidades para crecer profesionalmente.",
    "Busca el equilibrio entre el trabajo y el descanso para evitar el agotamiento.",
    "Demuestra tu compromiso y responsabilidad en tus tareas laborales.",
    "Atrévete a tomar decisiones audaces que impulsen tu carrera hacia adelante.",
    "Fortalece tus habilidades de comunicación para mejorar la colaboración con colegas.",
    "Sé flexible y adapta tu enfoque en función de las demandas laborales.",
    "Mantén una visión clara de tus objetivos y trabaja hacia ellos de manera constante.",
    "Aprende de tus colegas y mentores para expandir tus conocimientos y habilidades.",
    "Acepta los cambios como oportunidades para crecer y evolucionar en tu carrera.",
    "Reconoce tus logros y celebra tus éxitos en el ámbito laboral.",
    "Establece límites saludables para mantener una buena conciliación entre trabajo y vida personal.",
    "Afronta los retos laborales con valentía y confianza en tus capacidades.",
    "Colabora con tus compañeros de equipo para alcanzar objetivos comunes.",
    "Sé proactivo/a en buscar nuevas oportunidades de desarrollo profesional.",
    "Demuestra iniciativa y liderazgo en proyectos relevantes para tu carrera.",
    "Cultiva una red de contactos profesionales para ampliar tus horizontes laborales.",
    "Aprovecha el feedback constructivo para mejorar y crecer en tu carrera.",
    "Encuentra un equilibrio entre tu pasión y tus habilidades al elegir un camino profesional.",
    "Desarrolla tus habilidades de resolución de problemas para enfrentar desafíos laborales.",
    "Muestra gratitud hacia tus colegas y superiores por su apoyo y colaboración.",
    "Aprende de los fracasos y úsalos como trampolín para el éxito futuro.",
    "Mantén una mentalidad abierta y dispuesta a aprender de nuevas experiencias laborales.",
    "Haz un esfuerzo por mantener una atmósfera de trabajo positiva y motivadora.",
    "Reconoce y valora el esfuerzo y dedicación de tus compañeros de trabajo.",
    "Establece metas claras y realistas para mantener el enfoque en tu carrera.",
    "Busca oportunidades para destacar tus habilidades y aportar valor en tu lugar de trabajo."
]

frases_dinero = [
    "Haz un presupuesto y mantén un seguimiento de tus gastos.",
    "Invierte en tu educación financiera para tomar decisiones informadas.",
    "Busca formas de aumentar tus ingresos a través de fuentes adicionales.",
    "Ahorra una parte de tus ingresos regularmente para crear un fondo de emergencia.",
    "Evita compras impulsivas y reflexiona antes de realizar gastos importantes.",
    "Compara precios y busca descuentos antes de realizar compras.",
    "Considera la posibilidad de invertir en activos que generen ingresos pasivos.",
    "Paga tus deudas a tiempo para evitar cargos adicionales.",
    "Establece metas financieras a corto y largo plazo para mantenerte enfocado/a.",
    "Evalúa tus gastos y elimina aquellos que no sean realmente necesarios.",
    "Sé consciente de tus hábitos de consumo y evita caer en el consumismo excesivo.",
    "Mantén tus registros financieros organizados y actualizados.",
    "Busca asesoramiento financiero profesional para tomar decisiones importantes.",
    "Considera la posibilidad de diversificar tus inversiones para reducir riesgos.",
    "Aprende a diferenciar entre necesidades y deseos al manejar tu dinero.",
    "Sé paciente y disciplinado/a en tus estrategias de ahorro e inversión.",
    "Revisa tus estados de cuenta y detecta posibles errores o cargos incorrectos.",
    "Mantén una mentalidad positiva y enfocada en el crecimiento financiero.",
    "Considera la posibilidad de establecer un plan de jubilación temprano.",
    "Busca oportunidades para desarrollar habilidades que aumenten tu valor en el mercado laboral.",
    "Mantente informado/a sobre tendencias económicas y financieras.",
    "Evita adquirir deudas innecesarias y aprende a vivir dentro de tus posibilidades.",
    "Asegúrate de tener un fondo de emergencia para hacer frente a imprevistos.",
    "No pongas todos tus huevos en la misma canasta al invertir.",
    "Controla los gastos hormiga, ya que pueden sumar grandes cantidades a largo plazo.",
    "Considera la posibilidad de ahorrar para metas específicas, como viajes o compras importantes.",
    "No te compares financieramente con los demás; cada situación es única.",
    'Aprende a decir "no" a gastos innecesarios o presiones sociales.',
    "Busca oportunidades de mejora salarial o crecimiento profesional para aumentar tus ingresos.",
    "Evalúa tus inversiones periódicamente y ajusta tu estrategia según las condiciones del mercado."
]

frases_salud = [
    "Prioriza tu descanso y asegúrate de dormir lo suficiente cada noche.",
    "Realiza ejercicio físico regularmente para mantener tu cuerpo en movimiento.",
    "Cuida tu alimentación y asegúrate de incluir una dieta equilibrada y nutritiva.",
    "Practica técnicas de relajación, como la meditación o el yoga, para reducir el estrés.",
    "Escucha a tu cuerpo y descansa cuando sientas fatiga o agotamiento.",
    "Mantén una hidratación adecuada bebiendo suficiente agua durante el día.",
    "Busca actividades que te brinden alegría y te ayuden a liberar tensiones.",
    "Haz pausas regulares si pasas mucho tiempo frente a una pantalla o trabajando.",
    "Mantén una rutina de cuidado personal que incluya tiempo para ti mismo/a.",
    'Aprende a decir "no" cuando sientas que estás sobrecargado/a de responsabilidades.',
    "Evita el consumo excesivo de alcohol, tabaco o sustancias nocivas.",
    "Realiza exámenes médicos periódicos para monitorear tu salud.",
    "Busca apoyo emocional en amigos, familiares o profesionales si lo necesitas.",
    "Encuentra formas saludables de manejar el estrés, como practicar deportes o hobbies.",
    "Haz actividades al aire libre para conectarte con la naturaleza y revitalizarte.",
    "Practica la gratitud y enfócate en las cosas positivas de tu vida.",
    "Acepta y perdona tus errores, y utiliza cada experiencia como una oportunidad de crecimiento.",
    "Evita el sedentarismo y busca oportunidades para moverte a lo largo del día.",
    "Mantén tus relaciones sociales y busca conexiones significativas con otras personas.",
    "Establece límites en tu vida para evitar el agotamiento y el estrés innecesario.",
    "Aprende a manejar las emociones y a expresarlas de manera saludable.",
    "Practica el autocuidado y dedica tiempo a actividades que te hagan sentir bien.",
    "Escucha a tu intuición y respeta tus necesidades físicas y emocionales.",
    "Encuentra el equilibrio entre el trabajo, la vida personal y el tiempo para ti mismo/a.",
    "Cultiva una mentalidad positiva y enfocada en el bienestar.",
    "Mantén una postura adecuada y cuida de tu columna vertebral y tu ergonomía.",
    "Disfruta del sol de manera responsable y protege tu piel.",
    "Busca oportunidades para aprender y crecer en temas relacionados con la salud.",
    "Practica la empatía y el apoyo hacia los demás, lo que también fortalece tu bienestar.",
    "Celebra tus logros y avances en tu camino hacia una vida más saludable.",
    "Recuerda que el autocuidado es una prioridad, y es necesario cuidar de ti mismo/a para poder cuidar a los demás."
]

mensajes = [
    "Cree en ti mismo/a, porque eres capaz de lograr cosas increíbles.",
    "El camino hacia el éxito comienza con un solo paso, así que da el primer paso con valentía.",
    "Las dificultades pueden ser oportunidades disfrazadas, así que afronta los desafíos con determinación.",
    "Tus sueños no tienen fecha de caducidad, sigue persiguiéndolos sin importar el tiempo que lleve.",
    "Eres más fuerte de lo que piensas, y puedes superar cualquier obstáculo que se presente.",
    "El fracaso es una oportunidad para aprender y crecer, así que no temas arriesgarte y seguir adelante.",
    "El éxito no es el resultado de la suerte, sino de la perseverancia y el esfuerzo constante.",
    "Nunca subestimes el poder de una pequeña acción; cada paso cuenta en tu camino hacia tus metas.",
    "Tienes el poder de cambiar tu vida y de crear la realidad que deseas, confía en ti mismo/a.",
    "Las mejores cosas de la vida a menudo se encuentran fuera de tu zona de confort, así que atrévete a explorar.",
    "No dejes que el miedo te limite; permítete soñar en grande y alcanzar nuevas alturas.",
    "Cada día es una nueva oportunidad para comenzar de nuevo y crear la vida que deseas.",
    "La vida es un viaje con altibajos; disfruta los buenos momentos y aprende de los difíciles.",
    "El tiempo y el esfuerzo que inviertas en ti mismo/a valdrán la pena; eres tu mejor inversión.",
    "La autenticidad es la clave para atraer a las personas y oportunidades adecuadas en tu vida.",
    "Tu actitud determina tu altitud, así que mantén una mentalidad positiva y enfocada en el crecimiento.",
    "El poder de la gratitud puede transformar tu vida; agradece lo que tienes y atraerás más razones para hacerlo.",
    "Cada día es una página en blanco; escribe una historia que te llene de orgullo y satisfacción.",
    "Aprecia los pequeños momentos de felicidad y encuentra la belleza en las cosas simples de la vida.",
    "No te compares con los demás; cada persona tiene su propio camino y ritmo.",
    "La vida está llena de posibilidades infinitas; mantén tu mente abierta a nuevas oportunidades.",
    "La paciencia es una virtud; confía en que todo se desarrollará en el momento adecuado.",
    "El éxito se encuentra en el proceso tanto como en el resultado; disfruta del viaje.",
    "No temas pedir ayuda o apoyo cuando lo necesites; somos más fuertes cuando nos apoyamos mutuamente.",
    "El pasado ya no puede ser cambiado, pero el futuro está en tus manos; crea una nueva realidad.",
    "El amor y la bondad que das al mundo regresan a ti multiplicados; cultiva relaciones positivas.",
    "La vida está llena de sorpresas y oportunidades; mantente abierto/a a las maravillas que te esperan.",
    "Tus pensamientos y palabras tienen poder creativo; elige enfocarte en lo positivo y construir tu realidad.",
    "Cada desafío te da la oportunidad de fortalecerte y crecer; abraza las lecciones que te ofrece.",
    "Tu luz brilla más intensamente cuando eres auténtico/a y te permites ser quien realmente eres.",
    "Eres el autor/a de tu propia historia; escribe una trama llena de pasión, amor y realización."
]

def obtener_horoscopos():
    signos = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
    fechas = ["23/12 al 20/1", "21/1 al 19/2", "20/2 al 20/3", "21/3 al 20/4", "21/4 al 21/5", "22/5 al 21/6", "22/6 al 23/7", "24/7 al 23/8", "24/8 al 23/9", "24/9 al 23/10", "24/10 al 22/11", "23/11 al 22/12"]
    astros = ["Sol", "Luna", "Mercurio", "Venus", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno", "Plutón", "Plutón", "Jupiter"]
    elementos = ["Tierra", "Aire", "Agua", "Fuego", "Tierra", "Aire", "Agua", "Fuego", "Tierra", "Aire", "Agua", "Fuego"]
    piedras = ["Ónix", "Amatista", "Aquamarina", "Diamante", "Esmeralda", "Ágata", "Perla", "Rubí", "Zafiro", "Aguamarina", "Topacio", "Turquesa"]

    global frases_amor
    global frases_trabajo
    global frases_dinero
    global frases_salud
    global mensajes

    horoscopos = []

    def elemento_random(arreglo):
        indice_aleatorio = random.randint(0, len(arreglo) - 1)
        elemento = arreglo[indice_aleatorio]
        return elemento

    for i in range(len(signos)-1):
        signo = signos[i]
        fecha = fechas[i]
        piedra = piedras[i]
        elemento = elementos[i]
        astro = astros[i]
        frase_amor = elemento_random(frases_amor)
        frase_trabajo = elemento_random(frases_trabajo)
        frase_dinero = elemento_random(frases_dinero)
        frase_salud = elemento_random(frases_salud)
        numero = random.randint(0, 100)
        mensaje = elemento_random(mensajes)

        horoscopos.append({
            'signo': signo,
            'fecha': fecha,
            'piedra': piedra,
            'elemento': elemento,
            'astro': astro,
            'frase_amor': frase_amor,
            'frase_trabajo': frase_trabajo,
            'frase_dinero': frase_dinero,
            'frase_salud': frase_salud,
            'numero': numero,
            'mensaje': mensaje
        })

    return horoscopos