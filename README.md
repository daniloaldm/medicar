
# Instalação e Execução Backend

## Tecnologias utilizadas

Para o desenvolvimento do projeto foi utilizada as seguintes tecnologias:

- :snake: **Python 3** 
- :snake:  **Django** — Framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view
- :oil_drum: **Django Rest Framework** — Biblioteca para o Framework Django que disponibiliza funcionalidades para implementar APIs Rest de forma extremamente rápida.
- :anchor: **Djoser**  — Fornece um conjunto de visualizações do Django Rest Framework para lidar com ações básicas, como registro, login, logout, redefinição de senha e ativação da conta. Funciona com modelo de usuário personalizado
- :closed_lock_with_key: **Jwt**  — É um padrão da Internet para a criação de dados com assinatura opcional e/ou criptografia cuja sua payload contém o JSON que afirma algum número de declarações.

## Instalação
Clone o repositório:
```
git clone git@github.com:daniloaldm/medicar.git
```
Vá para o diretório backend:
```
cd backend
```
Para facilitar a execução deixei o banco de dados e a venv de fora do .gitignore. Execute:
```
source start-env/bin/active
```
Após isso, basta executar: 
```
python3 manage.py runserver
```

## :man_technologist: Autor

- **Danilo Alexandrino** - [GitHub](https://github.com/daniloaldm) - Email: [danilo.alexandrinodm@gmail.com](mailto:danilo.alexandrinodm@gmail.com)