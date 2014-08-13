{{ project_name }}
===========

This README documents whatever steps are necessary to get your application up and running.

**Create your virtual environment**
    
    $ virtualenv [env-name]
    $ cd env-name

**Install Less**

    $ npm install less

**Clone repository:**
    
    $ git clone git@bitbucket.org:charlonpalacay/chunky.git

**Install dependencies:**

    $ cd chunky
    $ pip install -r requirements.txt

**Set environment variable for local settings into terminal:**

    $ export DJANGO_SETTINGS_MODULE=chunky.settings.local

**Run server:**

    $ python manage.py runserver 0.0.0.0:8000
