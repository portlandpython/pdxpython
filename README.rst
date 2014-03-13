PDX Python Django Project
===========================

**Django project for the Portland Python User Group**

All are welcome to contribute, please follow the `issues <https://github.com/pdxpython/pdxpython/issues>`_ and submit a pull request.

Requirements
------------

**You'll need to have the following installed in your development environment.**

* `Python 2.7.X <http://www.python.org/download/releases/2.7.6/>`_
* `Virtualenv <http://www.virtualenv.org/en/latest/virtualenv.html#installation>`_
* `Grunt <http://gruntjs.com/>`_
* `Node.js <http://nodejs.org/>`_

Installation
------------

**Install by running:**

* git clone https://github.com/pdxpython/pdxpython.git
* cd pdxpython
* virtualenv --no-site-packages env
* source env/bin/activate
* pip install -r requirements/development.txt
* cp development.env.dist development.env
* Add your Meetup.com API Key to the development.env file. 
  You can obtain the key at `https://secure.meetup.com/meetup_api/key/ <https://secure.meetup.com/meetup_api/key/>`_.
  i.e. "export MEETUP_API_KEY=my-api-key"
* npm install
* grunt
* ./runserver

Then open your browser and visit `localhost:8000 <http://localhost:8000/>`_. You should see a list of upcoming events.

License
-------

The project is licensed under the BSD license.
