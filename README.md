django-scaffold-template
========================

A Django project template for creating adaptive web applications. Based on previous adaptive-proj-template and adapting 2scoops of Django project structure.


Install overview
----------------

* Setup virtualenv
* Install django
* Create Django project
* Install dependencies
* Create an app
* (Optional) Commit the virtualenv as a git repository


###Setup virtualenv

    $ virtualenv {{env_name}}
    $ cd {{env_name}}

###Install Django

    $ pip install django

###Create your project

    $ django-admin.py startproject --template=https://github.com/charlon/django-scaffold-template/archive/master.zip --extension=py,in,html {{project_name}}
    
###Install dependencies
    
    $ pip install -r requirements.txt
    
    
