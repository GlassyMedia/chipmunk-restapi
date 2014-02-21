import spreadsheet
import unittest


class SpreadsheetTest(unittest.TestCase):
    def test_write_cell(self):
        self.assertIsNone(spreadsheet.write_cell("chipmunk testing",
                                                 "1",
                                                 "A",
                                                 "this is test"))
