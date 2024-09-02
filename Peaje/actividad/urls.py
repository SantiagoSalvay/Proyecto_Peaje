from django.urls import path
from . import views

urlpatterns = [
    path('', views.cobro, name='index'),
    path('casilla/', views.Casilla, name='casilla'),
    path('casilla/comienza-turno/', views.comienza_turno, name='comienza_turno'),
    path('casilla/comienza-turno/cobro', views.cobro, name='cobro'),
    path('generar-factura/', views.generar_factura, name='generar_factura'),


]
