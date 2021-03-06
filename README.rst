PDX Python Django Project
===========================

**Django project for the Portland Python User Group**

All are welcome to contribute, please follow the `issues <https://github.com/pdxpython/pdxpython/issues>`_ and submit a pull request.

Requirements
------------

**You'll need to have the following installed in your development environment.**

* `Python 2.7.x <http://www.python.org/download/releases/2.7.6/>`_
* `Virtualenv <http://www.virtualenv.org/en/latest/virtualenv.html#installation>`_
* `Node.js <http://nodejs.org/>`_
* `Grunt.js <http://gruntjs.com/>`_

Installation
------------

**Install by running:**

.. code-block:: bash

    $ git clone https://github.com/pdxpython/pdxpython.git
    $ cd pdxpython
    $ virtualenv --no-site-packages venv
    $ source venv/bin/activate
    $ pip install -r requirements/development.txt
    $ cp development.env.dist development.env

Add your Meetup.com API Key to the development.env file. i.e. "export MEETUP_API_KEY=my-api-key" 
You can obtain your key at `https://secure.meetup.com/meetup_api/key/ <https://secure.meetup.com/meetup_api/key/>`_.

.. code-block:: bash

    $ source development.env
    $ python pdxpython/manage.py syncdb
    $ npm install
    $ grunt
    $ ./runserver.sh

Then open a browser and visit `localhost:8000 <http://localhost:8000/>`_. You should see a list of upcoming events.

License
-------

The project is licensed under the BSD license.
