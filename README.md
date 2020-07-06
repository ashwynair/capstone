# Capstone Project - Casting Agency

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

*Note: Please ensure you have the postgres role available.*

```
createdb casting_agency
flask db upgrade
psql casting_agency < data.sql
```

## Running the server

Ensure you are working using your created virtual environment.

To run the server, execute:

```
chmod +x setup.sh
source ./setup.sh
python3 run.py
```

## Directory structure

```
.
├── README.md
├── app
│   ├── __init__.py    // application factory
│   ├── auth.py        // handles RBAC
│   ├── config.py      // configurations for application
│   ├── models.py      // models representing db
│   ├── utils.py       // date format for application
│   └── views.py       // endpoints for application
├── data.sql
├── migrations         // migrations for db
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── f77f759edb07_.py
├── requirements.txt
├── run.py             // file to start application
├── setup.sh           // environment variables
└── tests
    ├── test_app.py
    └── test_roles.py
```

## API Documentation
```

Note: All endpoints below will contain the "success": True key-value pair.

Endpoints
GET '/api/actors'
GET '/api/movies'
POST '/api/actors'
POST '/api/movies'
DELETE '/api/actors/<int:actor_id>'
DELETE '/api/movies/<int:movie_id>'
PATCH '/api/actors/<int:actor_id>'
PATCH '/api/movies/<int:movie_id>'

GET '/api/actors'
- Requires get:actors permissions
- Endpoint for all assistants, directors and executive producers to retrieve a list of actors
- :return: Status code 200 and json {"success": True, "actors": actors} where actors is the list of actors, or an appropriate status code indicating reason for failure

GET '/api/movies'
- Requires get:movies permissions
- Endpoint for all assistants, directors and executive producers to retrieve a list of movies
- :return: Status code 200 and json {"success": True, "movies": movies} where movies is the list of movies, or an appropriate status code indicating reason for failure

POST '/api/actors'
- Requires post:actors permissions
- Endpoint for directors and executive producers to create new actors
- :return: Status code 200 and json {"success": True, "actor": actor} where actor is the details of the new actor that was added to the database

POST '/api/movies'
- Requires post:movies permissions
- Endpoint for directors and executive producers to create new movies
- :return: Status code 200 and json {"success": True, "movie": movie} where movie is the details of the new movie that was added to the database

DELETE '/api/actors/<int:actor_id>'
- Responds with a 404 error if drink corresponding <actor_id> is not found
- Deletes the corresponding row for <actor_id>
- Requires the 'delete:actors' permission
- :param kwargs: Must have actor_id key-value pair for id of actor
- :return: Status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record or appropriate status code indicating reason for failure

DELETE '/api/movies/<int:movie_id>'
- Responds with a 422 error if <movie_id> is not provided by client
- Responds with a 404 error if drink corresponding <movie_id> is not found
- Deletes the corresponding row for <movie_id>
- Requires the 'delete:movies' permission
- :param kwargs: Must have movie_id key-value pair for id of movie
- :return: Status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record or appropriate status code indicating reason for failure

PATCH '/api/actors/<int:actor_id>'
- Responds with a 400 error if <actor_id> is not provided by client
- Responds with a 404 error if drink corresponding <actor_id> is not found
- Updates the corresponding row for <actor_id>
- Requires the 'patch:actors' permission
- Contains the actor.details() data representation in response
- :param kwargs: Has actor_id key-value pair for id of drink
- :return: Status code 200 and JSON {"success": True, "actor": actor}, where actor is an object containing only the updated actor or appropriate status code indicating reason for failure

PATCH '/api/movies/<int:movie_id>'
- Responds with a 400 error if <movie_id> is not provided by client
- Responds with a 404 error if drink corresponding <movie_id> is not found
- Updates the corresponding row for <movie_id>
- Requires the 'patch:movies' permission
- Contains the movie.details() data representation in response
- :param kwargs: Has movie_id key-value pair for id of drink
- :return: Status code 200 and JSON {"success": True, "movie": movie}, where movie is an object containing only the updated movie or appropriate status code indicating reason for failure
```


## Testing
To run the tests, run
```
dropdb casting_agency
createdb casting_agency
flask db upgrade
psql casting_agency < data.sql
chmod +x setup.sh
source ./setup.sh
python3 tests/test_app.py
dropdb casting_agency
createdb casting_agency
flask db upgrade
psql casting_agency < data.sql
chmod +x setup.sh
source ./setup.sh
python3 tests/test_roles.py
```