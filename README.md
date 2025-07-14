# Tarea CRUD: 
# 📚 📚 Biblioteca de Libros 📚 📚

![Banner Proyectos](https://github.com/user-attachments/assets/a5e74f64-6653-475f-83e2-29bd4a2aadbf)

Este proyecto consiste en una biblioteca autogestionada de manera online; Eres el superuser, y puedes realizar las 4 operaciones CRUD sobre todos los libros que quieras: Añade(C), consulta(R), modifica(U), o borra(D) segun lo que necesites!

---

## 📁 Estructura del Proyecto

```
TareaJul14_CRUDLibros/                   # Origen del proyecto
├── README.md
└── system_books_kiru          
    ├── db.sqlite3
    ├── libros                           # Libros APP
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations                   # Migraciones
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py                    # Gestiona los modelos
    │   ├── templates                    # carpeta templates para cada operacion CRUD
    │   │   └── libros
    │   │       ├── crear_libro.html
    │   │       ├── detalle_libro.html
    │   │       ├── editar_libro.html
    │   │       ├── eliminar_libro.html
    │   │       └── lista_libros.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py                        # main de python
    └── system_books_kiru                # proyecto
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

---

## ⏩Aplicación CRUD y Django


## 📖 1. ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web?
CRUD hace referencia a las cuatro operaciones que utilizan una gran mayoría de aplicaciones web. Las siglas pertenecen a (C)reate, (R)ead, (U)pdate y (D)elete. O lo que es lo mismo, Crear, Leer, Actualizar y Eliminar. Por tanto estamos hablando de manejo de datos, consultas, entidades, etc… 

Para muestra los siguientes ejemplos:
Una tienda maneja CRUD a la hora de CREAR pedidos. 
Un gestor de tareas te permite BORRAR una, cuando ya la has completado. 
Una biblioteca te permite CONSULTAR los libros que tienes disponibles. 
Y en cualquier momento una red social te permite ACTUALIZAR tu perfil. 


## 📖 2. ¿Qué son los patrones de arquitectura en desarrollo de software?
Si nos pusieramos a picar código en un único archivo, resultaría algo muy complejo y sobre todo de difícil lectura y comprensión para un coder que no conozca el proyecto o esté acostumbrado a hacer las cosas de diferente manera. Por esto mismo existen los patrones de diseño o arquitectura, para organizar y estructurar el código de manera que una aplicación sea más fácil de comprender, o incluso de mantener y expandir. Seguir una estructura te permite separar funcionalidades, de manera que ante un cambio, te puede ser más fácil no poner en riesgo la totalidad del código al poder enfocarte únicamente en la parte del código que te está generando problemas. Una forma habitual es la separación entre la gestión de los datos, el mostrarlos, y la gestión de la lógica de negocio

### 📖 ○ ¿Qué es el patrón MVC (Modelo–Vista–Controlador)?
Es un patrón donde:
Modelo maneja los datos y la lógica de negocio.
Vista se encarga de mostrar la información al usuario.
Controlador gestiona las peticiones del usuario y conecta el modelo con la vista.

### 📖 ○ ¿Qué es el patrón MVT (Modelo–Vista–Template)?
Django usa una versión parecida al MVC llamada MVT:
Modelo: Igual que en MVC, gestiona los datos.
Vista: en Django, la vista contiene la lógica, o sea, qué hacer cuando alguien accede a una URL.
Template: es una capa/directorio que se encarga de mostrar el contenido en bloques de código HTML.

### 📖 ○ Diferencias entre MVC y MVT.
La principal diferencia está en cómo se llama cada parte:
En MVC, la "vista" es el HTML; en MVT, ese HTML se llama "template".
El controlador clásico de MVC no está definido como una capa separada en Django, ya que su función está repartida entre el sistema de enrutamiento (urls.py) y las vistas.

En MVC tradicional:
-Usuario hace clic en un botón.
-El Controlador recibe la acción.
-Consulta al Modelo.
-Le pasa los datos a la vista (HTML).

En Django (MVT):
-Usuario entra a una URL.
-Django busca una vista(view) que responda.
-Esa vista consulta al Modelo si necesita datos.
-Y luego envía los datos a un Template, que se muestra en el navegador.

### 📖 ○ ¿Cuál de estos dos patrones se usa en Django?
Django usa el patrón MVT.


## 📖 3. ¿Cómo se estructura un proyecto en Django? Explicar brevemente el rol de los modelos, vistas, templates y URLs.
Un proyecto de Django se divide en aplicaciones (que funcionan como módulos), y dentro de cada una hay funciones claras:
Modelos: Definen las tablas de la base de datos.
Vistas (views.py): Deciden qué pasa cuando un usuario entra a una URL (por ejemplo, mostrar un formulario, guardar datos, etc.).
Templates: Son los archivos HTML que ve el usuario.
URLs: Se encargan de dirigir las rutas (lo que escribes en el navegador) hacia la vista correcta.

### 📖 ○ ¿Para qué se usa el signo “%%” en los templates?
Se usan para poner instrucciones de Django dentro del HTML, como por ejemplo mostrar datos, hacer bucles o condiciones.


## 📖 4. ¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?
Primero, el usuario llena un formulario y lo envía. Ese formulario llega a una vista que revisa los datos y, si todo está bien, los guarda usando un modelo. Luego, si queremos, podemos redirigir al usuario a otra página o mostrarle un mensaje de éxito.
Básicamente: Solicitud POST del usuario que lleva a una vista (view) >> Django verifica que los datos sean válidos, y los introduce (save) en la base de datos >> Por último, además de las opciones anteriores, también se puede actualizar el contenido (UPDATE)


## 📖 5. ¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un CRUD, para qué es cada una? (Por ejemplo: startapp, makemigrations, migrate, runserver, ModelForm, admin, etc.)
Algunas de las mas importantes y que ya hemos utilizado en esta tarea, son:
startapp: Crea una nueva aplicación dentro del proyecto.
makemigrations: Prepara los cambios en los modelos para la base de datos.
migrate: Aplica esos cambios a la base de datos.
runserver: Inicia el servidor local para probar la aplicación.
ModelForm: Crea formularios directamente a partir de los modelos.
admin: Es una herramienta de Django que te permite manejar los datos desde una interfaz web muy completa, sin necesidad de programar nada extra.


## 📖 6. ¿Cómo funciona el Admin de Django?
Es como un panel de control que viene listo para usar. Solo tienes que registrar tus modelos en el archivo admin.py, y ya puedes crear, editar o eliminar registros desde el navegador. Es muy útil para pruebas o para que los administradores manejen la información sin tocar código.


## ⏩ Parte 2: Crear un CRUD
Desarrollar una aplicación básica con Django que permita gestionar una lista de libros.
Debes seguir los pasos del siguiente repositorio:
https://github.com/Factoria-F5-madrid/CRUD-django
*Nota: Puedes modificar el proyectos tu gusto, solo ten en cuenta que debe hacer lo mínimo
requerido, es decir, un CRUD.

## ⏩ Entrega

● Subir un repositorio con la práctica terminada
● Incluir un archivo README.md que contenga las respuestas a las preguntas de la
primera parte.

---
## 🛠️ Tecnologías empleadas

- Python en IntelliJ
- Git y GitHub para control de versiones
- Servidor Localhost

---
# Proyecto Monolítico en Django: Sistema de Gestión de Libros
---

## Índice
1. [Introducción a Django](#introducción-a-django)
2. [El Admin de Django](#el-admin-de-django)
3. [Configuración del Proyecto](#configuración-del-proyecto)
4. [Creación de Modelos](#creación-de-modelos)
5. [Configuración del Admin](#configuración-del-admin)
6. [Creación de Vistas](#creación-de-vistas)
7. [Configuración de URLs](#configuración-de-urls)
8. [Creación de Plantillas](#creación-de-plantillas)
9. [Ejecución del Proyecto](#ejecución-del-proyecto)
10. [Recursos](#recursos)

## Introducción a Django

Django es un framework de desarrollo web de alto nivel escrito en Python que fomenta el desarrollo rápido y el diseño limpio y pragmático. Fue creado para facilitar la creación de aplicaciones web complejas, orientadas a bases de datos.

Características principales de Django:
- Sigue el patrón de diseño Modelo-Vista-Template (MVT)
- Incluye un ORM (Object-Relational Mapping) potente
- Proporciona un panel de administración automático
- Tiene un sistema de autenticación incorporado
- Ofrece un framework de migración de bases de datos

Django se utiliza para desarrollar todo tipo de aplicaciones web, desde sistemas de gestión de contenidos y wikis hasta redes sociales y plataformas de noticias.

## El Admin de Django

El Admin de Django es una de las características más poderosas del framework. Es una interfaz de administración generada automáticamente que lee los metadatos de tus modelos para proporcionar una interfaz potente y lista para producción, donde los usuarios autorizados pueden gestionar el contenido de tu sitio.

Características del Admin de Django:
- Generación automática de interfaces CRUD para los modelos
- Sistemas de autenticación y autorización incorporados
- Personalización de la apariencia y el comportamiento
- Filtros y búsquedas avanzadas
- Gestión de relaciones entre modelos

El Admin de Django es especialmente útil para crear rápidamente una interfaz de gestión interna para tu aplicación o para prototipar un proyecto.

## Configuración del Proyecto

1. Crea tu entorno virtual, lo activas e Instala Django:

Crear entorno:

```bash
python -m venv .venv
```
Activar en windows

```bash
.venv/Scripts/activate
```
Activar en mac o linux

```bash
source .venv/Scripts/activate
```
Instalar django:

```bash
pip install django
```
2. Crea un nuevo proyecto Django:


```shellscript
django-admin startproject sistema_libros
cd sistema_libros
```

### Esta será tu estructura una vez creadas las aplicaciones
```plaintext
crud_python/ # Carpeta donde guardas tu proyecto
│
├── manage.py
├── libreria/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── libros/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── serializer.py
│   ├── tests.py
│   ├── urls.py 
│   ├── views.py
│
```

3. Crea una nueva aplicación:


```shellscript
python manage.py startapp libros
```

4. Agrega 'libros' a INSTALLED_APPS en sistema_libros/settings.py:


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'libros',
]
```

## Creación de Modelos

En libros/models.py, crea el modelo Libro:

```python
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo
```

Realiza las migraciones:

```shellscript
python manage.py makemigrations
python manage.py migrate
```

## Configuración del Admin

En libros/admin.py, registra el modelo Libro:

```python
from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'isbn')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('fecha_publicacion',)
```

## Creación de Vistas

En libros/views.py, crea las vistas para listar y detallar libros:

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('detalle_libro', libro_id=libro.id)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form, 'libro': libro})

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})
```

## Creación de Forms

En libros/forms.py, crea el formulario para tus vistas de crear y modificar/actualizar libros:

```python
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'fecha_publicacion', 'isbn']
```

## Configuración de URLs

En sistema_libros/urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('libros.urls')),
]
```

