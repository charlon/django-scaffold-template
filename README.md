Your Project Name
=================

This README documents whatever steps are necessary to get your application up and running.

**Create your virtual environment**
    
    $ virtualenv projectenv
    $ cd projectenv
    
**Activating your virtualenv**

aasjdfasdf

    $ source bin/activate

**Install Node**

    Note: varies per platform

**Install Less**

    $ npm install less

**Clone repository:**
    
    $ git clone [[ repo_location ]] projectname.git

**Install dependencies:**

    $ cd projectname
    $ pip install -r requirements.txt

**Create local.py**
    
    $ cp projectname/settings/local_example.py projectname/settings/local.py
    
**Set environment variable for local settings into terminal:**

    $ export DJANGO_SETTINGS_MODULE=projectname.settings.local

**Update local.py settings**

    SECRET_KEY = ''

    
**Run server:**

    $ python manage.py runserver 0.0.0.0:8000
