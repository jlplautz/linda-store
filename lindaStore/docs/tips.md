## Comandos iniciais
```python
git clone git@github.com:jlplautz/linda-store.git
cd linda-store
poetry init
pyenv local 3.12.0
poetry shell
poetry env info
```

## issue#1
```python
git checkout -b issue#1
source .venv/bin/activate
pip list
python3.12 -m ensurepip --upgrade
pip list
source .venv/bin/activate
deactivate
pip list
poetry env info
poetry add django
mng runserver 
django-admin startproject lindaStore .
source .venv/bin/activate
django-admin startproject lindaStore .
mng runserver 
git push -u origin issue#1
git status
git add .python-version
git add poetry.lock pyproject.toml
git add lindaStore/
git status
git add manage.py
git commit -m 'build(issue#1): Instalado Django e criado projeto ore.'
git push -u origin issue#1
git checkout main
git pull origin main
git branch
git branch -D issue#1 
```

## issue#2
```python
git checkout -b issue#2 
django-admin startapp shop
django-admin
ls -la
cd lindaStore
django-admin startapp shop
git status
git add shop/
git add settings.py
git status
git commit -m 'build(issue#2): Criado app shop e criado models e Product.'
git push -u origin issue#2
git checkout main
git pull origin main
git diff
```

## issue#4
```python
git checkout -b issue#4
poetry add pillow
mng showmigrations
mng makemigrations
git status
git add shop/
git add poetry.lock pyproject.toml
git status
git add poetry.lock pyproject.toml
git add ../poetry.lock ../pyproject.toml
git status
git commit -m 'build(issue#4): Instaldo biblioteca Pillow e do as migrações.'
git push -u origin issue#4
git checkout main
git pull origin main
```

## issue#6
```python
git checkout -b issue#6
mng createsuperuser
django-admin 
mng createsuperuser 
mng migrate
mng createsuperuser 
mng runserver 
git status
git add shop/
git status
git products/
git add products/
mng runserver 
git status
mng runserver 
git status
git add products/
git status
mng runserver 
git status
git commit -m 'build(issue#6): Criado catalodo para site admin e superuser.'
git push -u origin issue#6
git checkout main
git pull origin main
```

## issue#9
```python
git checkout -b issue#9
mng runserver 
git status
mng runserver 
git status
git add shop/
git status
git add produtcs/
git status
git add ../cafe-arabica.jpg
git add ../cha-mate.png
git add ../media/
git status
git add suco-uva.jpeg
git status
git commit -m 'build(issue#9): Criado catalodo de produtos na ra listar e fazer filtro.'
git push -u origin issue#9
git checkout main
git pull origin main
```

## issue#11
```python
git checkout -b issue#11
cd lindaStore
mng startapp carrinho
mng runserver 
git status
git add carrinho/
git status
git add settings  
git status
git add delete
git add deleted:    products/2024/03/15/cafe-arabica.jpg
git add/rm products/2024/03/15/cafe-arabica.jpg
git rm products/2024/03/15/cafe-arabica.jpg
git rm products/2024/03/15/cafe-arabica_3xfFwvM.jpg
git rm products/2024/03/15/cha-mate.png
git status
git rm suco-uva.jpeg
git status
git rm ../cafe-arabica.jpg
git rm ../cha-mate.png
git status
git restore settings.py
git restore urls.py
git status
git commit -m 'build(issue#11): Criado app Carrinho e ntado views, forms, carrinho.py.'
git push -u origin issue#11
git checkout main
git pull origin main
git status
```

## issue#13
```python
git checkout issue#13
mng runserver 
git status
git add lindaStore/
git status
git commit -m 'build(issue#13): Adicinado função ao carrinho + processador de ontexto.'
git push -u origin issue#13
git checkout main
git pull origin main
git diff
git branch
mng runserver 
git status
```

## issue#15
```python
git checkout -b issue#15
poetry add --group dev pytest pytest-cov taskipy blue isort
task -l
task lint
task format
poetry add --group dev ruff
task lint
task test
poetry show --tree
task test
pytest -s -x --cov=lindaStore -vv
pytest
task test
pytest -s -x --cov=lindaStore -vv
task test
pytest -s -x --cov=lindaStore -vv
pytest
pytest --cov=lindaStore -vv
task test
task lint
poetry add poetry.lock
git add pyproject.toml poetry.lock
poetry add poetry.lock
git status
poetry add manage.py
poetry remove manage.py
git status
git restore pyproject.toml
git add manage.py
git status
git commit -m 'build(issue#15): Adicionado libs taskipy, blue, isort, ruff, pytest, -cov.'
git push -u origin issue#15
git checkout main
git pull origin main
```

