from django.db import models
from django.contrib.auth.hashers import  check_password, make_password
class EstacionDePeaje(models.Model):
    numero_de_estacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class CasillaDePeaje(models.Model):
    numero_de_casilla = models.IntegerField(primary_key=True)
    numero_de_estacion = models.ForeignKey(EstacionDePeaje, on_delete=models.CASCADE)
    sentido_de_cobro = models.CharField(max_length=255)

    def __str__(self):
        return f"Casilla {self.numero_de_casilla} - Estación {self.numero_de_estacion}"


class Operador(models.Model):
    id_operador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    dni = models.IntegerField(unique=True, default=0)
    contraseña = models.CharField(max_length=255) 

    def verificar_contraseña(self, raw_password):
        return raw_password == self.contraseña  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class TurnoDeTrabajo(models.Model):
    id_turno = models.IntegerField(primary_key=True)
    fecha_hora_de_inicio = models.DateTimeField()
    fecha_hora_de_fin = models.DateTimeField()
    monto_de_cambio_entregado = models.FloatField()
    id_operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    numero_de_casilla = models.ForeignKey(CasillaDePeaje, on_delete=models.CASCADE)
    plata_inicial = models.FloatField()
    plata_final = models.FloatField()
    numero_de_estacion = models.ForeignKey(EstacionDePeaje, on_delete=models.CASCADE)

    def __str__(self):
        return f"Turno {self.id_turno} - Operador {self.id_operador}"


class TipoVehiculo(models.Model):
    id_tipo_vehiculo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion


class HistorialTarifas(models.Model):
    id_historial = models.IntegerField(primary_key=True)
    id_tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    tarifa = models.FloatField()
    tarifa_actual = models.IntegerField()

    def __str__(self):
        return f"Historial {self.id_historial} - Vehículo {self.id_tipo_vehiculo}"


class RegistroEfectivo(models.Model):
    id_registro = models.IntegerField(primary_key=True)
    fecha_hora_de_emision = models.DateTimeField()
    importe_cobrado = models.FloatField()
    codigo_QR = models.CharField(max_length=255, null=True, blank=True)
    id_historial_tarifas = models.ForeignKey(HistorialTarifas, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registro Efectivo {self.id_registro}"


class RegistroTelepase(models.Model):
    id_registro = models.IntegerField(primary_key=True)
    fecha_hora_de_emision = models.DateTimeField()
    importe_cobrado = models.FloatField()
    codigo_telepase = models.CharField(max_length=255, default='SIN_CODIGO')
    usuario = models.CharField(max_length=255, default='No especificado')
    direccion = models.CharField(max_length=255, default='No especificado')
    patente = models.CharField(max_length=255, default='SIN_PATENTE')
    tarjeta_debito = models.IntegerField(default='SIN_DATOS')
    id_historial_tarifas = models.ForeignKey(HistorialTarifas, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registro Telepase {self.id_registro}"


class NoPagados(models.Model):
    id_no_pagado = models.IntegerField(primary_key=True)
    nombre_conductor = models.CharField(max_length=255)
    apellido_conductor = models.CharField(max_length=255)
    dni_conductor = models.CharField(max_length=20)
    fecha_hora_de_emision = models.DateTimeField()
    tipo_vehiculo = models.CharField(max_length=20, null=True, blank=True)  
    importe = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  

    def __str__(self):
        return f"No Pagado {self.id_no_pagado}"


class Pasada(models.Model):
    id_pasada = models.IntegerField(primary_key=True)
    id_tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    fecha_hora_de_pasada = models.DateTimeField()
    pasada_telepase = models.CharField(max_length=255, null=True, blank=True)   
    pasada_efectivo = models.CharField(max_length=255, null=True, blank=True)
    pasada_no_paga = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Pasada {self.id_pasada}"
