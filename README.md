django-scaffold-template
========================

A Django project template for creating adaptive web applications. Based on previous adaptive-proj-template and adapting 2scoops of Django project structure.


Setup overview
----------------

* Virtual environments
* Project scaffold
* (Optional) Commit the virtualenv as a git repository


###Virtual environments

Make sure that virtualenv is installed. You may need to install nodeenv for running Node applications in a virtual container. For this project template, LessCSS is used and compiled server-side using Node. Install nodeenv if you don't want to install the LessCSS compiler globally.

**Virtualenv:**

    $ virtualenv {{repo_name}}
    $ cd {{repo_name}}
    $ source bin/activate

Note: I typically name my virtualenv the same as my repository in Github. This allows for consistency if collaborating with others or just having to clone the repo on another machine.

**Nodeenv:**

    $ pip install nodeenv
    $ nodeenv -p
    $ npm install less

**Django:**

    $ pip install django

###Project scaffold

**Start project**

    $ django-admin.py startproject --template=https://github.com/charlon/django-scaffold-template/archive/master.zip --extension=py,in,html {{project_name}}
    
**Install dependencies:**

    $ pip install -r requirements.txt
    $ python manage.py startapp {{app_name}}

**Run server:**

    $ python manage.py runserver --settings=settings.local
    
    
    
    
