from webtest import TestApp
import unittest
import server
import os

app = TestApp(server.app)
WORKSHEET = os.environ.get('TEST_WORKSHEET_KEY')


class TestAppendCell(unittest.TestCase):
    def test_post_cell_append(self):
        response = app.post_json('/api/v1/cell/append',
                                 {'worksheetKey': WORKSHEET,
                                  'col': 'A',
                                  'value': 'POSTed cell'})
        self.assertEqual(response.status, "201 Created")

    def test_post_cell_missing_keys(self):
        response = app.post_json('/api/v1/cell/append',
                                 {'worksheetKey': WORKSHEET,
                                  'col': 'A'},
                                 status=400)
        self.assertEqual(response.status, "400 Bad Request")

    def test_post_cell_nojson(self):
        response = app.post('/api/v1/cell/append', status=400)
        self.assertEqual(response.status, "400 Bad Request")


class TestWriteReadCell(unittest.TestCase):
    def test_post_cell(self):
        response = app.post_json('/api/v1/cell',
                                 {'worksheetKey': WORKSHEET,
                                  'row': 3,
                                  'col': 'A',
                                  'value': 'POSTed cell'})
        self.assertEqual(response.status, "201 Created")

    def test_post_cell_missing_keys(self):
        response = app.post_json('/api/v1/cell',
                                 {'worksheetKey': WORKSHEET,
                                  'col': 'A'},
                                 status=400)
        self.assertEqual(response.status, "400 Bad Request")

    def test_post_cell_nojson(self):
        response = app.post('/api/v1/cell', status=400)
        self.assertEqual(response.status, "400 Bad Request")
