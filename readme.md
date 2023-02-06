# Comando usado para criar projeto inicial
## rodar no terminal do Pycharm...
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
python manage.py runserver

## Criando o primeiro app 'galeria'
python manage.py startapp galeria

## Obs: Um projeto pode conter varios apps

## Colocar os arquivos estaticos dentro da pasta 'static'
* Depois rodar o comando abaixo para coletar os arquivos estaticos
`python manage.py collectstatic`

* Observar que apareceu uma pasta nova acima de 'venv'

## Carregando demais paginas da aplicação


