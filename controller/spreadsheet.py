import gspread
import os


def write_cell(worksheet, row, col, value):
    account = gspread.login(os.environ.get('GOOGLE_USER'),
                            os.environ.get('GOOGLE_PASS'))
    worksheet = account.open(worksheet).sheet1
    if(worksheet.acell(col + row).value is None):
        worksheet.update_acell(col + row, value)
