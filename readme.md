<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Alura Spaces" />

  &#xa0;

  <!-- <a href="https://aluraspaces.netlify.app">Demo</a> -->
</div>

<h1 align="center">Alura Spaces</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/Gelvazio/alura-spaces?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/Gelvazio/alura-spaces?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Gelvazio/alura-spaces?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/Gelvazio/alura-spaces?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/Gelvazio/alura-spaces?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/Gelvazio/alura-spaces?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/Gelvazio/alura-spaces?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Alura Spaces 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-starting-a-new-project">Starting a New Project</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-customizing-project">Customizing Project</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/Gelvazio" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Projeto de estudos Python Alura
* Observação: Um projeto pode conter varios 'apps'

## :sparkles: Features ##

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/Gelvazio/alura-spaces

# Access
$ cd alura-spaces

# Install dependencies
$ pip install django
$ pip freeze > requirements.txt

# Run the project
$ python manage.py runserver

# The server will initialize in the <http://localhost:8000>
```

## :white_check_mark: Starting a New Project ##
```bash
# Criando o primeiro app 'galeria'
$ python manage.py startapp galeria`

# Create a new project
$ django-admin startproject setup .

# Comando para ativar a venv no vscode
$ venv/Scripts/Activate.ps1

# Colocar os arquivos estaticos dentro da pasta 'static'
# Depois rodar o comando abaixo para coletar os arquivos estaticos
$ python manage.py collectstatic

# Comando para criar os models atraves de 'migrations'
$ python manage.py makemigrations

# Comando para atualizar as migrations
$ python manage.py migrate

# Toda vez que mexer no model, precisa reexecutar as Migrations
$ python manage.py makemigrations
$ python manage.py migrate

# Instalando Pillow para fotos
$ python -m pip install Pillow

# Secret Key deste projeto
$ SECRET_KEY = 'django-insecure--%1%&9r!%xemk$@ue6^mfp!qm+j2u5q4n+qk!6-!$^h11v&2x6'

# instalando pacote de variaveis de ambiente 
$ pip install python-dotenv

# Instalar a extensao do vscode 'SQLite Viewer'

# Configuracao do Django Admim
# Dados do usuario
$ Usuario:admim
$ Senha:123456

```

## :white_check_mark: Customizing Project
- [x] Criar as rotas de filtros por tipo de imagem(Nebulosa, Estrela, Galáxia, Planeta)
- :heavy_check_mark: Criar a rota de fotos mais vistas
- :heavy_check_mark: Criar a rota de fotos novas
- :heavy_check_mark: Criar a rota de surpreenda-me - com fotos diferentes
- :heavy_check_mark: Adicionar url direto da nasa mesmo, exemplo:
    https://apod.nasa.gov/apod/image/2303/RainbowTree_Houck_3198.jpg
    para isso usar o campo = publicada se for true pega da nasa senao pega local
- :heavy_check_mark: Lista de varias fotos da Nasa: https://apod.nasa.gov/apod/archivepix.html
- :heavy_check_mark: Adicionar a opcao de curtir a foto por usuario

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/Gelvazio" target="_blank">Gelvazio Camargo</a>

&#xa0;

<a href="#top">Back to top</a>
