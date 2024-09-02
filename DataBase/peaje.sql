DROP DATABASE IF EXISTS peaje_db;
CREATE DATABASE peaje_db;
USE peaje_db;

CREATE TABLE IF NOT EXISTS ESTACION_DE_PEAJE (
    numero_de_estacion INT,
    nombre VARCHAR(255) NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
    CONSTRAINT pk_estacion PRIMARY KEY (numero_de_estacion)
);

CREATE TABLE IF NOT EXISTS CASILLA_DE_PEAJE (
    numero_de_casilla INT,
    numero_de_estacion INT,
    sentido_de_cobro VARCHAR(255) NOT NULL,
    CONSTRAINT pk_casilla PRIMARY KEY (numero_de_casilla),
    CONSTRAINT fk_estacion_casilla FOREIGN KEY (numero_de_estacion) REFERENCES ESTACION_DE_PEAJE(numero_de_estacion)
);

CREATE TABLE IF NOT EXISTS OPERADOR (
    id_operador INT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    CONSTRAINT pk_operador PRIMARY KEY (id_operador)
);

CREATE TABLE IF NOT EXISTS TURNO_DE_TRABAJO (
    id_turno INT,
    fecha_hora_de_inicio DATETIME NOT NULL,
    fecha_hora_de_fin DATETIME NOT NULL,
    monto_de_cambio_entregado FLOAT NOT NULL,
    id_operador INT,
    numero_de_casilla INT,
    plata_inicial FLOAT NOT NULL,
    plata_final FLOAT NOT NULL,
    numero_de_estacion INT,
    CONSTRAINT pk_turno PRIMARY KEY (id_turno),
    CONSTRAINT fk_operador_turno FOREIGN KEY (id_operador) REFERENCES OPERADOR(id_operador),
    CONSTRAINT fk_casilla_turno FOREIGN KEY (numero_de_casilla) REFERENCES CASILLA_DE_PEAJE(numero_de_casilla),
    CONSTRAINT fk_estacion_turno FOREIGN KEY (numero_de_estacion) REFERENCES ESTACION_DE_PEAJE(numero_de_estacion)
);

CREATE TABLE IF NOT EXISTS TIPO_VEHICULO (
    id_tipo_vehiculo INT,
    descripcion VARCHAR(255) NOT NULL,
    CONSTRAINT pk_tipo_vehiculo PRIMARY KEY (id_tipo_vehiculo)
);

CREATE TABLE IF NOT EXISTS HISTORIAL_TARIFAS (
    id_historial INT,
    id_tipo_vehiculo INT,
    fecha_inicio DATETIME NOT NULL,
    fecha_fin DATETIME NOT NULL,
    tarifa FLOAT NOT NULL,
    tarifa_actual INT NOT NULL,
    CONSTRAINT pk_historial PRIMARY KEY (id_historial),
    CONSTRAINT fk_tipo_vehiculo_historial FOREIGN KEY (id_tipo_vehiculo) REFERENCES TIPO_VEHICULO(id_tipo_vehiculo)
);

CREATE TABLE IF NOT EXISTS REGISTRO_EFECTIVO (
    id_registro INT,
    fecha_hora_de_emision DATETIME NOT NULL,
    importe_cobrado FLOAT NOT NULL,
    codigo_QR VARCHAR(255),
    id_historial_tarifas INT,
    CONSTRAINT pk_registro_efectivo PRIMARY KEY (id_registro),
    CONSTRAINT fk_historial_tarifas_registro_efectivo FOREIGN KEY (id_historial_tarifas) REFERENCES HISTORIAL_TARIFAS(id_historial)
);

CREATE TABLE IF NOT EXISTS REGISTRO_TELEPASE (
    id_registro INT,
    fecha_hora_de_emision DATETIME NOT NULL,
    importe_cobrado FLOAT NOT NULL,
    codigo_telepase VARCHAR(255),
    usuario VARCHAR(255),
    direccion VARCHAR(255),
    patente VARCHAR(255),
    tarjeta_debito INT,
    id_historial_tarifas INT,
    CONSTRAINT pk_registro_telepase PRIMARY KEY (id_registro),
    CONSTRAINT fk_historial_tarifas_registro_telepase FOREIGN KEY (id_historial_tarifas) REFERENCES HISTORIAL_TARIFAS(id_historial)
);

CREATE TABLE IF NOT EXISTS NO_PAGADOS (
    id_no_pagado INT,
    nombre_conductor VARCHAR(255),
    apellido_conductor VARCHAR(255),
    dni_conductor VARCHAR(20),
    fecha_hora_de_emision DATETIME NOT NULL,
    CONSTRAINT pk_no_pagado PRIMARY KEY (id_no_pagado)
);

CREATE TABLE IF NOT EXISTS PASADA (
    id_pasada INT,
    id_tipo_vehiculo INT,
    fecha_hora_de_pasada DATETIME NOT NULL,
    pasada_telepase VARCHAR(255),
    pasada_efectivo VARCHAR(255),
    pasada_no_paga VARCHAR(255),
    CONSTRAINT pk_pasada PRIMARY KEY (id_pasada),
    CONSTRAINT fk_tipo_vehiculo_pasada FOREIGN KEY (id_tipo_vehiculo) REFERENCES TIPO_VEHICULO(id_tipo_vehiculo)
);
