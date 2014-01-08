django-scaffold-template
========================

A Django project template for creating adaptive web applications. Based on previous adaptive-proj-template and adapting 2scoops of Django project structure.


Install overview
----------------

* Setup environment
* Install django
* Setup Django project and dependencies
* (Optional) Commit the virtualenv as a git repository


###Setup environment

Make sure that virtualenv is installed. You may optionally install nodeenv as a container for running Node applications. For this project template, LessCSS is used and compiled server-side using Node.

Virtualenv:

    $ virtualenv {{env_name}}
    $ cd {{env_name}}
    $ source bin/activate

Nodeenv:

    $ pip install nodeenv
    $ nodeenv -p
    $ npm install less

###Install Django

    $ pip install django

###Setup Django project and dependencies

    $ django-admin.py startproject --template=https://github.com/charlon/django-scaffold-template/archive/master.zip --extension=py,in,html {{project_name}}
    $ pip install -r requirements.txt
    $ python manage.py startapp {{app_name}}


###Run server

    $ python manage.py runserver --settings=settings.local
    
    
    
    
