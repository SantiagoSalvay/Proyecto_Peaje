from Peaje_App.models import TurnoDeTrabajo
from django.contrib import messages

def cargar_turno(request):
    if request.method == "POST":
        id_operador = request.POST.get('id_operador')
        fecha_hora_de_inicio = request.POST.get('fecha_hora_de_inicio')
        fecha_hora_de_fin = request.POST.get('fecha_hora_de_fin')
        id_operador = request.POST.get('id_operador')
        numero_de_casilla = request.POST.get('numero_de_casilla')
        numero_de_estacion = request.POST.get('numero_de_estacion')

        try:
            turno = TurnoDeTrabajo(
                fecha_hora_de_inicio=fecha_hora_de_inicio,
                fecha_hora_de_fin=fecha_hora_de_fin,
                id_operador_id=id_operador,
                numero_de_casilla_id=numero_de_casilla,
                numero_de_estacion_id=numero_de_estacion
            )
            turno.save()
            messages.success(request, "Turno de trabajo cargado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al cargar el turno: {e}")
