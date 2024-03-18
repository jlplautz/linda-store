git clone git@github.com:jlplautz/linda-store.git
cd linda-store
poetry init
pyenv local 3.12.0
poetry shell
poetry env info

## issue#1
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

## issue#2
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

## issue#4
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

## issue#6
git checkout -b issue#6
mng createsuperuser
django-admin 
mng 
mng createsuperuser 
BB
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

## issue#9
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

## issue#11
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

## issue#13
git checkout -b issue#13
mng runserver 
history
mng runserver 
cd 
cd Proj_2024/
ll
cd linda-store
code .
poetry shell
emulate bash -c '. /home/plautz/Proj_2024/linda-store/.venv/bin/e'
mng runserver 
git checkout main
mng runserver 
