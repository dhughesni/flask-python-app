```
dhughes@Daryls-MacBook-Pro:~/Developer$ mkdir flask-python-app
dhughes@Daryls-MacBook-Pro:~/Developer$ cd flask-python-app/
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ git init
Initialized empty Git repository in /Users/dhughes/Developer/flask-python-app/.git/
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch README.md
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ virtualenv venv
New python executable in /Users/dhughes/Developer/flask-python-app/venv/bin/python2.7
Also creating executable in /Users/dhughes/Developer/flask-python-app/venv/bin/python
Installing setuptools, pip, wheel...done.
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ ls
README.md  venv/
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ source venv/bin/activate
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ mkdir flaskPythonApp
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch run_app.py
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch flaskPythonApp/__init__.py
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install flask
..
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip freeze > requirements.txt #pip install -e .
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ export FLASK_APP=app.py
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ flask run
...
...More Dev
...
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ flask routes
Endpoint  Methods  Rule
--------  -------  -----------------------
static    GET      /static/<path:filename>
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ mv run_app.py flaskPythonApp/app.py
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ export FLASK_APP=app.py
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ mkdir api
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ touch api/__init__.py
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ touch api/views.py
...
Added blueprints
...
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ export FLASK_ENV=development
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ pip install uuid
...
Added logging
set up via setup_custom_logger in log.py
- In app.py:
  import log
  LOG = log.setup_custom_logger('root')
- In subModules:
  import logging
  LOG = logging.getLogger('root')
...
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install pytest-flask
https://pytest-flask.readthedocs.io/en/latest/index.html
...
...Add setup.py: http://flask.pocoo.org/docs/1.0/tutorial/install/
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch setup.py
Adding cli as seperate file as it is easier to maintain
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch flaskPythonApp/cli.py
...Now works (venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install -e .
Obtaining file:///Users/dhughes/Developer/flask-python-app
Installing collected packages: flaskPythonApp
  Found existing installation: flaskPythonApp 0.0.1
    Uninstalling flaskPythonApp-0.0.1:
      Successfully uninstalled flaskPythonApp-0.0.1
  Running setup.py develop for flaskPythonApp
Successfully installed flaskPythonApp
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ flaskPythonApp
Usage: flaskPythonApp [OPTIONS] COMMAND [ARGS]...

  Management script for the flaskPythonApp

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  init    Initialize application
  routes  Show the routes for the app.
  run     Runs a development server.
  shell   Runs a shell in the app context.
  test    Test a print

...Added coverage for pytests
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install pytest coverage
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ coverage run -m pytest # run coverage
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ coverage report # view report

```
