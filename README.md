# Gerencia de estabelecimentos


-  clone o projeto ``` https://github.com/eltonjncorreia/estabelecimentos.git store ```
-  entre no diretorio ``` cd store ```
-  crie um ambiente virtual da maneira que preferir ``` python -m venv .venv ```
-  ative o virtual env ``` source .venv/bin/activate ```
-  Instale as dependencias ``` pip install -r requirements.txt ```

#### Ou com Pipenv

-  Com o Pipenv use ``` pipenv install Pipfile```
-  depois ative a virtual env  ``` pipenv shell```

### Configure as instancias

-  Configure a instância com o .env  ``` cp contrib/env-sample .env ```
-  rode os testes ``` python manage.py test ```

##### Crie as migrações.

-  Crie as migrações com o camando ``` python manage.py migrate ```
-  execute a aplicação ```python manage.py runserver```

##### Acessar a aplicação no endereço:

``` https://store-admins.herokuapp.com/ ```