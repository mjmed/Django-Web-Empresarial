from django.shortcuts import render

def home(request):
    """Renderiza la vista de Inicio"""
    return render(request, 'core/home.html')

def about(request):
    """Renderiza la vista de Historia"""
    return render(request, 'core/about.html')

def store(request):
    """Renderiza la vista de Visítanos"""
    return render(request, 'core/store.html')
