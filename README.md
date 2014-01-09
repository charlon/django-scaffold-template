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

    $ virtualenv [repo_name]
    $ cd [repo_name]
    $ source bin/activate

Note: I typically name my virtualenv the same as my repository in Github. This allows for consistency if collaborating with others or just having to clone the repo on another machine.

**Nodeenv:**

    $ pip install nodeenv
    $ nodeenv -p
    $ npm install less

###Project scaffold

**Install Django:**

    $ pip install django
    
**Start project using template**

    $ django-admin.py startproject --template=https://github.com/charlon/django-scaffold-template/archive/master.zip --extension=py,in,html [project_name]
    
**Install dependencies:**

    $ cd [project_name]
    $ pip install -r requirements.txt

**Run server (depending on deploy location):**

    $ cd [project_name]
    $ python manage.py runserver --settings=[project_name].settings.local
    $ python manage.py runserver --settings=[project_name].settings.production

**Install apps**

    $ python manage.py startapp [app_name]
    
    
    
