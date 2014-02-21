import gspread
import os


def write_cell(worksheetKey, row, col, value):
    gc = gspread.login(os.environ.get('GOOGLE_USER'),
                       os.environ.get('GOOGLE_PASS'))
    worksheet = gc.open_by_key(worksheetKey).get_worksheet(0)
    if(worksheet.acell(col + row).value is None):
        worksheet.update_acell(col + row, value)
