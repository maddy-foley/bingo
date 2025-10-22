from flask import Flask, render_template
from functions import draw_bingo_card


app = Flask(__name__)

@app.route("/")
def hello_world():
    draw_bingo_card()
    return render_template('bingo.html')