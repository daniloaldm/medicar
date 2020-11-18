<p align="center">
   <img width="300" src="frontend/src/assets/logo.png">
</p>

<p align="center">
   <a href="https://www.linkedin.com/in/danilo-alexandrino-4aaa1518b/">
   <a>
      <img alt="Danilo Alexandrino" src="https://img.shields.io/badge/-Danilo%20Alexandrino-49B4BB?style=flat&logo=Linkedin&logoColor=white" />
  <a href="https://github.com/daniloaldm/medicar/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/daniloaldm/medicar?color=49B4BB">
  </a> 
  <a href="https://github.com/daniloaldm/medicar/blob/master/frontend/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-49B4BB">
  </a>
  <a href="https://github.com/daniloaldm/medicar/stargazers"><img alt="Stargazers" src="https://img.shields.io/github/stars/daniloaldm/medicar?color=49B4BB&logo=github">
  </a>
</p>

# Tecnologias utilizadas
<!--
<p align="center">
   <img src="https://img.shields.io/badge/python-%233776AB.svg?&style=for-the-badge&logo=python&logoColor=white">
   <img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white">
   <img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white">
   <img src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white">
   <img src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">
   <img src="https://img.shields.io/badge/typescript%20-%23007ACC.svg?&style=for-the-badge&logo=typescript&logoColor=white">
   <img src="https://img.shields.io/badge/angular%20-%23DD0031.svg?&style=for-the-badge&logo=angular&logoColor=white">
</p> -->

Para o desenvolvimento do projeto foi utilizada as seguintes tecnologias:

- :snake: **Python 3** 
- :snake:  **Django** — Framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view
- :oil_drum: **Django Rest Framework** — Biblioteca para o Framework Django que disponibiliza funcionalidades para implementar APIs Rest de forma extremamente rápida.
- :anchor: **Djoser**  — Fornece um conjunto de visualizações do Django Rest Framework para lidar com ações básicas, como registro, login, logout, redefinição de senha e ativação da conta. Funciona com modelo de usuário personalizado
- :closed_lock_with_key: **Jwt**  — É um padrão da Internet para a criação de dados com assinatura opcional e/ou criptografia cuja sua payload contém o JSON que afirma algum número de declarações.
- :a: **Angular** - O AngularJS é um framework de código aberto usado para construir aplicativos para web baseados em uma única página dinâmica.

## Instalação e Execução Backend
Clone o repositório:
```
git clone git@github.com:daniloaldm/medicar.git
```
Vá para o diretório backend:
```
cd backend
```
Para facilitar a execução deixei o banco de dados fora do .gitignore. Execute:
```
pip install -r requirements.txt
```
Após isso, basta executar: 
```
python3 manage.py runserver
```
Para testar a API com o Insomnia:
<br><br>
<a href="https://insomnia.rest/run/?label=Medicar%20API&uri=https%3A%2F%2Fgithub.com%2Fdaniloaldm%2Fmedicar%2Fblob%2Fmaster%2FInsomnia.json" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>

## Instalação e Execução Frontend

Caso já possua o repositório pule esta etapa, caso não clone o repositório:
```
git clone git@github.com:daniloaldm/medicar.git
```

Vá para o diretório frontend:
```
cd frontend
```

Após isso, execute: 
```
npm install
```
Logo depois 
```
ng serve
```

Para testar acesse a url padrão local do Angular:
```
http://localhost:4200/
```

## :man_technologist: Autor

- **Danilo Alexandrino** - [GitHub](https://github.com/daniloaldm) - Email: [danilo.alexandrinodm@gmail.com](mailto:danilo.alexandrinodm@gmail.com)
