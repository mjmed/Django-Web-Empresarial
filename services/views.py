from django.shortcuts import render

from .models import Service

def services(request):
    """Renderiza la vista de Servicios"""
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