## issue#16
```python
git status
git checkout -b issue#16
cd linda-store
cd lindaStore
mng startapp orders
mng makemigrations
mng migrate
mng runserver 
task lint
mng runserver 
task lint
task format
task lint
task test
git status
git add orders/
task test
git status
git add carrinho/
git status
git add urls.py
git add settings.py
git status
git commit -m 'build(issue#16): Registrado o pedido do cliente.'
git push -u origin issue#16
git checkout main
git pull origin main
git diff
```

## issue#19
```python
git checkout -b issue#19
poetry add celery
apt-get install rabbitmq
sudo apt-get install rabbitmq
rabbitmq-server
cd 
df -kh
apt-get install rabbitmq
su -
apt-get install rabbitmq
rabbitmq-server 
bash
exit()\n\ncd
rabbitmq-server
poetry add celery
celery -h
celery --help
celery -A myshop worker -l info
celery -A lindaStore worker -l info
mng runserver 
docker run --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
mng runserver 
celery -A lindaStore worker -l info
mng runserver 
celery -A lindaStore worker -l info
celery --help
celery list
celery shell
celery status
celery result
celery result Task_ID
celery result --help
celery result -t
celery result -t 7
celery result -t 9
celery result -t TASK_ID=9
celery report
celery list --help
celery list 
celery list binding
poetry add flower
celery -A lindaStore flower
mng runserver 
celery -A lindaStore flower
mng runserver 
su -
celery -A lindaStore flower
celery -A lindaStore worker -l info
mng runserver 
mng runserver 8001
mng runserver 
celery -A lindaStore flower
mng runserver 
celery -A lindaStore flower
cd 
cd Proj_2024/
code .
history
celery -A lindaStore worker -l info
celery -A lindaStore flower
mng runserver 
celery -A lindaStore worker -l info
celery
celery list
celery -A lindaStore flower
pwd
docker run --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
docker ps
docker ps -a
celery list
celery -A lindaStore flower
cd ..
celery -A lindaStore flower
ls -la
cd lindaStore
ls -la
celery -A lindaStore flower
cd ..
celery -A lindaStore flower
mng runserver 
celery -A lindaStore flower
cd lindaStore
celery -A lindaStore flower
source .venv/bin/activate
cd ..
source .venv/bin/activate
celery -A lindaStore flower
bash
celery -A lindaStore worker -l info
cd ;;
cd 
cd Proj_2024/linda-store
code .
celery -A lindaStore worker -l info
docker ps -a
docker conttainer ls
docker container ls
docker rm 668
docker rm 5d7
docker rm 9ee
docker container ls
docker ps -a
docker rm 2dd
docker rm 4492dd
docker rm 449
docker rm c48
docker ps -a
docker rm 06e
docker rm db6
docker rm a51
docker ps -a
docker rm b92 4a5 a51
docker rm b92 4a5
docker rm 4a5
docker ps -a
docker ps 051-a
docker ps 051
docker ps -a
docker rm 051
docker rm 747
docker ps -a
docker run --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
celery -A lindaStore worker -l info
source .venv/bin/activate
celery -A lindaStore worker -l info
docker container ls
ping 172.17.0.2
ssh guest@172.17.0.2
telnet localhost 5672
dir
ssh guest@172.17.0.2
ftp guest:172;17;02
ftp guest:172.17.0.2
ftp guest@172.17.0.2
ssh 172.17.0.2 port:5672
celery -A myshop flower
celery -A lindaStore flower
docker container ls
docker ps -a
docker rm 649
docker ps -a
docker run --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
mng runserver 
source .venv/bin/activate
celery -A lindaStore flower
docker container ls
docker ps
docker ps -a
docker rm 642
docker --version
docker run --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
docker container ls
docker ps -a
docker rm 5ef
docker container ls
poetry install
docker run --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq
docker container ls
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
docker ps -a
docker rm 6c7
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
mng runserver 
celery -A lindaStore flower
mng createsuperuser 
docker container ls
docker ps
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
celery -A lindaStore flower
celery -A lindaStore flower
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
mng runserver 
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
celery -A lindaStore flower
mng runserver 
celery --help
celery inspect
celery inspect conf
clear
docker ps
docker ps -a
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
celery -A lindaStore flower
docker ps -
docker ps -a
mng runserver 
poetry env info
poetry show --tree
task lint
task format
task lint
task test
git status
git add lindaStore/celery.py
git add lindaStore/docs/
git add lindaStore/orders/
git status
git add lindaStore/__init__.py
git add lindaStore/settings.py
git add lindaStore/urls.py
git add poetry.lock pyproject.toml
git status
git commit -m 'build(issue#19): Implementadp tarefas assincronas com Celery, mas email não foi enviado.'
git push -u origin issue#19
git checkout main
```python

