{{ project_name }}
========================

{{ project_name }} is a Django project created using adaptive web application concepts. The base template uses previous adaptive-proj-template and adapting 2scoops of Django project structure.

**Clone {{ project_name }}**

    $ git clone [github-repository-url]

Turn the cloned repository into a virtual environment

**Virtualenv:**

    $ virtualenv [repo-name]
    $ cd [repo-name]
    $ source bin/activate

**Nodeenv:**

    $ pip install nodeenv
    $ nodeenv -p
    $ npm install less

**Install project dependencies:**

    $ cd [project_name]
    $ pip install -r requirements.txt

**Run server (using local settings):**

    $ cd [project_name]
    $ python manage.py runserver --settings=[project_name].settings.local 0.0.0.0:8000



    
