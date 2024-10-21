from django.shortcuts import render, redirect
from django.views import View
from .handlers.index_handler import procesar_login
from .handlers.operador_handler import registrar_operador, procesar_casilla
from .handlers.factura_handler import generar_factura_pdf
from .handlers.cobro_handler import CobroHandler


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return procesar_login(request)

class CargarOperadorView(View):
    def get(self, request):
        return render(request, 'registro_trabajador.html')

    def post(self, request):
        return registrar_operador(request)

class CasillaView(View):
    def get(self, request):
        return render(request, 'casilla.html')

    def post(self, request):
        return procesar_casilla(request)


class ComienzaTurnoView(View):
    def get(self, request):
        return render(request, 'comienza_turno.html')


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
        return generar_factura_pdf(request)
