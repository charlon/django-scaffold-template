django-scaffold-template
========================

A Django project template for creating adaptive web applications. Based on previous adaptive-proj-template and adapting 2scoops of Django project structure.


Install overview
----------------

* Setup virtualenv
* Install django
* Setup Django project and dependencies
* (Optional) Commit the virtualenv as a git repository


###Setup virtualenv

    $ virtualenv {{env_name}}
    $ cd {{env_name}}

###Install Django

    $ pip install django

###Setup Django project and dependencies

    $ django-admin.py startproject --template=https://github.com/charlon/django-scaffold-template/archive/master.zip --extension=py,in,html {{project_name}}
    $ pip install -r requirements.txt
    $ python manage.py startapp {{app_name}}


###Run server

    $ python manage.py runserver --settings=settings.local
    
    
    
    
