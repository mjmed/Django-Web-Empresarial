# Web Empresarial

## *Curso Práctico de Django con Python: Desarrollo Web Backend*

**Web Empresarial** es un proyecto intermedio para practicar lo aprendido en **Web Personal** e introducir nuevos conceptos, basado en realizar la web de presentación de una cafetería con varias secciones dinámicas manejadas desde el panel de administrador.

Incluye:
+ **Django Templates**
+ Entorno virtual con **Pipenv**
+ Personalización del panel administrador de _Django_
+ **Procesadores de contexto**
+ **Temple Tags propios**
+ Editor **wysiwyg**
+ Formularios con _Django.forms_
+ Envío de correos electrónicos
+ Grupos y permisos

### Librerías y paquetes utilizados:
- [**Django CKEditor**](https://django-ckeditor.readthedocs.io/en/latest/): editor de texto tipo _word_ para campos _TextField_.

### Versión: 1.0.0

### Notas:
Comando para activar el entorno virtual:
```
pipenv shell
```

Comando para ver todos los paquetes (con sus dependencias) instaladas:
```
pip list --local
```
o
```
pipenv graph
```

Comando para instalar las dependencias del proyecto desde el fichero requirements.txt (con el entorno virtual activado):
```
pip install -r requirements.txt
```

Comando para crear o actualizar el fichero requirements.txt (con el entorno virtual activado):
```
pip freeze > requirements.txt
```

Comando para ejecutar el servidor en desarrollo:
```
python manage.py runserver
```

Incluir en la raíz del directorio la carpeta **media** con las subcarpetas **blog** y **services**.
```
˅ media
    > blog
    > services
```
