from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm


def contact(request):
    """Renderiza la vista de Contacto"""
    # crea la plantilla vacía
    contact_form = ContactForm()
    
    # detecta si se ha enviado por POST algún dato
    if request.method == 'POST':
        # rellena la planilla con la información de la petición
        contact_form = ContactForm(data=request.POST)
        
        # verifica que todos los datos sean correctos
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            # envía el correo
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", # asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content), # cuerpo
                "no-contestar@inbox.mailtrap.io", # email_origen
                ["developweb.test21@gmail.com"], # email_destino
                reply_to=[email]
            )
            
            try:
                # envía el mensaje
                email.send()
                # redirecciona
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')
        
    return render(request, 'contact/contact.html', {'form': contact_form})
