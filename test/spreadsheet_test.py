from controller import spreadsheet as ss
import gspread
import unittest
import os

WORKSHEET = os.environ.get('TEST_WORKSHEET_KEY')


class SpreadsheetTest(unittest.TestCase):
    def setUp(self):
        """Wipe first column in the test worksheet."""
        gc = ss.new_token()
        worksheet = gc.open_by_key(WORKSHEET).get_worksheet(0)
        cell_list = worksheet.range('A1:A100')
        for cell in cell_list:
            cell.value = ''
        worksheet.update_cells(cell_list)

    def test_write_cell(self):
        self.assertIsNone(ss.write_cell(WORKSHEET,
                                        "1",
                                        "A",
                                        "write cell"))

    def test_writeread_cell(self):
        message = "write test cell message"
        ss.write_cell(WORKSHEET, "2", "A", message)
        self.assertEqual(ss.read_cell(WORKSHEET, "2", "A"), message)

    def test_write_worksheet_not_found(self):
        self.assertRaises(gspread.SpreadsheetNotFound,
                          ss.write_cell,
                          "xxx1234",
                          "1",
                          "A",
                          "write not found")

    def test_col2num(self):
        self.assertEqual(ss.col2num("A"), 1)
        self.assertEqual(ss.col2num("Z"), 26)
        self.assertEqual(ss.col2num("AA"), 27)

    def test_next_append_row(self):
        ss.write_cell(WORKSHEET,
                      "1",
                      "A",
                      "occupied cell")
        self.assertEqual(ss.next_append_row(WORKSHEET, "A"),
                         2)
