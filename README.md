# Gerencia de estabelecimentos


-  clone o projeto ``` https://github.com/eltonjncorreia/estabelecimentos.git store ```
-  entre no diretorio ``` cd store ```
-  crie um ambiente virtual da maneira que preferir ``` python -m venv .venv ``` ou com Pipenv
-  ative o virtual env ``` source .venv/bin/activate ```

-  Instale as dependencias.
-  Estou usando o Pipenv, então use ``` pipenv install Pipfile```
-  depois ative a virtual env  ``` pipenv shell```
-  ou  se estiver usando pip,
-  depois ``` pip install -r requirements.txt ```

-  Configure a instância com o .env  ``` cp contrib/env-sample .env ```
-  rode os testes ``` python manage.py test ```

##### Crie as migrações.

-  Crie as migrações com o camando ``` python manage.py migrate ```
-  execute a aplicação ```python manage.py runserver```

