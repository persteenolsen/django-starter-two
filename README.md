

# Django + Vercel

This example shows how to use Django 4 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

Last updated: 30-04-2025

Node version selected at Vercel Cloud: 22

## Demo

https://django-starter-two.vercel.app/

## Demo / Admin

The Administration Backend can use MySQL for Dev + Prod but can also work with a SQLite DB for developement locally ( Dev )

## How it Works

Our Django application, `example` is configured as an installed application in `vercel_app/settings.py`:

```python
# vercel_app/settings.py
INSTALLED_APPS = [
    # ...
    'example',
]
```

We allow "\*.vercel.app" subdomains in `ALLOWED_HOSTS`, in addition to 127.0.0.1:

```python
# vercel_app/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
```

The `wsgi` module must use a public variable named `app` to expose the WSGI application:

```python
# vercel_app/wsgi.py
app = get_wsgi_application()
```

The corresponding `WSGI_APPLICATION` setting is configured to use the `app` variable from the `vercel_app.wsgi` module:

```python
# vercel_app/settings.py
WSGI_APPLICATION = 'vercel_app.wsgi.app'
```

There are severals views in `example/views.py` which load HTML Django Templates `templates`:

The views are exposed a URL through `example/urls.py`:

```python
# example/urls.py
from django.urls import path

from example.views import index
from example.views import about
from example.views import me

urlpatterns = [
    path('', index),
    path('about', about),
    path('me', me),
]
```

Finally, it's made accessible to the Django server inside `vercel_app/urls.py`:

```python
# vercel_app/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('example.urls')),
]
```

This example uses the Web Server Gateway Interface (WSGI) with Django to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
python manage.py runserver
```
Your Django application is now available at `http://127.0.0.1:8000/`.

## The Admin Backend

The Admin Backend is using a MySQL Database for both Dev + Prod, but is able to use a SQLite for Dev

To connect to the MySQL DB install the Python package "pymysql" and the packeges from the requirements.txt

```bash
pip install -r requirements.txt
```
Create a Super User for the Admin Backend in the MySQL DB

```bash
py manage.py createsuperuser
```

Make the Migration to the MySQL DB

```bash
py manage.py makemigrations
py manage.py migrate
```

## Static files for the Admin Backend and the Frontend

Make sure that the Python package "whitenoise" is installed from the requirements.txt

Make sure you have the line "whitenoise.middleware.WhiteNoiseMiddleware" in the 

MIDDLEWARE = [] at the `vercel_app/settings.py` along with the other packages

Finally, it's made accessible to the Django server inside `vercel_app/settings.py`:

Note: This is needed for serving static files at Vercel - like the css for the Admin part

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR/'static' 

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" #dependency whitenoise

STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'assets')
]

After adding any static file, run the collectstatic command which will create folder: static/

```bash
py manage.py collectstatic
```

## Running Locally and take a look at the Admin Backend

```bash
python manage.py runserver
```
Your Django application is now available at `http://127.0.0.1:8000/admin`.
