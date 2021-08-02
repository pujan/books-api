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