git pull origin main
docker compose up --build -d 
poetry remove celery flower
poetry remove flower
poetry remove celery
docker compose up --build -d 
docker container ls
docker stop 4e2
docker rm 4e2
docker compose up --build -d 
docker container ls
docker ps
docker -f rm c03
docker stop 4e2
docker ps
docker stop c03
docker rm c03
docker compose build
docker ps -a
docker compose up
docker compose build
docker compose up
poetry show --tree
which python
python
pip list
deactivate
source .venv/bin/activate
pip list
deactivate
poetry shell
cd ..
cd lindaStore
ls -la
cd linda-store
ls -la
rm -rf .venv
ls -la
sudo rm -rf .venv
poetry run gunicorn --help
pyenv local
docker compose build
docker compose up
docker ps -a
docker compose up
docker compose down -v
docker compose build
docker compose down -v
docker compose build
docker container ls
docker ps -a
docker ps 
docker ps -a
docker compose up
docker images
docker ps -a
poetry add watchfiles
docker compose down -v
docker image prune
docker images
docker image rm -f 0ba ac1 fdf
docker images
docker image rm -f d67 669 a99 d36 478
docker images
docker compose build
docker compose up
docker compose down -v
docker compose build
docker compose up
git stach
```
## issue#21
```python
git checkout -b issue#21
git stach pop
git checkout main
mng runserver 
poetry shell
exit90
mng runserver 
deactivate
poetry shell
ls -la
pip list
deactivate
source .venv/bin/activate
pip list
deactivate
ls -la
sudo rm -rf .venv
poetry install
which python
pyenv local
python
ls -la
cat .python-version
deactivate
python
pyenv local
ls -la
sudo rm -rf .venv
ls -la
poetry install --help
poetry install --sync
poetry install
poetry shell
emulate bash -c '. /home/plautz/Proj_2024/linda-store/.venv/bin/activate'
poetry show --tree
pip list
mng runserver 
docker compose down -v
docker compose buid
docker compose build
docker compose up
docker container ls
docker compose down -v
deactivate
sudo rm -rf .venv
pyenv local 3.11.0
pyenv local
poetry lock
poetry install --sync
poetry shell
poetry env info
poetry show --tree
docker compose build
docker compose up
source .venv/bin/activate
poetry run gunicorn --help
gunicorn
gunicorn --bind port:8000 lindaStore.wsgi
gunicorn --bind :8000 lindaStore.wsgi
gunicorn --help
docker compose down -v
docker compose build
docker compose up
docker compose down -v
docker compose up --build -d 
docker container ls
docker compose down -v
deactivate
docker compose down -v
docker ps -a
docker ps
git status
poetry add celery 
poetry shell
poetry show --tree
deactivate
poetry show --tree
poetry shell
sudo rm -rf .venv
pyent
pyenv local
poetry install --sync
poetry install
poetry shell
source .venv/bin/activate
poetry env info
poetry show --tree
mng runserver 
poetry add celery 
poetry add flower
mng runserver 
git status
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
celery -A lindaStore worker -l info
celery -A lindaStore flower
celery --broker=amqp://guest:guest@localhost:5672// flower
cd 
cd Proj_2024/linda-store
pyenv local
pip list
pip install django
pip uninstall django 
pip list
pip list -h
pip list -l
source .venv/bin/activate
pip list -l
poetry show --tree
mng runserver 
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
source .venv/bin/activate
celery --broker=amqp://guest:guest@localhost:5672// flower
celery -A tasks flower --loglevel=info
celery --help
celery -A lindaStore flower --loglevel=info
celery flower --basic-auth=guest:guest
elery flower --address='0.0.0.0'
celery flower --address='0.0.0.0'
celery flower --address='localhost'
cd Proj_2024/linda-store
cd
cd Proj_2024/linda-store
code .

celery flower --address='localhost'
celery -A tasks worker --loglevel=info
celery -A lindaStore --loglevel=info
celery -A lindaStore worker --loglevel=info
git status
git stash
git branch
git stach --help
git stash --help
git stash info
git stash list
git stash show
```

## issue#22
```python
git checkout -b issue#22
git stash pop
git status
git add poetry.lock pyproject.toml
git add .python-version
git status
git add lindaStore/docs/
git status
task lint
task test
git commit -m 'fix(issue#22): Corrigido a versão do python baixamos para 3.11, para conflito com pip.'
git push -u origin issue#22
git checkout main
git pull origin main
```
