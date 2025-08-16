# Proyecto Django: Inventario de Productos

Este proyecto es una aplicación web desarrollada con Django para la gestión de inventario de productos.

## Estructura del Proyecto

- `inventario/`: Configuración principal del proyecto Django.
- `productos/`: Aplicación encargada de la gestión de productos, con modelos, vistas, URLs y migraciones.
- `templates/`: Plantillas HTML para la interfaz de usuario (`base.html`, `listar.html`).
- `db.sqlite3`: Base de datos SQLite utilizada por defecto.
- `manage.py`: Script de administración de Django.
- `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.

## Funcionalidades
- Listado de productos.
- Administración de productos (crear, editar, eliminar).
- Interfaz web basada en plantillas Jinja2/Django.

## Instalación y Ejecución
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
3. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
4. Accede a la aplicación en [http://localhost:8000](http://localhost:8000)

## Uso en Clase
Este proyecto sirve como base para prácticas y ejemplos de desarrollo web avanzado con Django, incluyendo el uso de plantillas, modelos y vistas.

## Autor
- EdJGM

## Licencia
Uso educativo.
