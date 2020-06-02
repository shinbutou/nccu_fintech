import os
from flask import Flask, render_template

app = Flask(__name__)

portfolio = []
picks = []

@app.route('/')
def index():
	return render_template('index.html', portfolio=portfolio, picks=picks, history=history)


if __name__=='__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)



