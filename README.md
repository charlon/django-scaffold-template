{{ project_name }}
========================

Welcome to {{ project_name }}... 

Cras mattis consectetur purus sit amet fermentum. Nullam id dolor id nibh ultricies vehicula ut id elit. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Integer posuere erat a ante venenatis dapibus posuere velit aliquet. Donec ullamcorper nulla non metus auctor fringilla.

Install
-------

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



    
