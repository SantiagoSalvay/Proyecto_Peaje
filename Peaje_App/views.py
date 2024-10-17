from django.shortcuts import render, redirect
from Peaje_App.models import Operador
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        contraseña = request.POST.get('contraseña')

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

def Casilla(request):
    if request.method == 'POST':
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

def comienza_turno(request):
    return render(request, 'comienza_turno.html')

def cobro(request):
    return render(request, 'cobro.html')

def multa(request):
    return render(request, 'multa.html')

def fin_turno(request):
    return render(request, 'fin_turno.html')

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import qrcode
from io import BytesIO
from datetime import datetime

def generar_factura(request):
    vehiculo = request.GET.get('vehiculo')
    importe = request.GET.get('importe')

    
    numero_casilla = request.session.get('numero_casilla')
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{vehiculo}.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.setTitle("Factura")
    width, height = letter

    
    p.setFont("Helvetica-Bold", 18)
    p.drawString(100, height - 50, "Factura de Cobro - Paso Seguro")

    p.setFont("Helvetica", 12)
    p.drawString(100, height - 100, f"Peaje: Paso Seguro")

    
    p.drawString(100, height - 120, f"Casilla: {numero_casilla}")  

    
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    p.drawString(100, height - 140, f"Fecha y Hora de Emisión: {fecha_hora}")

    
    p.drawString(100, height - 160, f"Tipo de Vehículo: {vehiculo}")
    p.drawString(100, height - 180, f"Importe Cobrado: ${importe}")
    
    
    p.drawString(100, height - 220, "Muchas gracias por confiar en nuestro peaje")

    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('https://www.youtube.com/watch?v=xvFZjo5PgG0')  
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_pil = img.convert('RGB')
    img_reader = ImageReader(img_pil)

    
    p.drawImage(img_reader, 100, height - 400, 150, 150)

    
    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

def cobro(request):
    if request.method == "POST":
        sentido_cobro = request.POST.get('sentido-cobro')
        numero_casilla = request.POST.get('numero-casilla')
        return render(request, 'cobro.html', {
            'sentido_cobro': sentido_cobro,
            'numero_casilla': numero_casilla
        })
    return render(request, 'cobro.html')



