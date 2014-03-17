from bottle import Bottle, run, request, response
from controller import spreadsheet as ss

app = Bottle()


@app.post('/api/v1/cell/append')
def post_cell_append():
    """
    Append a cell with 'value' to the next available row in 'col' of
    'worksheetKey'.

    POST a JSON with 'worksheetKey', 'col', and 'value' keys.
    HTTP request header must set Content-Type to application/json.
    """
    data = request.json
    attr = ('worksheetKey', 'col', 'value')

    if data is not None and all(key in data for key in attr):
        worksheet = data[attr[0]]
        col = data[attr[1]]
        row = ss.next_append_row(worksheet, col)
        value = data[attr[2]]
        ss.write_cell(worksheet, row, col, value)
        response.status = '201 Created'
    else:
        response.status = '400 Bad Request'

    return response


@app.post('/api/v1/cell')
def post_cell():
    """
    POST to a specific cell to write value into location specified
    """
    data = request.json
    attr = ('worksheetKey', 'row', 'col', 'value')

    if data is not None and all(key in data for key in attr):
        worksheet = data[attr[0]]
        row = data[attr[1]]
        col = data[attr[2]]
        value = data[attr[3]]
        ss.write_cell(worksheet, row, col, value)
        response.status = '201 Created'
    else:
        response.status = '400 Bad Request'

    return response


@app.get('/api/v1/cell')
def get_cell():
    """
    GET a specific cell
    """
    q = request.query.decode()
    worksheet = q['worksheetKey']
    row = q['row']
    col = q['col']
    value = ss.read_cell(worksheet, row, col)
    response.status = '200 OK'
    response.content_type = 'application/json'
    return {'value': value,
            'row': row,
            'col': col,
            'worksheetKey': worksheet}


@app.get('/api/v1/column')
def get_column():
    """
    GET a specific column
    """
    q = request.query.decode()
    worksheet = q['worksheetKey']
    col = q['col']
    values = ss.read_column(worksheet, col)
    if values is not None:
        response.status = '200 OK'
        response.content_type = 'application/json'
        return {'values': values,
                'col': col,
                'worksheetKey': worksheet}
    else:
        response.status = '400 Bad Request'
        return response


if __name__ == "__main__":
    run(app, host='localhost', port=8080, reloader=True, debug=True)
