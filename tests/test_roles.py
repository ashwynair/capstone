import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app import create_app


class EndpointTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    def tearDown(self):
        pass

    def test_get_actors_by_assistant(self):
        """Test for retrieving questions with assistant token"""
        assistant_token = os.getenv('assistant_token')
        res = self.client().get(
            '/api/actors',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { assistant_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_get_movies_by_assistant(self):
        """Test for retrieving questions with assistant token"""
        assistant_token = os.getenv('assistant_token')
        res = self.client().get(
            '/api/actors',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { assistant_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_error_add_movies_by_assistant(self):
        """Test for retrieving questions with assistant token"""
        assistant_token = os.getenv('assistant_token')
        res = self.client().post(
            '/api/movies',
            json={
                "name": "Actor 1",
                "age": 22,
                "gender": "M"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { assistant_token }')
            ]
        )
        self.assertEqual(res.status_code, 401)

    def test_add_actors_by_director(self):
        """Test for retrieving questions with assistant token"""
        director_token = os.getenv('director_token')
        res = self.client().post(
            '/api/actors',
            json={
                "name": "Actor 1",
                "age": 22,
                "gender": "M"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {director_token}')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_delete_actors_by_director(self):
        """Test for retrieving questions with assistant token"""
        director_token = os.getenv('director_token')
        test_delete_actor_id = os.getenv('test_delete_actor_id')
        res = self.client().delete(
            '/api/actors/' + str(test_delete_actor_id),
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {director_token}')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_error_add_movies_by_director(self):
        """Test for retrieving questions with assistant token"""
        director_token = os.getenv('director_token')
        res = self.client().post(
            '/api/movies',
            json={
                "title": "Movie 1",
                "release_date": "22/05/2016"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {director_token}')
            ]
        )
        self.assertEqual(res.status_code, 401)

    def test_edit_movies_by_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        test_patch_actor_id = os.getenv('test_patch_actor_id')
        res = self.client().patch(
            '/api/actors/' + str(test_patch_actor_id),
            json={
                "name": "Edited Actor",
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {exec_prod_token}')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_delete_movies_by_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        test_delete_movie_id = os.getenv('test_delete_movie_id')
        res = self.client().delete(
            '/api/movies/' + str(test_delete_movie_id),
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {exec_prod_token}')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])
