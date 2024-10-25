from django.shortcuts import redirect, render
from Peaje_App.models import Operador
from django.contrib import messages

class CasillaHandler:
    @staticmethod
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
    

    
