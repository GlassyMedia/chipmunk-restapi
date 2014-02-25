import gspread
import os
import string


def new_token():
    gc = gspread.login(os.environ.get('GOOGLE_USER'),
                       os.environ.get('GOOGLE_PASS'))
    return gc


def write_cell(worksheetKey, row, col, value):
    gc = new_token()
    worksheet = gc.open_by_key(worksheetKey).get_worksheet(0)
    row = str(row)
    if(worksheet.acell(col + row).value is None):
        worksheet.update_acell(col + row, value)


def read_cell(worksheetKey, row, col):
    gc = new_token()
    worksheet = gc.open_by_key(worksheetKey).get_worksheet(0)
    row = str(row)
    return worksheet.acell(col + row).value


def col2num(col):
    """
    Converts a spreadsheet column letter name to a column number

    Reference:
    http://stackoverflow.com/a/12640614/654416
    """
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num


def read_column(worksheetKey, col):
    gc = new_token()
    worksheet = gc.open_by_key(worksheetKey).get_worksheet(0)
    return worksheet.col_values(col2num(col))


def next_append_row(worksheetKey, col):
    return len(read_column(worksheetKey, col)) + 1
