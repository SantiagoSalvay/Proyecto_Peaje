from django.shortcuts import render, redirect
from django.views import View
from .handlers.index_handler import IndexHandler
from .handlers.operador_handler import OperadorHandler
from .handlers.factura_handler import FacturaHandler
from .handlers.cobro_handler import CobroHandler
from .handlers.casilla_handler import CasillaHandler
from .handlers.turno_handler import GestionCobroHandler
from .models import Operador
from django.urls import reverse

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return IndexHandler.procesar_login(request)

class CargarOperadorView(View):
    def get(self, request):
        operadores = Operador.objects.all()
        return render(request, 'registro_trabajador.html', {'operadores': operadores})

    def post(self, request):
        return OperadorHandler.registrar_operador(request)


class CasillaView(View):
    def get(self, request):
        return render(request, 'casilla.html')

    def post(self, request):
        return CasillaHandler.procesar_casilla(request)

class ComienzaTurnoView(View):
    def get(self, request):  # Ahora acepta `self` y `request`
        # Renderiza el template
        return render(request, "comienza_turno.html")

    def post(self, request):  # También acepta `self` y `request`
        # Instancia el handler y llama a la función que guarda datos
        handler = GestionCobroHandler(request)
        handler.guardar_datos_cobro()

        # Redirige a la siguiente vista o template según sea necesario
        return redirect(reverse("cobro"))

class DatoTurno(View):
    def get(self):
        handler = GestionCobroHandler(self.request)
        dinero_actual, sentido_cobro = handler.obtener_datos_cobro()

        return render(self.request, "cobro.html", "fin_turno.html", {
            "dinero_actual": dinero_actual,
            "sentido_cobro": sentido_cobro,
        })



class CobroView(View):
    def get(self, request):
        return CobroHandler.handle_get(request)

    def post(self, request):
        return CobroHandler.handle_post(request)

class MultaView(View):
    def get(self, request):
        return render(request, 'multa.html')

class FinTurnoView(View):
    def get(self, request):
        return render(request, 'fin_turno.html')

class GenerarFacturaView(View):
    def get(self, request):
        return FacturaHandler.generar_factura_pdf(request)
