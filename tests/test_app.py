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
        load_dotenv('../.env')
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

    def test_401_get_actors(self):
        """Test for retrieving questions with assistant token"""
        res = self.client().get(
            '/api/actors',
            headers=[
                ('Content-Type', 'application/json')
            ]
        )
        self.assertEqual(res.status_code, 401)

    def test_get_movies_by_assistant(self):
        """Test for retrieving questions with assistant token"""
        assistant_token = os.getenv('assistant_token')
        res = self.client().get(
            '/api/movies',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { assistant_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_401_get_movies(self):
        """Test for retrieving questions with assistant token"""
        res = self.client().get(
            '/api/movies',
            headers=[
                ('Content-Type', 'application/json')
            ]
        )
        self.assertEqual(res.status_code, 401)

    def test_add_actors_by_director(self):
        """Test for retrieving questions with assistant token"""
        director_token = os.getenv('director_token')
        res = self.client().post(
            '/api/actors',
            json={
                "name": "Ashwyn Nair",
                "age": 22,
                "gender": "M"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { director_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_422_age_not_provided_add_actor(self):
        """Test for retrieving questions with assistant token"""
        director_token = os.getenv('director_token')
        res = self.client().post(
            '/api/actors',
            json={
                "name": "Ashwyn Nair",
                "gender": "M"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { director_token }')
            ]
        )
        self.assertEqual(res.status_code, 422)

    def test_add_movies_by_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        res = self.client().post(
            '/api/movies',
            json={
                "title": "Movie 1",
                "release_date": "01/01/2021"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { exec_prod_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_422_title_not_provided_add_movie(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        res = self.client().post(
            '/api/movies',
            json={
                "release_date": "01/01/2021"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { exec_prod_token }')
            ]
        )
        self.assertEqual(res.status_code, 422)

    def test_delete_actors_by_director(self):
        """Test for retrieving questions with assistant token"""
        director_token = os.getenv('director_token')
        test_delete_actor_id = os.getenv('test_delete_actor_id')
        res = self.client().delete(
            '/api/actors/' + str(test_delete_actor_id),
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { director_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_404_delete_nonexistent_actor_by_director(self):
        """Test for retrieving questions with assistant token"""
        director_token = os.getenv('director_token')
        res = self.client().delete(
            '/api/actors/' + str(99),
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { director_token }')
            ]
        )
        self.assertEqual(res.status_code, 404)

    def test_delete_movies_by_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        test_delete_movie_id = os.getenv('test_delete_movie_id')
        res = self.client().delete(
            '/api/movies/' + str(test_delete_movie_id),
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { exec_prod_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_404_delete_nonexistent_movie_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        res = self.client().delete(
            '/api/movies/' + str(99),
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { exec_prod_token }')
            ]
        )
        self.assertEqual(res.status_code, 404)

    def test_update_actor_by_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        test_patch_actor_id = os.getenv('test_patch_actor_id')
        res = self.client().patch(
            '/api/actors/' + str(test_patch_actor_id),
            json={
                "name": "New Name"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { exec_prod_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_404_update_nonexistent_actor_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        res = self.client().patch(
            '/api/movies/' + str(99),
            json={
                "name": "New Name"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { exec_prod_token }')
            ]
        )
        self.assertEqual(res.status_code, 404)

    def test_update_movie_by_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        test_patch_movie_id = os.getenv('test_patch_movie_id')
        res = self.client().patch(
            '/api/actors/' + str(test_patch_movie_id),
            json={
                "title": "New Title"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { exec_prod_token }')
            ]
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data["success"])

    def test_404_update_nonexistent_movie_exec_producer(self):
        """Test for retrieving questions with assistant token"""
        exec_prod_token = os.getenv('exec_prod_token')
        res = self.client().patch(
            '/api/movies/' + str(99),
            json={
                "title": "New Title"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer { exec_prod_token }')
            ]
        )
        self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
    unittest.main()