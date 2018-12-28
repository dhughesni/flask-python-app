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
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip freeze > requirements.txt
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ export FLASK_APP=run_app.py
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
```
set up via setup_custom_logger in log.py
- In app.py:
  import log
  LOG = log.setup_custom_logger('root')
- In subModules:
  import logging
  LOG = logging.getLogger('root')
```
...
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install pytest-flask
```
- https://pytest-flask.readthedocs.io/en/latest/index.html
```
