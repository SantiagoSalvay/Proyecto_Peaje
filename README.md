# Proyecto de Gestión de Peaje - "Paso Seguro"

Este proyecto es una aplicación web de gestión de peajes, llamada "Paso Seguro", desarrollada con Django. Permite realizar diversas operaciones relacionadas con la administración de cobros en casillas de peaje, el control de turnos, y la generación de reportes en formato PDF.

## Características principales

- **Gestión de turnos**: Permite iniciar y finalizar turnos de los operadores.
- **Gestión de cobros**: Registro y cálculo de los montos cobrados en función del tipo de vehículo.
- **Generación de reportes**: Generación de un PDF al final de cada turno, con un resumen de las transacciones realizadas.
- **Interfaz moderna**: Uso de Bootstrap para proporcionar una interfaz intuitiva y adaptable.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `Peaje_Proyecto/`: Directorio principal del proyecto Django.
  - `Peaje_Proyecto/`: Contiene la configuración del proyecto (urls, settings, etc.).
  - `static/`: Archivos estáticos como hojas de estilo CSS y scripts JS.
  - `templates/`: Archivos HTML que representan la interfaz de la aplicación.
  - `apps/`: Directorios que contienen las aplicaciones individuales dentro del proyecto.
  - `__pycache__/`: Archivos compilados por Python para mejorar el rendimiento.
  
- `static/css/`: Contiene las hojas de estilo para diferentes partes de la aplicación (e.g., `casilla.css`, `fin_turno.css`).
- `static/js/`: Contiene los scripts JavaScript asociados a la funcionalidad dinámica de cada parte de la aplicación.
- `templates/`: Contiene los archivos HTML para las vistas del sistema como `casilla.html`, `cobro.html`, `fin_turno.html`, etc.

## Instalación

### Requisitos

Para ejecutar el proyecto necesitarás instalar las siguientes dependencias:

- **Python 3.12.4**: Puedes descargar Python desde [python.org](https://www.python.org/downloads/).
- **Django 5.1.1**: Django es el framework utilizado para desarrollar la aplicación.
- **reportlab**: Librería utilizada para generar archivos PDF en Python.
- **qrcode**: Librería para generar códigos QR.

### Pasos de instalación

1. **Clona el repositorio**:

   Clona el proyecto desde el repositorio (reemplaza `<url-del-repositorio>` con el enlace correspondiente):

   ```bash
   git clone <url-del-repositorio>

2. **Navega al directorio del proyecto**:


   ```bash
   cd Proyecto_Peaje

3. **Instala las dependencias necesarias**:


   ```bash
   pip install -r requirements.txt

4. **Aplica las migraciones**:


   ```bash
   python manage.py migrate

5. **Ejecuta el servidor de desarrollo**:


   ```bash
   python manage.py runserver

6. **Accede a la aplicacion**:

   Abre tu navegador y accede a la aplicación en la siguiente URL:

   ```bash
   http://127.0.0.1:8000

## Generación de reportes PDF

Al finalizar cada turno, se genera un reporte en formato PDF que incluye los detalles del cobro. Este se puede descargar automáticamente al hacer clic en el botón "Terminar Turno". El reporte incluye:

- Nombre y apellido del operador.
- Número de casilla.
- Sentido de cobro.
- Monto recaudado.
- Código QR con enlace a más información.

## Archivos importantes

- `views.py`: Contiene la lógica de generación de los reportes PDF.
- `urls.py`: Define las rutas de acceso a las distintas funcionalidades del sistema.
- `templates/`: Los archivos HTML que estructuran la interfaz del usuario.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Miembros

- Mateo Raviolo
- Mateo Barbini
- Santiago Salvay





