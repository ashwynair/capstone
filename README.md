# Capstone Project - Casting Agency

## Motivation

Capstone project for Udacity Full Stack Dev Course.

## Heroku

This application is hosted live on Heroku

URL: https://sleepy-sea-55864.herokuapp.com

## User Roles

#### Casting Assistant

* Can view actors and movies

#### Casting Director

* All permissions a Casting Assistant has and…
* Add or delete an actor from the database
* Modify actors or movies

#### Executive Producer
* All permissions a Casting Director has and…
* Add or delete a movie from the database

## Authentication

JWT Bearer tokens are provided below and in the setup.sh file. These can be used with [Postman](www.postman.com) to test the endpoints detailed in the API Documentation.

#### Assistant

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9xaGxXVUl2SEFtY0VSWkcxbm5VeCJ9.eyJpc3MiOiJodHRwczovL2F2bi1jYXN0aW5nLWFnZW5jeS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwMGE3NDBiYjMzMTMwMDEzOWUyY2FhIiwiYXVkIjoiY2FzdGluZy1hZ2VuY3kiLCJpYXQiOjE1OTQwNzQ2MTQsImV4cCI6MTU5NDE2MTAxNCwiYXpwIjoiMk9kc3A1M0pJS05MYm0xTENXV2FGVDVWaktPbmFrMGsiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0OnJvbGVzIl19.knNNWYWomSuRjqJ-m2Mzptr0VE3gjQEFhC9mMdafI8J14uHE1Btvuu146wd2tbfCgcASuUz6Its-rgLHB_gNIaIcF0YXQpXT1mpLwm5Qtu6JC5c5UZfOOWRXQRZ1vvqG4F2QCul83b_CB09mps75CqP56RMrz-Y71CeoYLlbRzhkp9wcS-uTzQBcwFc7cEnB0jyfvrdY4xeE2xaKGBwBKl7NKM5MmzvSkT-FjiTTCmeK32fHmcY12_g-nDfAKKJWq7bUkHIk8YOVqI5xKswLbPvUCxLQ4Cw38gJXCfgbaFh59WxNy61G4daM-J58pfxb_ul8OfYroIIXUcg0tg1g3g

#### Director

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9xaGxXVUl2SEFtY0VSWkcxbm5VeCJ9.eyJpc3MiOiJodHRwczovL2F2bi1jYXN0aW5nLWFnZW5jeS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwMGE4MjE3NjAwNDQwMDEzOTk5MzM4IiwiYXVkIjoiY2FzdGluZy1hZ2VuY3kiLCJpYXQiOjE1OTQwNzQ2NTksImV4cCI6MTU5NDE2MTA1OSwiYXpwIjoiMk9kc3A1M0pJS05MYm0xTENXV2FGVDVWaktPbmFrMGsiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImdldDpyb2xlcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBhdGNoOnJvbGVzIiwicG9zdDphY3RvcnMiXX0.OsQ6xKVVxz4H6DOxFHec34sqKhN33aXfkbb7Gnlsfo2yvGq3eQQAplTmWg_mjRdX8fkcURuaoAOTIckv3MgyvDQMvZ_G9yNSjUfYp1xrGYYhu5C-TrBy2Bx0KPA8IQGfYfMXTZMQRJtq4vJ6Ohsyd2nDL8LleXJOxF2BNcP-JKzWcLiVuiGYUlgYTd0L0CyykUFB9cF-pQZatQMvsftWZyUSAIDIctQCyg-Z8bIN0W84NDXFzVfO_ID6m2SiDn-G2EFInslNdvlO_8SGGVJ9AXTg1P2K0Al2aQHwJFkLhchK-d7_heOE_ALE9vxVkWNKahMpz175m8i_UgPnb1s4zA

#### Exec Producer

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9xaGxXVUl2SEFtY0VSWkcxbm5VeCJ9.eyJpc3MiOiJodHRwczovL2F2bi1jYXN0aW5nLWFnZW5jeS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwMGE4OTE2YjI1NjEwMDE5MTAyZmVmIiwiYXVkIjoiY2FzdGluZy1hZ2VuY3kiLCJpYXQiOjE1OTQwNzQ2OTAsImV4cCI6MTU5NDE2MTA5MCwiYXpwIjoiMk9kc3A1M0pJS05MYm0xTENXV2FGVDVWaktPbmFrMGsiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZGVsZXRlOnJvbGVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJnZXQ6cm9sZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwYXRjaDpyb2xlcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwb3N0OnJvbGVzIl19.D-tsUv5mDuZElx53q09lZjVhVC39TU6ouowKdBsQKOLC2gYxco4sj1OoOjZvIxdZ3uhoqa8xVA9lORDHK0l_kgjy9JzZWABMw-hvKF-qnNsboW-2vrZ1PpADWA8FaPaqRwKm8E-BFUVGFiMJug2A0LONGA2EcuBvUmdxXGUx8CBdLaecxlAd00kqoA2FyapRKxq35mqqcQeDNP1uTVieBX238cZI4tPB-4nl4UUFJzZkGiV5_a_JAloLhmpWdjyBczerQFJS3tF_NV0D6-CdQfbD4BQCy1VJoojYD5EsBTCVFsA4G0DgpM9W1T17bw-WFfxe6bGi2OOjitLiHsq9JA

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

## Running Locally

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

## Running the server locally

Ensure you are working using your created virtual environment.

To run the server, execute:

```
chmod +x setup.sh
source ./setup.sh
python3 run.py
```

## Unit Testing
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