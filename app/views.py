from sys import exc_info
from flask import jsonify, request, abort, Blueprint, current_app
from app import db
from app.auth import requires_auth
from app.models import Actors, Movies, Roles
from datetime import datetime
from app.utils import standard_date_format

view = Blueprint("view", __name__)


@view.route('/api/actors', methods=["GET"])
@requires_auth('get:actors')
def get_actors(*args, **kwargs):
    """
    Requires get:actors permissions
    Endpoint for all assistants, directors and
    executive producers to retrieve a list of actors
    :return: Status code 200 and json {"success": True,
    "actors": actors} where actors is the list of actors,
    or an appropriate status code indicating reason for failure
    """
    actors = list(map(Actors.details, Actors.query.all()))
    return jsonify({
        "success": True,
        "actors": actors
    })


@view.route('/api/movies', methods=["GET"])
@requires_auth('get:movies')
def get_movies(*args, **kwargs):
    """
    Requires get:movies permissions
    Endpoint for all assistants, directors and executive
    producers to retrieve a list of movies
    :return: Status code 200 and json {"success": True,
    "movies": movies} where movies is the list of movies,
    or an appropriate status code indicating reason for failure
    """
    movies = list(map(Movies.details, Movies.query.all()))
    return jsonify({
        "success": True,
        "movies": movies
    })


@view.route('/api/actors', methods=["POST"])
@requires_auth('post:actors')
def add_actors(*args, **kwargs):
    """
    Requires post:actors permissions
    Endpoint for directors and executive producers to create new actors
    :return: Status code 200 and json {"success": True,
    "actor": actor} where actor is the details of
    the new actor that was added to the database
    """
    data = dict(request.get_json())
    if not all(key in data.keys() for key in ("name", "age", "gender")):
        abort(422)

    error = False
    try:
        new_actor = Actors(
            name=data.get("name"),
            age=data.get("age"),
            gender=data.get("gender")
        )
        new_actor.insert()
        result = {
            "success": True,
            "actor": new_actor.details()
        }
        return jsonify(result)
    except Exception:
        error = True
        db.session.rollback()
        print(exc_info())
    finally:
        db.session.close()
        if error:
            abort(500)


@view.route('/api/movies', methods=["POST"])
@requires_auth('post:movies')
def add_movies(*args, **kwargs):
    """
    Requires post:movies permissions
    Endpoint for directors and executive producers to create new movies
    :return: Status code 200 and json {"success": True,
    "movie": movie} where movie is the details of the
    new movie that was added to the database
    """
    data = dict(request.get_json())
    if not all(key in data.keys() for key in ("title", "release_date")):
        abort(422)

    release_date = ''
    try:
        release_date = datetime.strptime(
            data.get("release_date"),
            standard_date_format
        )
    except ValueError:
        abort(422)

    error = False
    try:
        new_movie = Movies(
            release_date=release_date,
            title=data.get("title")
        )
        new_movie.insert()
        result = {
            "success": True,
            "movie": new_movie.details()
        }
        return jsonify(result)
    except Exception:
        error = True
        db.session.rollback()
        print(exc_info())
    finally:
        db.session.close()
        if error:
            abort(500)


@view.route('/api/actors/<int:actor_id>', methods=["DELETE"])
@requires_auth('delete:actors')
def delete_actors(*args, **kwargs):
    """
    Responds with a 404 error if drink corresponding <actor_id> is not found
    Deletes the corresponding row for <actor_id>
    Requires the 'delete:actors' permission
    :param kwargs: Must have actor_id key-value pair for id of actor
    :return: Status code 200 and json {"success": True,
    "delete": id} where id is the id of the deleted record
    or appropriate status code indicating reason for failure
    """
    actor_id = kwargs.get("actor_id", None)
    if not actor_id:
        abort(400)
    actor = Actors.query.get(int(actor_id))
    if not actor:
        abort(404)
    error = False
    try:
        actor.delete()
        return jsonify({
            "success": True,
            "delete": actor_id
        })
    except Exception:
        error = True
        db.session.rollback()
        print(exc_info())
    finally:
        db.session.close()
        if error:
            abort(500)


