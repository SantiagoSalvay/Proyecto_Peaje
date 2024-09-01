from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('casilla/', views.Casilla, name='casilla'),
    path('casilla/comienza-turno/', views.comienza_turno, name='comienza_turno'),

]
