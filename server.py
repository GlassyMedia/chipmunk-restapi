from bottle import Bottle, run
import spreadsheet

app = Bottle()


@app.route('/api/v1/cell', method='POST')
def post_cell():
    data = app.request.json
    spreadsheet.write_cell(data["worksheet"],
                           data["row"],
                           data["col"],
                           data["value"])

if __name__ == "__main__":
    run(app, host='localhost', port=8080)
