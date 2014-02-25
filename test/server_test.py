from webtest import TestApp
from controller import spreadsheet as ss
import unittest
import server
import os
import ast

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
    message = {'worksheetKey': WORKSHEET,
               'row': '3',
               'col': 'A',
               'value': 'POSTed cell'}

    def setUp(self):
        """Wipe first column in the test worksheet."""
        gc = ss.new_token()
        worksheet = gc.open_by_key(WORKSHEET).get_worksheet(0)
        cell_list = worksheet.range('A1:A100')
        for cell in cell_list:
            cell.value = ''
        worksheet.update_cells(cell_list)

    def test_post_cell(self):
        response = app.post_json('/api/v1/cell', self.message)
        self.assertEqual(response.status, "201 Created")

    def test_post_get_cell(self):
        self.test_post_cell()
        response = app.get('/api/v1/cell',
                           {'worksheetKey': WORKSHEET,
                            'row': 3,
                            'col': 'A'})
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(ast.literal_eval(response.body), self.message)

    def test_post_cell_missing_keys(self):
        response = app.post_json('/api/v1/cell',
                                 {'worksheetKey': WORKSHEET,
                                  'col': 'A'},
                                 status=400)
        self.assertEqual(response.status, "400 Bad Request")

    def test_post_cell_nojson(self):
        response = app.post('/api/v1/cell', status=400)
        self.assertEqual(response.status, "400 Bad Request")
