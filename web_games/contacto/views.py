from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse
# Create your views here.

def contacto(request):
    #Creo el objeto de tipo formulario
    formulario = ContactForm()
    if request.method == "POST":
        #Enviaron el formulario apretando el boton enviar y no por la carga
        #de la pagina
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre",'')
            correo = request.POST.get('correo','')
            mensaje = request.POST.get('mensaje','')
            email = EmailMessage("Le han contactado!",
            "{} {}: dijo {}".format(nombre,correo,mensaje),
            "gamesduocz@gmail.com",
            ['gamesduocz@gmail.com'],
            reply_to=[correo])
            try:
                email.send()
                #TODO:Mejorar esto para que mande el ok
                #localhost:8000/contacto?ok
                return redirect(reverse('contacto')+"?ok")
            except Exception as e:
                #localhost:8000/contacto?error
                return redirect(reverse('contacto') + "?error")
    return render(request, "contacto.html", {'form':formulario})
