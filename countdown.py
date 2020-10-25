from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route('/countdown')
def roll():
    delta_date = date.today() - date(year=2021, month=1, day=1)
    countdown = delta_date.days
    return f'the number of days until the next January 1st is: {str(abs(countdown))}'


@app.route('/')
def index():
    return 'hello tst'


if __name__ == '__main__':
    app.run(debug=True)
