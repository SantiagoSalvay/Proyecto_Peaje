from django.shortcuts import redirect, render
from Peaje_App.models import Operador
from django.contrib import messages

class OperadorHandler:
    @staticmethod
    def registrar_operador(request):
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            dni = request.POST.get('dni')
            contraseña = request.POST.get('contraseña')

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
            
            return redirect('cargar_operador')  
        
        
        operadores = Operador.objects.all()
        return render(request, 'registro_trabajador.html', {'operadores': operadores})

