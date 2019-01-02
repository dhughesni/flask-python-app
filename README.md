
# Dev setup

```
- set up virtual env
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ virtualenv venv
- activate virtual env
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ source venv/bin/activate
- install requirements
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install -r requirements.txt
- install flaskPythonApp module
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install .
- run the app
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ flaskPythonApp run
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ...
```

# Build Steps
```
- Build Docker image
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker build -t flask-python-app .
- Install Chart
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ helm install helm
- Test Chart
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ helm test <DEPLOYED-CHART-NAME>
```

# Flask App Setup

```
- make project dir
dhughes@Daryls-MacBook-Pro:~/Developer$ mkdir flask-python-app
dhughes@Daryls-MacBook-Pro:~/Developer$ cd flask-python-app/
- initialize as git repo
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ git init
Initialized empty Git repository in /Users/dhughes/Developer/flask-python-app/.git/
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch README.md
- install virtual env for local development
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ virtualenv venv
New python executable in /Users/dhughes/Developer/flask-python-app/venv/bin/python2.7
Also creating executable in /Users/dhughes/Developer/flask-python-app/venv/bin/python
Installing setuptools, pip, wheel...done.
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ ls
README.md  venv/
- start venv and begin development of project
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ source venv/bin/activate
- set up python module
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ mkdir flaskPythonApp
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch flaskPythonApp/app.py # add basic flask endpoint
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch flaskPythonApp/__init__.py
- install Flask
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install flask
- freeze requirements.txt
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip freeze > requirements.txt
- run basic Flask App
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ export FLASK_APP=flaskPythonApp/app.py
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ flask run
- check the routes
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ flask routes
Endpoint  Methods  Rule
--------  -------  -----------------------
static    GET      /static/<path:filename>
...Test out the app
- add uuidAPI
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ mkdir uuidApi
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ touch uuidApi/__init__.py
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ touch uuidApi/views.py
...
- added blueprints
...
- install python uuid module
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app/flaskPythonApp$ pip install uuid
...
 - added logging
set up via setup_custom_logger in log.py
- In app.py:
  import log
  LOG = log.setup_custom_logger('root')
- In subModules:
  import logging
  LOG = logging.getLogger('root')
...
- added pytest-flask module: https://pytest-flask.readthedocs.io/en/latest/index.html
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install pytest-flask
...
- Add setup.py: http://flask.pocoo.org/docs/1.0/tutorial/install/
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch setup.py
...Adding cli as separate file as it is easier to maintain
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch flaskPythonApp/cli.py
- install flaskPythonApp module
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
...
- Added coverage for pytests
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ pip install pytest coverage
- run coverage
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ coverage run -m pytest
- view report
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ coverage report # view report
```

# Docker App setup

```
- Check minikube status
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube status
...
minikube: Stopped
cluster:
kubectl:
E1231 11:13:42.168028    1486 env.go:330] Error setting machine env variable(s): Error getting ip from host: Host is not running
- start Minikube
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
- set docker env to point to minikube
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ eval $(minikube docker-env)
- check minikube status
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube status
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100
- Make docker file
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch Dockerfile
- added .dockerignore
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch .dockerignore
- added docker-entrypoint.sh
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ touch docker-entrypoint.sh
- Build docker image as latest
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker build -t flask-python-app .
Sending build context to Docker daemon  146.4kB
Step 1/4 : FROM python:3
 ---> db1c801f1c06
Step 2/4 : EXPOSE 5000
 ---> Using cache
 ---> 870c11fdfc1b
Step 3/4 : COPY . .
 ---> 441d6235275a
Step 4/4 : ENTRYPOINT ["/docker-entrypoint.sh"]
 ---> Running in d0b926022a67
Removing intermediate container d0b926022a67
 ---> f2866c0d57e7
Successfully built f2866c0d57e7
Successfully tagged flask-python-app:latest
- check docker image
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker images
REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
flask-python-app                           latest              f2866c0d57e7        29 seconds ago      927MB
...
- Try run the docker image before deploying into helm using: docker run image_name:tag_name
.. To enter docker image as bash and to expose the running port
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker run -p 5000:5000 -it flask-python-app /bin/bash
...
- test app is running "MINKUBE-HOST:5000"
.. app is running on minikube, first get
dhughes@Daryls-MacBook-Pro:~$ echo $(minikube ip)
192.168.99.100
dhughes@Daryls-MacBook-Pro:~$ curl http://192.168.99.100:5000
App is running!
```