Crea libros/urls.py:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]
```

## Creación de Plantillas

Crea las siguientes plantillas:

libros/templates/libros/lista_libros.html:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Libros</title>
</head>
<body>
    <h1>Lista de Libros</h1>
    <ul>
    {% for libro in libros %}
        <li><a href="{% url 'detalle_libro' libro.id %}">{{ libro.titulo }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>
```

libros/templates/libros/detalle_libro.html:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ libro.titulo }}</title>
</head>
<body>
    <h1>{{ libro.titulo }}</h1>
    <p>Autor: {{ libro.autor }}</p>
    <p>Descripción: {{ libro.descripcion }}</p>
    <p>Fecha de publicación: {{ libro.fecha_publicacion }}</p>
    <p>ISBN: {{ libro.isbn }}</p>
    <a href="{% url 'lista_libros' %}">Volver a la lista</a>
</body>
</html>
```

libros/templates/libros/editar_libro.html:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Editar {{ libro.titulo }}</title>
</head>
<body>
    <h1>Editar {{ libro.titulo }}</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar cambios</button>
    </form>
    <a href="{% url 'detalle_libro' libro.id %}">Cancelar</a>
</body>
</html>
```

libros/templates/libros/crear_libro.html:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Crear Libro</title>
</head>
<body>
    <h1>Crear Libro</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
    <a href="{% url 'lista_libros' %}">Cancelar</a>
</body>
</html>
```
libros/templates/libros/eliminar_libro.html:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Eliminar {{ libro.titulo }}</title>
</head>
<body>
    <h1>Eliminar {{ libro.titulo }}</h1>
    <p>¿Estás seguro de que quieres eliminar este libro?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Sí, eliminar</button>
    </form>
    <a href="{% url 'detalle_libro' libro.id %}">Cancelar</a>
</body>
</html>
```

## Ejecución del Proyecto

1. Crea un superusuario para acceder al admin:


```shellscript
python manage.py createsuperuser
```

2. Inicia el servidor de desarrollo:


```shellscript
python manage.py runserver
```

3. Accede al admin en [http://localhost:8000/admin/](http://localhost:8000/admin/) y añade algunos libros.
4. Visita [http://localhost:8000/libros/](http://localhost:8000/libros/) para ver la lista de libros y [http://localhost:8000/libros/1/](http://localhost:8000/libros/1/) para ver los detalles de un libro (reemplaza '1' con el ID de un libro existente).

## Recursos

* [Artículo de Medium para crear tu primer CRUD](https://medium.com/@gutundbose/aplicaci%C3%B3n-crud-con-django-82bb217493ea)
