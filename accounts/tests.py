from django.test import TestCase

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sistema_control_docente import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
# Create your tests here.

def send_email():
    # Establecemos conexion con el servidor smtp de gmail
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado..')

        email_to = 'lucasvillavicencio15@gmail.com'
        # Construimos el mensaje
        mensaje = MIMEMultipart("""Esto es un mensaje de ejemplo""")
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo nuevo"

        content = (render_to_string('accounts/recuperacion.html', {'user': User.objects.get(pk=1)}))
        mensaje.attach(MIMEText(content, 'html'))

        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                            email_to,
                            mensaje.as_string())
    
        print('Correo enviado correctamente')

    except Exception as e:
        print(e)

send_email()