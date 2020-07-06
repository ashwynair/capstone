from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_cors import CORS
from flask_migrate import Migrate

moment = Moment()
db = SQLAlchemy()
migrate = Migrate()

from app.views import view


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    moment.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app import models

    app.register_blueprint(view)

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    return app
