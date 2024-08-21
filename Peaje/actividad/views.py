from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def telepase(request):
    return render(request, 'telepase.html')

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

def foro(request):
    return render(request, 'Foro.html')

def obras(request):
    return render(request, 'Obras.html')

def obras_ejecucion(request):
    return render(request, 'obras_e.html')

def obras_ejecutadas(request):
    return render(request, 'obras_ec.html')