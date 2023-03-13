# Comando usado para criar projeto inicial
## Rodar no terminal do Pycharm...
`python -m venv C:\xampp\htdocs\projetos-estudos-tidas\projetos-python\02-FORMACAO-DJANGO\alura-spaces\venv`
`python -m venv C:\fontes\fontes-geo\projetos-estudos-tidas\projetos-python\02-FORMACAO-DJANGO\alura-spaces\venv`

# Comando para ativar a venv no vscode
`c:/xampp/htdocs/projetos-estudos-tidas/projetos-python/02-FORMACAO-DJANGO/alura-spaces/venv/Scripts/Activate.ps1`
`venv/Scripts/Activate.ps1`

##Comando para instalar django
`pip install django`

##Comando para criar os requirements
`pip freeze > requirements.txt`

##Comando para iniciar o projeto do Django 
`django-admin startproject setup .`

##SECRET_KEY = 'django-insecure--%1%&9r!%xemk$@ue6^mfp!qm+j2u5q4n+qk!6-!$^h11v&2x6'

## instalando pacote de variaveis de ambiente 
`pip install python-dotenv`

## Atualizar o requirements de novo
`pip freeze > requirements.txt`

## Rodar o projeto 
`python manage.py runserver`

## Criando o primeiro app 'galeria'
`python manage.py startapp galeria`

## Observação: Um projeto pode conter varios 'apps'

## Colocar os arquivos estaticos dentro da pasta 'static'
* Depois rodar o comando abaixo para coletar os arquivos estaticos
`python manage.py collectstatic`

* Observar que apareceu uma pasta nova acima de 'venv'

## Carregando demais páginas da aplicação

## Comando para criar os models atraves de 'migrations'
`python manage.py makemigrations`

## Comando para atualizar as migrations
`python manage.py migrate`

## Instalar a extensao do vscode 'SQLite Viewer'

## Configuracao do Django Admim
* Dados do usuario
`Usuario:admim`
`Senha:123456`

## Crud no Admin
Apos mexer nomodel, precisa reexecutar as Migrations
`python manage.py makemigrations`
`python manage.py migrate`

## Instalando Pillow para fotos
`python -m pip install Pillow`

## Locais para buscar as imagens das Nebulosas
* Brasil
https://brazilastronomy.files.wordpress.com/2014/08/hubble_space_telescope_crab_bebula.jpg

* Nasa
https://apod.nasa.gov/apod/image/1701/potw1636aN159_HST_2048.jpg




