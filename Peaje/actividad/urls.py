from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peaje-dinamico/', views.peaje_dinamico, name='peaje_dinamico'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios/', views.servicios, name='servicios'),
    path('atencion-al-cliente/', views.atencion_al_cliente, name='atencion_al_cliente'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
]
