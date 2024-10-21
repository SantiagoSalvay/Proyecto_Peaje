from Peaje_App.models import Operador
from django.contrib import messages
from django.shortcuts import render, redirect

def registrar_operador(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        dni = request.POST.get('dni')
        contraseña = request.POST.get('contraseña')

        if Operador.objects.filter(dni=dni).exists():
            messages.error(request, "El DNI ya está registrado.")
        else:
            try:
                operador = Operador(
                    nombre=nombre,
                    apellido=apellido,
                    telefono=telefono,
                    direccion=direccion,
                    dni=dni,
                    contraseña=contraseña  
                )
                operador.save()
                messages.success(request, "Operador registrado exitosamente.")
                return redirect('index')  
            except Exception as e:
                messages.error(request, f"Error al registrar el operador: {e}")
    
        operadores = Operador.objects.all()
        return render(request, 'registro_trabajador.html', {'operadores': operadores})

def procesar_casilla(request):
    numero_casilla = request.POST.get('numero_casilla')
    nombre = request.session.get('nombre')
    apellido = request.session.get('apellido')

    try:
        operador = Operador.objects.get(nombre=nombre, apellido=apellido)
        operador.casilla_seleccionada = numero_casilla
        operador.save()

        request.session['numero_casilla'] = numero_casilla
        messages.success(request, f"Casilla {numero_casilla} seleccionada correctamente.")
        return redirect('comienza_turno')  
    except Operador.DoesNotExist:
        messages.error(request, "No se encontró el operador.")

    return render(request, 'casilla.html')
