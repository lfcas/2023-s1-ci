# Projeto para suporte às aulas de integração contínua
test
## Problema
Esse repositório implementa uma API HTTP para validar o texto de uma senha 
de acordo com alguns critérios. Entretanto, o código está incompleto e possui
bugs, o seu trabalho é consertá-lo, completá-lo e rodar o pipeline.<br>

Este repositório foi desenvolvido utilizando o gerenciador de pacotes 
**poetry**, mas você não precisa dele. Basta utilizar o arquivo 
simple_web_api/requirements.txt<br>

### Os critérios para senhas válidas são:
1. Mínimo de 8 caracteres<br>
2. Pelo menos 1 número<br>
3. Pelo menos 1 caractere especial<br>
4. Pelo menos 1 letra maiúscula<br>
5. Pelo menos 1 letra minúscula<br>
6. Caracteres especiais não podem ser / ^ ~<br>

# Tarefas
## 0. Faça o fork do projeto no github;
## 1. Faça o clone do seu fork na sua máquina;
## 2. Verifique que os testes não cobrem a especificação e adicione testes e implementação adequados;
## 3. Rode o seu pipeline com sucesso.

# Instalando o ambiente de desenvolvimento

## Development environment dependencies
| Dependencies      | Tested Version | Minimum Version | Url                                                            |
|-------------------|----------------|-----------------|----------------------------------------------------------------|
| Python            | 3.11           | 3.7.5           | [link](https://www.python.org/downloads/release/python-3110/)  |
| Poetry (optional) | 1.2.0          | 1.0.0           | [link](https://python-poetry.org/)                             |

### clone o seu fork
````shell
$ git clone git@github.com:...XXXX.../2023-s1-ci.git
````

### Instalando as dependências
````shell
$ cd 2023-s1-ci/
$ python3 -m venv .venv
$ source .venv/bin/activate
$ cd simple_web_app
$ pip install -r requirements.txt
````

## Rodando a aplicação web
````shell
$ cd 2023-s1-ci/simple_web_app
$ uvicorn main:app --reload
````

## Rodando os testes
````shell
$ cd 2023-s1-ci
$ pytest
````

## Apêndice
### Publicar imagens docker
0. Criar uma conta no docker hub https://hub.docker.com/
1. Criar access token no docker hub
2. Criar variável mascarada **docker_hub_token** com este access_token no github
3. Criar variável **docker_hub_login** com o seu espaço no docker hub no github
4. Rodar os stages de build e release do pipeline

### Fazer deploy da aplicação no PaaS chamado deta
0. Criar uma conta no deta https://www.deta.sh/
1. Instalar cliente do deta e configurar projeto
````shell
$ curl -fsSL https://get.deta.dev/cli.sh | sh   # instalar cliente deta
$ source ~/.bashrc                              # disponibilizar comando
$ deta login                                    # logar na conta já criada
$ cd 2023-s1-ci                                 # entrar na raiz do projeto
$ deta new —python simple_web_app               # criar projeto no cloud deta
$ cd simple_web_app                             # entrar na pasta com código python
$ deta deploy                                   # realizar deploy
$ deta visor enable                             # habilitar logs no cloud deta
````
2. Gerar access token em settings no site deta
3. Criar variável mascarada **DETA_ACCESS_TOKEN** no github
4. Commitar modificações no arquivo simple_web_app/.deta/prog_info
5. Criar variável **PRODUCTION_URL** no github com a URL do serviço na deta
6. Seguir o fluxo de gerência de configuração até a branch main
7. Disparar o job de deploy manualmente ao final da pipeline na main

### rodando do docker
````shell
$ cd 2023-s1-ci
$ docker build -t simple_web_app .
$ docker run --rm -p 8000:80 simple_web_app
````
