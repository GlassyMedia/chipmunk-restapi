from controller import spreadsheet as ss
import gspread
import unittest


class SpreadsheetTest(unittest.TestCase):
    def test_write_cell(self):
        self.assertIsNone(ss.write_cell("0AlVXob3noRJTdFV5b3piVU03LU1zaEVObU4wMXViSmc",
                                        "1",
                                        "A",
                                        "this is test"))

    def test_write_worksheet_not_found(self):
        self.assertRaises(gspread.SpreadsheetNotFound,
                          ss.write_cell,
                          "xxx1234",
                          "1",
                          "A",
                          "this is test")