# Run in Minikube via kubectl
```
- clean minikube env
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube delete
Deleting local Kubernetes cluster...
Machine deleted.
- check status
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube status
minikube:
cluster:
kubectl:
- start minikube
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube start --memory 8192 --cpus 6
Starting local Kubernetes v1.10.0 cluster...
Starting VM...
...
- open minikube dashboard
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube dashboard
Opening kubernetes dashboard in default browser...
- set docker env to point to minikube
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ eval $(minikube docker-env)
- Build Docker image
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker build -t flask-python-app .
- check docker image built
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ docker images
REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
flask-python-app                           latest              734f026dd452        3 seconds ago       927MB
- Create deployment
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ kubectl run flask-python-app --image=flask-python-app:latest --port=5000 --image-pull-policy=Never
deployment.apps/flask-python-app created
- Create Service
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ kubectl expose deployment flask-python-app --type=LoadBalancer
service/flask-python-app exposed
- check service is running
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ kubectl get services
NAME               TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
flask-python-app   LoadBalancer   10.97.51.79   <pending>     5000:32352/TCP   29s
kubernetes         ClusterIP      10.96.0.1     <none>        443/TCP          10m
- get host-port of running service
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ minikube -n default service list
|-----------|------------------|-----------------------------|
| NAMESPACE |       NAME       |             URL             |
|-----------|------------------|-----------------------------|
| default   | flask-python-app | http://192.168.99.100:32352 |
| default   | kubernetes       | No node port                |
|-----------|------------------|-----------------------------|

```

# Use Helm to deploy as Chart

```
- Ref: https://docs.helm.sh/using_helm/#quickstart

- check kubectl context is set to minikube
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ kubectl config current-context
minikube
- Run helm init
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ helm init
$HELM_HOME has been configured at /Users/dhughes/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
To prevent this, run `helm init` with the --tiller-tls-verify flag.
For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
Happy Helming!

... set up simple chart: https://tech.paulcz.net/blog/getting-started-with-helm/
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ kubectl run flask-python-app --image=flask-python-app:latest --port=5000 --image-pull-policy=Never -o yaml > manifests/deployment.yaml
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ kubectl expose deployment flask-python-app --type=LoadBalancer -o yaml > manifests/service.yaml
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ kubectl delete -f manifests
deployment.apps "flask-python-app" deleted
service "flask-python-app" deleted
- Create the basic chart directory
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ helm create helm
Creating helm  
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ cp manifests/* helm/templates/
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ rm helm/templates/ingress.yaml
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ rm helm/templates/NOTES.txt
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ helm install -n my-first-helm-chart helm
NAME:   my-first-helm-chart
LAST DEPLOYED: Wed Jan  2 14:02:07 2019
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Service
NAME              TYPE          CLUSTER-IP      EXTERNAL-IP  PORT(S)         AGE
flask-python-app  LoadBalancer  10.104.222.102  <pending>    5000:31824/TCP  1s

==> v1beta1/Deployment
NAME              DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
flask-python-app  1        0        0           0          1s

==> v1/Pod(related)
NAME                               READY  STATUS   RESTARTS  AGE
flask-python-app-699755cdf5-jdr4n  0/1    Pending  0         0s
```

# Basic Helm test

```
dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ helm install -n test-helm-chart helm
NAME:   test-helm-chart
LAST DEPLOYED: Wed Jan  2 16:45:45 2019
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1beta1/Deployment
NAME              DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
flask-python-app  1        0        0           0          1s

==> v1/Pod(related)
NAME                               READY  STATUS             RESTARTS  AGE
flask-python-app-699755cdf5-5gcvf  1/1    Terminating        0         39m
flask-python-app-699755cdf5-d52wk  0/1    ContainerCreating  0         1s

==> v1/Service
NAME              TYPE          CLUSTER-IP      EXTERNAL-IP  PORT(S)         AGE
flask-python-app  LoadBalancer  10.104.222.102  <pending>    5000:31824/TCP  1s


dhughes@Daryls-MacBook-Pro:~/Developer/flask-python-app$ helm test test-helm-chart --debug --cleanup
[debug] Created tunnel using local port: '58107'

[debug] SERVER: "127.0.0.1:58107"

RUNNING: test-helm-chart-service-test
PASSED: test-helm-chart-service-test
```
