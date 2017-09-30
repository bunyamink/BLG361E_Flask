# -*- coding: utf-8 -*-
from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('home.html', day_name=day)
    
@app.route('/movies')
def movies_page():
    return render_template('movies.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
