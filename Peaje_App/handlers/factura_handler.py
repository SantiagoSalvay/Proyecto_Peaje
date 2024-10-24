from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import qrcode
from io import BytesIO
from django.http import HttpResponse
import random
from datetime import datetime

class FacturaHandler:
    @staticmethod
    def generar_factura_pdf(request):
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
