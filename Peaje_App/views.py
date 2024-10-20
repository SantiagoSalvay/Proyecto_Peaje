from django.shortcuts import render, redirect
from Peaje_App.models import Operador
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import qrcode
from io import BytesIO
from datetime import datetime
import random


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
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


class CargarOperadorView(View):
    def get(self, request):
        return render(request, 'registro_trabajador.html')

    def post(self, request):
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        dni = request.POST.get('dni')
        contraseña = request.POST.get('contraseña')

        if Operador.objects.filter(dni=dni).exists():
            messages.error(request, "El DNI ya está registrado.")
            return render(request, 'registro_trabajador.html')  

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
            return render(request, 'registro_trabajador.html')  


class CasillaView(View):
    def get(self, request):
        return render(request, 'casilla.html')

    def post(self, request):
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


class ComienzaTurnoView(View):
    def get(self, request):
        return render(request, 'comienza_turno.html')


class CobroView(View):
    def get(self, request):
        return render(request, 'cobro.html')

    def post(self, request):
        sentido_cobro = request.POST.get('sentido-cobro')
        numero_casilla = request.POST.get('numero-casilla')
        return render(request, 'cobro.html', {
            'sentido_cobro': sentido_cobro,
            'numero_casilla': numero_casilla
        })


class MultaView(View):
    def get(self, request):
        return render(request, 'multa.html')


class FinTurnoView(View):
    def get(self, request):
        return render(request, 'fin_turno.html')


class GenerarFacturaView(View):
    def get(self, request):
        
        vehiculo = request.GET.get('vehiculo')
        importe = request.GET.get('importe')
        numero_casilla = request.session.get('numero_casilla')

        
        numero_ticket = random.randint(100000, 999999)
        nombre_estacion = f"Estación Paso Seguro {random.randint(1, 20)}"
        numero_estacion = random.randint(1, 10)
        ubicacion_estacion = f"Ruta {random.randint(1, 10)} - Km {random.randint(50, 500)}"
        numero_legajo_operador = random.randint(1000, 9999)

        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="factura_{vehiculo}.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        p.setTitle("Factura")
        width, height = letter

        p.setFont("Helvetica-Bold", 18)
        p.drawString(100, height - 50, "Factura de Cobro - Paso Seguro")

        
        p.setFont("Helvetica", 12)
        p.drawString(100, height - 100, f"Número de Ticket: {numero_ticket}")
        p.drawString(100, height - 120, f"Nombre de la Estación: {nombre_estacion}")
        p.drawString(100, height - 140, f"Número de Estación: {numero_estacion}")
        p.drawString(100, height - 160, f"Ubicación: {ubicacion_estacion}")
        p.drawString(100, height - 180, f"Casilla: {numero_casilla}")

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        p.drawString(100, height - 200, f"Fecha y Hora de Emisión: {fecha_hora}")
        p.drawString(100, height - 220, f"Categoría de Vehículo: {vehiculo}")
        p.drawString(100, height - 240, f"Importe Cobrado: ${importe}")
        p.drawString(100, height - 260, f"Número de Legajo del Operador: {numero_legajo_operador}")

        p.drawString(100, height - 300, "Muchas gracias por confiar en nuestro peaje")

        
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('https://www.youtube.com/watch?v=zu2Eaw6Ohxc')  
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img_pil = img.convert('RGB')
        img_reader = ImageReader(img_pil)

        
        p.drawImage(img_reader, width - 160, height - 160, 150, 150)

        
        p.showPage()
        p.save()

        
        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/pdf')
