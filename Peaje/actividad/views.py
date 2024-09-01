from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Casilla(request):
    return render(request, 'casilla.html')

def comienza_turno(request):
    return render(request, 'comienza_turno.html')