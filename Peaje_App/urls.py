from django.urls import path
from .views import IndexView, CargarOperadorView, CasillaView, ComienzaTurnoView, CobroView, MultaView, FinTurnoView, GenerarFacturaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cargar-operador/', CargarOperadorView.as_view(), name='cargar_operador'),
    path('casilla/', CasillaView.as_view(), name='casilla'),
    path('casilla/comienza-turno/', ComienzaTurnoView.as_view(), name='comienza_turno'),
    path('casilla/comienza-turno/cobro', CobroView.as_view(), name='cobro'),
    path('casilla/comienza-turno/cobro/multa', MultaView.as_view(), name='multa'),
    path('casilla/comienza-turno/cobro/fin-turno', FinTurnoView.as_view(), name='turno'),
    path('generar-factura/', GenerarFacturaView.as_view(), name='generar_factura'),
]
