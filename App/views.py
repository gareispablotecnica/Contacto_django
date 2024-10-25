from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
#-->Librerias para plantillas GMAIL
from django.template.loader import render_to_string
#-->Libreria para GMAIL
from django.core.mail import EmailMessage

# Create your views here.
def Home(request):
    return render(request,"index.html")

def Gmail(request):
    if request.method=='POST':
        nombre=request.POST['nombre']
        email=request.POST['email']
        asunto=request.POST['asunto']
        mensaje=request.POST['mensaje']
        #-->Para editar el Email para enviar
        plantilla= render_to_string('email.html',{
            nombre:'nombre',
            email:'email',
            asunto:'asunto',
            mensaje:'mensaje'
        })

        #--->Donde se configura los datos a enviar
        enviar_email=EmailMessage(
            asunto,
            plantilla,
            settings.EMAIL_HOST_USER,
            #-->Email de la Empresa
            ['gareispablo7mo@gmail.com']
        )

        enviar_email.content_subtype='html'
        enviar_email.fail_silenty=True
        enviar_email.send()

        messages.success(request,'Datos Enviados Correctamente')
    return redirect(to='inicio')