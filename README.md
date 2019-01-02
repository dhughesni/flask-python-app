TO-DO:
-
# Flask App Setup
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
# Docker App setup
```
- Check the status
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube status
There is a newer version of minikube available (v0.32.0).  Download it here:
https://github.com/kubernetes/minikube/releases/tag/v0.32.0

To disable this notification, run the following:
minikube config set WantUpdateNotification false
minikube: Stopped
cluster:
kubectl:
E1231 11:13:42.168028    1486 env.go:330] Error setting machine env variable(s): Error getting ip from host: Host is not running
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube start --memory 8192 --cpus 6
Starting local Kubernetes v1.10.0 cluster...
Starting VM...
Getting VM IP address...
Moving files into cluster...
Setting up certs...
Connecting to cluster...
Setting up kubeconfig...
Starting cluster components...
E1231 11:26:06.851720    1507 start.go:305] Error restarting cluster:  restarting kube-proxy: waiting for kube-proxy to be up for configmap update: timed out waiting for the condition
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ eval $(minikube docker-env)
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube status
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100
... Make docker file
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch Dockerfile
.. added .dockerignore
..Make docker image
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker build -t flask-python-app:v0.0.1 . # or docker build -t flask-python-app . <-- to tag as latest
Sending build context to Docker daemon  26.48MB
Step 1/5 : FROM python:3
 ---> db1c801f1c06
Step 2/5 : COPY . .
 ---> Using cache
 ---> 328e268bbda9
Step 3/5 : RUN pip install -e .
 ---> Using cache
 ---> f9ab1e690d66
Step 4/5 : EXPOSE 5000
 ---> Using cache
 ---> 48ddf2d3be2c
Step 5/5 : CMD [ "CMD", "flaskPythonApp run" ]
 ---> Using cache
 ---> e0ce1bff3141
Successfully built e0ce1bff3141
Successfully tagged flask-python-app:v0.0.1
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker images
REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
flask-python-app                           v0.0.1              e0ce1bff3141        33 seconds ago      957MB

... Lets try run the docker image before deploying into helm using: docker run image_name:tag_name
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker run -it flask-python-app

.. To enter docker image as bash
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker run -it flask-python-app /bin/bash


```
