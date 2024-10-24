from django.shortcuts import redirect, render
from Peaje_App.models import Operador
from django.contrib import messages

class IndexHandler:
    @staticmethod
    def procesar_login(request):
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        contraseña = request.POST.get('contraseña')

        if nombre == 'admin' and apellido == 'admin' and contraseña == 'admin':
            return redirect('/cargar-operador/')

        try:
            operador = Operador.objects.get(nombre=nombre, apellido=apellido)
            if operador.contraseña == contraseña:
                request.session['nombre'] = operador.nombre
                request.session['apellido'] = operador.apellido
                return redirect('/casilla/')
            else:
                messages.error(request, "Contraseña incorrecta.")
        except Operador.DoesNotExist:
            messages.error(request, "Nombre o apellido incorrectos.")
        
        return render(request, 'index.html')
