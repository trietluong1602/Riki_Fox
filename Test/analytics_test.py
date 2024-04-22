import unittest
import sys
sys.path.append("/Users/xanderchua/Desktop/Xander Document/School/CSC 440/Riki_Fox/")
from wiki.web.routes import track_page_view, get_view_count, get_timestamps
# import config
from Riki import app


class TestPageViewFunctions(unittest.TestCase):

    def test_track_page_view(self):
        with app.test_client() as client:
            response = client.post("/track_page_view", json={"page": "example_page"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode("utf-8"), "Page view tracked successfully")

    def test_get_view_count(self):
        with app.test_client() as client:
            response = client.post("/get_view_count", json={'page': 'example_page'})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            assert int(data["view_count"]) > 0

            response = client.post("/get_view_count", json={"page": "rubbish"})
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.data.decode("utf-8"), "{\"error\":\"Page not found\"}\n")

    def test_get_timestamps(self):
        with app.test_client() as client:
            response = client.post("/get_timestamps", json={"page": "example_page"})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            assert int(data[0]["count"]) > 0

            response = client.post("/get_timestamps", json={"page": "rubbish"})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data, [])

if __name__ == "__main__":
    unittest.main()
