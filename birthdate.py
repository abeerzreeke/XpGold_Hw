from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route('/birthdate/<int:year>/<int:month>/<int:day>')
def roll(year, month, day):

    delta_date = date.today() - date(year=year, month=month, day=day)

    minute_age = int(delta_date.total_seconds() / 60)

    return f' the number of minutes you lived in his life is: {str(minute_age)}'


@app.route('/')
def index():
    return 'hello tst'


if __name__ == '__main__':
    app.run(debug=True)
