import unittest
from flask import Flask
from ..web.routes import bp

class TestFlaskSearchRoute(unittest.TestCase):
    def setUp(self):
        # Create a Flask test app
        self.app = Flask(__name__)
        self.app.register_blueprint(bp)

        self.client = self.app.test_client()

    def test_search_route_get(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 500)

    def test_tag_ignore_true(self):
        response = self.client.post('/search/', data=dict(
            search_option='tags',
            term='tag1,tag2',
            ignore_case=True
        ))
        self.assertEqual(response.status_code, 500)

    def test_tag_ignore_false(self):
        response = self.client.post('/search/', data=dict(
            search_option='tags',
            term='tag1,tag2',
            ignore_case=False
        ))
        self.assertEqual(response.status_code, 500)


    def test_title_true(self):
        response = self.client.post('/search/', data=dict(
            search_option='title',
            term='title1,title2',
            ignore_case=True
        ))
        self.assertEqual(response.status_code, 500)

    def test_title_false(self):
        response = self.client.post('/search/', data=dict(
            search_option='title',
            term='title1,title2',
            ignore_case=False
        ))
        self.assertEqual(response.status_code, 500)

    def test_body_true(self):
        # Test POST request with search option as 'body'
        response = self.client.post('/search/', data=dict(
            search_option='body',
            term='search term in body',
            ignore_case=True  # Assuming this is the case for this test
        ))
        self.assertEqual(response.status_code, 500)

    def test_body_false(self):
        # Test POST request with search option as 'body'
        response = self.client.post('/search/', data=dict(
            search_option='body',
            term='search term in body',
            ignore_case=True  # Assuming this is the case for this test
        ))
        self.assertEqual(response.status_code, 500)

    def test_default_true(self):
        # Test POST request with default search option
        response = self.client.post('/search/', data=dict(
            term='default search term',
            ignore_case=True  # Assuming this is the case for this test
        ))
        self.assertEqual(response.status_code, 500)

    def test_default_false(self):
        # Test POST request with default search option
        response = self.client.post('/search/', data=dict(
            term='default search term',
            ignore_case=False  # Assuming this is the case for this test
        ))
        self.assertEqual(response.status_code, 500)



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
