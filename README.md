## CRUD com Python e Django

![Badge](https://img.shields.io/github/license/jarnunes/crudveiculos)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


## 👨‍💻 Visit this project on Heroku
[Click here access web application](https://crudveiculos.jnunesc.com.br/)

<!--ts-->
### 📖 Menu
* [Features](#-features)
* [Running project](#-running-project)
* [Technologies](#-technologies)
<!--te-->

--------------------------------------------------------------------------------
### 💡 Features
- [x] Create
- [x] Read
- [x] Update
- [x] Delete

--------------------------------------------------------------------------------
### ⚙ Running project
1. Clone this project ``` git clone https://github.com/jarnunes/crudveiculos.git ```
2. [Install Python 3+](https://www.python.org/downloads/)
3. Install all requirements available on crudveiculos/requirements.txt ``` pip install -r requirements.txt ```
4. Set the environments values to database on ``` .env ``` file or System Environments:
   DJGDB_HOST, DJGDB_NAME,  DJGDB_PASSWORD, DJGDB_PORT, DJGDB_USERNAME
5. Build migrations with command ``` py manage.py makemigrations ```
6. Migrate models with command ``` py manage.py migrate ```
7. Now, run application with ``` py manage.py runserver ``` 
8. Visit http://localhost:8000 in your browser. The app should be up & running.

--------------------------------------------------------------------------------

### 🛠 Technologies

- [Python](#)
- [Django](#)
- [HTML](#)
- [CSS](#)
- [JavaScript](#)
