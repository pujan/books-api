# books-api
REST API - Polish books

## Make developer enviroment

### Create virtual enviroment (virtualenv)
```bash
venv env
source env/bin/activate
pip install -r requirements.txt
```

### Create virtual enviroment (virtualenvwrapper)

```bash
mkvirtualenv -r requirements.txt books-api
```

### Patching swagger template

```bash
patch $PATH_TO_VIRTUALENV_SITE_PACKAGES/rest_framework_swagger/templates/rest_framework_swagger/index.html swagger.patch
```

### Migrate a database

```bash
./manage.py migrate
```

### Create a super user

```bash
./manage.py createsuperuser
```

### Filling the database with fixtures - random data

```bash
./manage.py testfixtures
```

### Run developer server

```bash
./manage.py runserver
```

## API

### GET books

```
/books/
```

### GET a book

```
/books/1/
```

### GET autors

```
/authors/
```

### GET an author

```
/authors/1/
```

### GET publishers

```
/publishers/
```

### GET a publisher

```
/publishers/1/
```

### GET number of authors, number of books and number of publishers

```
/counters/
```

[![GitHub license](https://img.shields.io/github/license/pujan/books-api)](https://github.com/pujan/books-vue/blob/main/LICENSE)
