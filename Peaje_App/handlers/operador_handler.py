from django.shortcuts import redirect, render
from Peaje_App.models import Operador
from django.contrib import messages
from Peaje_App.models import Operador  
from django.shortcuts import get_object_or_404


class OperadorHandler:
    @staticmethod
    def registrar_operador(request):
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            print("Nombre recibido:", nombre)  
            
            
            apellido = request.POST.get('apellido')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            dni = request.POST.get('dni')
            contraseña = request.POST.get('contraseña')

            if not nombre:
                messages.error(request, "El campo 'nombre' es obligatorio.")
                return redirect('cargar_operador')

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

    
    @staticmethod
    def get_operadores():
        return Operador.objects.all()
    
    @staticmethod
    def eliminar_operador(dni):
        operador = get_object_or_404(Operador, dni=dni)  
        operador.delete()

