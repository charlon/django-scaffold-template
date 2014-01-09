django-scaffold-template
========================

A Django project template for creating adaptive web applications. Based on previous adaptive-proj-template and adapting 2scoops of Django project structure.


Setup
-----

* Virtual environments
* Project scaffold
* Version control


###Virtual environments

Make sure that virtualenv is installed. You may need to install nodeenv for running Node applications in a virtual container. For this project template, LessCSS is used and compiled server-side using Node. Install nodeenv if you don't want to install the LessCSS compiler globally.

**Virtualenv:**

    $ virtualenv [repo-name]
    $ cd [repo-name]
    $ source bin/activate

Note: I typically name my virtualenv the same as my repository in Github. This allows for consistency if collaborating with others or just having to clone the repo on another machine.

**Nodeenv:**

    $ pip install nodeenv
    $ nodeenv -p
    $ npm install less

###Project scaffold

Concepts: Adaptive design, mobile-first, RESS, responsive web design - whatever you want to call it!
Includes: Bootstrap3/Normalize, Django Compressor, MobileESP, LessCSS

**Install Django:**

    $ pip install django
    
**Start project using template**

    $ django-admin.py startproject --template=https://github.com/charlon/django-scaffold-template/archive/master.zip --extension=py,in,html [project_name]
    
**Install dependencies:**

    $ cd [project_name]
    $ pip install -r requirements.txt

**Run server (using local settings):**

    $ cd [project_name]
    $ python manage.py runserver --settings=[project_name].settings.local 0.0.0.0:8000

At this point, you may want to start version controlling your project (see Version Control).

**Install apps**

    $ python manage.py startapp [app_name]
    
###Version control

First, create an empty Github remote repository.

**Initialize local repository**

    $ cd [repo-name]
    $ git init
    $ git remote add origin https://github.com/[gitusername]/[git-repo-name].git
    $ git pull origin master
    
**Add project to Github**

    $ git add [project_name]
    $ git commit -m "Initial Django project commit."
    $ git push -u origin master


Collaboration
-------------

Collaborating on a project is easy as cloning the repository you just created and turning it into a virtualenv.

**Clone repository**

    $ git clone [github-repo-url]
    
**Virtualenv:**

    $ virtualenv [repo-name]
    $ cd [repo-name]
    $ source bin/activate
    
**Nodeenv:**

    $ pip install nodeenv
    $ nodeenv -p
    $ npm install less
    
**Project**

    $ cd [project_name]
    $ pip install -r requirements.txt
    
