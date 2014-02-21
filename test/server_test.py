from webtest import TestApp
import unittest
import server
import os

app = TestApp(server.app)
WORKSHEET = os.environ.get('TEST_WORKSHEET_KEY')


class TestWriteCell(unittest.TestCase):
    def test_post_cell(self):
        response = app.post_json('/api/v1/cell',
                                 {'worksheetKey': WORKSHEET,
                                  'row': '2',
                                  'col': 'A',
                                  'value': 'unit test pass'})
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
