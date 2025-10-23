from flask import Flask, render_template, request
from functions import draw_bingo_card


app = Flask(__name__)

@app.route('/')
def home():
    cards = draw_bingo_card()
    return render_template("bingo.html",cards=cards)
# @app.get('/')
# def get_card():
#     return "hi"

# @app.post('/login')
# def draw_card():
#     return "d"