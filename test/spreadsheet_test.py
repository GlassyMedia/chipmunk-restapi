from controller import spreadsheet as ss
import unittest


class SpreadsheetTest(unittest.TestCase):
    def test_write_cell(self):
        self.assertIsNone(ss.write_cell("chipmunk testing",
                                        "1",
                                        "A",
                                        "this is test"))
