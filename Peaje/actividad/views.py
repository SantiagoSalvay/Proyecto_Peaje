from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def peaje_dinamico(request):
    return render(request, 'PEAJE-DINAMICO.html')

def quienes_somos(request):
    return render(request, 'QUIENES-SOMOS.html')

def servicios(request):
    return render(request, 'SERVICIOS.html')

def atencion_al_cliente(request):
    return render(request, 'ATENCION-AL-CLIENTE.html')

def login(request): 
    return render(request, 'LOGIN.html')

def registro(request):
    return render(request, 'REGISTER.html')

def recuperar_contrasena(request):
    return render(request, 'RECUCONTRA.html')

