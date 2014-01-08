django-scaffold-template
========================

A Django project template for creating adaptive web applications. Based on previous adaptive-proj-template and adapting 2scoops of Django project structure.


Setup overview
----------------

* Virtual environments
* Project scaffold
* (Optional) Commit the virtualenv as a git repository


###Virtual environments

Make sure that virtualenv is installed. You may optionally install nodeenv as a container for running Node applications. For this project template, LessCSS is used and compiled server-side using Node.

Virtualenv:

    $ virtualenv {{env_name}}
    $ cd {{env_name}}
    $ source bin/activate

Nodeenv:

    $ pip install nodeenv
    $ nodeenv -p
    $ npm install less

Django:

    $ pip install django

###Project scaffold

Start project

    $ django-admin.py startproject --template=https://github.com/charlon/django-scaffold-template/archive/master.zip --extension=py,in,html {{project_name}}
    
Install dependencies:

    $ pip install -r requirements.txt
    $ python manage.py startapp {{app_name}}

Run server:

    $ python manage.py runserver --settings=settings.local
    
    
    
    
