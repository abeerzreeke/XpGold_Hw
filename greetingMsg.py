from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/greeting')
def roll():
    now_date = datetime.now()
    if 8 <= now_date.hour < 13:
        return f'{str(now_date)} good morning'
    if 13 <= now_date.hour < 17:
        return f'{str(now_date)} good afternoon'
    if 17 <= now_date.hour < 21:
        return f'{str(now_date)} good evening'
    else:
        return f'{str(now_date)} Good night'


if __name__ == '__main__':
    app.run(debug=True)
