

# Django + MySQL + Vercel

This example shows how to use Django 4 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

Last updated: 04-05-2025

Node version selected at Vercel Cloud: 22

## Demo at Vercel

https://django-starter-two.vercel.app/

## Installing

- Download Python from the official website [Python](https://python.org/)
- Make sure that you have installed Python and Django by the commands in Powershell: "python --version"
- Download the Python extension for Visual Studio Code which automatically include the Pylance extionsion
- Download / fork this Django Starter Web App from my GitHub
- Create the virtual envirement ".venv" for the Django Web App by Powershell or by VS Code
- Virtual Enviroment by VS Code: "View - Command Palette - Python Create Enviroment"


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

This Django example uses the Web Server Gateway Interface (WSGI) with Django to enable handling requests on Vercel with Serverless Functions.

## Routing 

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

## Templates

To use templates create the dir 'templates' at root level and put the HTML files there

There is only one Django App in the Project and the dir 'templates' can be at root level

Tell Django where to look for Templates by `example/settings.py`:

Find the section TEMPLATES = [] and add the dir of the Templates

'DIRS': [BASE_DIR / 'templates']

## Running Locally

```bash
python manage.py runserver
```
Your Django application is now available at `http://127.0.0.1:8000/`.

## The Admin Backend and Databases

The Admin Backend is using a MySQL Database for both Dev + Prod, but is able to use a SQLite for Dev

To connect to the MySQL DB install the Python package "pymysql" and the packeges from the requirements.txt

```bash
pip install -r requirements.txt
```

Take a look at the files needed for connect to MySQL: `vercel_app/mysql_setup.py` and 

`vercel_app/__init__.py`

Create a Super User for the Admin Backend in the MySQL DB

```bash
py manage.py createsuperuser
```

Make the Migration to the MySQL DB

```bash
py manage.py makemigrations
py manage.py migrate
```
You will need to do the Migration at first and when / if you will add, update or delete models.py which this Django Web App does not use

For using a SQLite developing / locally make the config in the setting file `vercel_app/settings.py`

Find the section DATABASES = {} and add support for SQLite and comment out the MySQL

## Static files for the Admin Backend and the Frontend

There is only one Django App in the Project and the dir 'static' and 'assets' are at root level

Make sure that the Python package "whitenoise" is installed from the requirements.txt

Note: Make sure you have the line "whitenoise.middleware.WhiteNoiseMiddleware" in the 

MIDDLEWARE = [] at the `vercel_app/settings.py` along with the other packages

Finally, it's made accessible to the Django server inside `vercel_app/settings.py`:

Note: This is needed for serving static files at Vercel - like the CSS for the Admin part

Where Django looks for the static files

STATIC_URL = 'static/'

Where you put your static files 'static' = 'static ' ( Need to match the above )

STATIC_ROOT = BASE_DIR/'static' 

## Additional directory from which to load static files if wanted

The files in the dir 'asset' will be copied to the dir 'static' after running

```bash
py manage.py collectstatic
```

STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'assets')
]

After adding any static file, run the collectstatic command which will create folder: static/

```bash
py manage.py collectstatic
```
## Check that Django is serving Static files by URL

Type the URL in your Browser after deployment to Vercel

https:// your project at vercel.app/static/pso-django.jpg

or they the URL when running locally

`http://127.0.0.1:8000/static/pso-django.jpg`

If everything is fine my photo will be displayed

Working with CSS files will be the same by added CSS files to the dir "static"

Now you can use images and css in your Templates

## Running Locally and take a look at the Admin Backend

```bash
python manage.py runserver
```

The Django application is now available at `http://127.0.0.1:8000/admin`

## Deployment to Vercel

Make sure that your satic files are ready by running

```bash
py manage.py collectstatic
```

Take a look at the file `vercel.json`

Make sure to set Debug = False in the file `vercel_app/settings.py`

Make a commit to your GitHub and your Django will build and deploy

Happy use of Django :-)
