# MusicProBodega
Version 1.3 de sistema de bodega para musicpro

Instrucciones
- Instale los requisitos: pip install -r requirements.txt
- Luego, realice migraciones de base de datos: python manage.py makemigrations
- python manage.py migrate
- Y finalmente, ejecute la aplicación: python manage.py runserver

Para la cuenta de administrador y para iniciar sesion, cree una con superusuario: python manage.py createsuperuser

Para ver los productos como Api la direccion es http://127.0.0.1:8000/inventory/api/products/ Es con localhost.
