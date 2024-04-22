import unittest
from flask import Flask, render_template, send_file, current_app
from flask.testing import FlaskClient
from unittest.mock import patch, Mock
from routes import bp
from werkzeug.exceptions import NotFound
import io


class TestDownload(unittest.TestCase):
    def setUp(self):
        # Create a Flask test app
        self.app = Flask(__name__)
        self.app.register_blueprint(bp)

        # Set up an application context
        self.ctx = self.app.app_context()
        self.ctx.push()

        # Mocking configuration access
        config = {
            'CONTENT_DIR': '/path/to/content',
            'APPLICATION_ROOT': '/',
            'PREFERRED_URL_SCHEME': 'http',
            'SERVER_NAME': 'localhost',
            'SECRET_KEY': 'test_secret_key',
            'PROPAGATE_EXCEPTIONS': True,
            'SESSION_COOKIE_NAME': 'session',
            'USE_X_SENDFILE': False,
            'SEND_FILE_MAX_AGE_DEFAULT': 0,
            'SESSION_COOKIE_DOMAIN': 'localhost',
            'SESSION_COOKIE_PATH': '/',
            'SESSION_COOKIE_SECURE': False,
            # Add other configurations as needed
        }

        # Load configuration into the Flask app
        self.app.config.from_mapping(config)

        self.client = self.app.test_client()

    def tearDown(self):
        # Pop the application context after the test
        self.ctx.pop()

    @patch('routes.current_wiki.get_or_404')
    def test_download_route(self, mock_get_or_404):
        # Mocking the get_or_404 function to return a mock page
        mock_page = Mock()
        mock_page.title = "Mock Title"
        mock_page.body = "Mock Body"
        mock_get_or_404.return_value = mock_page

        # Make a request to the download route
        response = self.client.get('/download/example_page/')

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response content type starts with 'text/plain'
        self.assertTrue(response.content_type.startswith('text/plain'))

        # Assert that the response contains attachment headers
        self.assertTrue('attachment' in response.headers['Content-Disposition'])



    @patch('routes.current_wiki.get_or_404')
    def test_download_route_title(self, mock_get_or_404):
        # Mocking the get_or_404 function to return a mock page
        mock_page = Mock()
        mock_page.title = "Mock Title"
        mock_get_or_404.return_value = mock_page

        # Make a request to the download route
        response = self.client.get('/download/example_page/')

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response content type starts with 'text/plain'
        self.assertTrue(response.content_type.startswith('text/plain'))

        # Assert that the response contains attachment headers
        self.assertTrue('attachment' in response.headers['Content-Disposition'])


    @patch('routes.current_wiki.get_or_404')
    def test_download_route_body(self, mock_get_or_404):
        # Mocking the get_or_404 function to return a mock page
        mock_page = Mock()
        mock_page.body = "Mock Body"
        mock_get_or_404.return_value = mock_page

        # Make a request to the download route
        response = self.client.get('/download/example_page/')

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response content type starts with 'text/plain'
        self.assertTrue(response.content_type.startswith('text/plain'))

        # Assert that the response contains attachment headers
        self.assertTrue('attachment' in response.headers['Content-Disposition'])



    def test_download_route_with_invalid_url(self):
        # Make a request to the download route with an invalid URL (no slashes)
        response = self.client.get('/download/invalidurl')

        # Assert that the response status code is 308
        self.assertEqual(response.status_code, 308)


if __name__ == '__main__':
    unittest.main()