@view.route('/api/movies/<int:movie_id>', methods=["DELETE"])
@requires_auth('delete:movies')
def delete_movies(*args, **kwargs):
    """
    Responds with a 422 error if <movie_id> is not provided by client
    Responds with a 404 error if drink corresponding <movie_id> is not found
    Deletes the corresponding row for <movie_id>
    Requires the 'delete:movies' permission
    :param kwargs: Must have movie_id key-value pair for id of movie
    :return: Status code 200 and json {"success": True,
    "delete": id} where id is the id of the deleted record
    or appropriate status code indicating reason for failure
    """
    movie_id = kwargs.get("movie_id", None)
    if not movie_id:
        abort(400)
    movie = Movies.query.get(int(movie_id))
    if not movie:
        abort(404)
    error = False
    try:
        movie.delete()
        return jsonify({
            "success": True,
            "delete": movie_id
        })
    except Exception:
        error = True
        db.session.rollback()
        print(exc_info())
    finally:
        db.session.close()
        if error:
            abort(500)


@view.route('/api/actors/<int:actor_id>', methods=["PATCH"])
@requires_auth('patch:actors')
def update_actors(*args, **kwargs):
    """
    Responds with a 400 error if <actor_id> is not provided by client
    Responds with a 404 error if drink corresponding <actor_id> is not found
    Updates the corresponding row for <actor_id>
    Requires the 'patch:actors' permission
    Contains the actor.details() data representation in response
    :param kwargs: Has actor_id key-value pair for id of drink
    :return: Status code 200 and JSON {"success": True,
    "actor": actor}, where actor is an object containing only
    the updated actor or appropriate status code indicating reason for failure
    """
    actor_id = kwargs.get("actor_id", None)
    if not actor_id:
        abort(400)

    data = dict(request.get_json())
    name = data.get("name", None)
    age = data.get("age", None)
    gender = data.get("gender", None)

    actor = Actors.query.get(int(actor_id))
    if not actor:
        abort(404)

    error = False
    try:
        if name:
            actor.name = name
        if age:
            actor.age = age
        if gender:
            actor.gender = gender
        actor.update()
        return jsonify({
            "success": True,
            "actor": actor.details()
        })
    except Exception:
        error = True
        db.session.rollback()
        print(exc_info())
    finally:
        db.session.close()
        if error:
            abort(500)


@view.route('/api/movies/<int:movie_id>', methods=["PATCH"])
@requires_auth('patch:movies')
def update_movies(*args, **kwargs):
    """
    Responds with a 400 error if <movie_id> is not provided by client
    Responds with a 404 error if drink corresponding <movie_id> is not found
    Updates the corresponding row for <movie_id>
    Requires the 'patch:movies' permission
    Contains the movie.details() data representation in response
    :param kwargs: Has movie_id key-value pair for id of drink
    :return: Status code 200 and JSON {"success": True,
    "movie": movie}, where movie is an object containing only
    the updated movie or appropriate status code indicating reason for failure
    """
    movie_id = kwargs.get("movie_id", None)
    if not movie_id:
        abort(400)

    data = dict(request.get_json())
    title = data.get("title", None)
    release_date = data.get("release_date", None)

    movie = Movies.query.get(int(movie_id))
    if not movie:
        abort(404)

    error = False
    try:
        if title:
            movie.title = title
        if release_date:
            try:
                release_date = datetime.strptime(
                    data.get("release_date"),
                    standard_date_format
                )
                movie.release_date = release_date
            except ValueError:
                abort(422)
        movie.update()
        return jsonify({
            "success": True,
            "actor": movie.details()
        })
    except Exception:
        error = True
        db.session.rollback()
        print(exc_info())
    finally:
        db.session.close()
        if error:
            abort(500)
