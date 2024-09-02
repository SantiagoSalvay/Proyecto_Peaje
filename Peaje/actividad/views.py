from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Casilla(request):
    return render(request, 'casilla.html')

def comienza_turno(request):
    return render(request, 'comienza_turno.html')

def cobro(request):
    return render(request, 'cobro.html')

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


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="factura.pdf"'  

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)


    p.setTitle("Factura")

    width, height = letter


    p.setFont("Helvetica-Bold", 18)
    p.drawString(100, height - 50, "Factura de Cobro - Paso Seguro")


    p.setFont("Helvetica", 12)
    p.drawString(100, height - 100, f"Peaje: X")
    p.drawString(100, height - 120, f"Casilla: X")


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
    qr.add_data('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')


    img_pil = img.convert('RGB')

    img_reader = ImageReader(img_pil)

    p.drawImage(img_reader, 100, height - 400, 150, 150)

    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
