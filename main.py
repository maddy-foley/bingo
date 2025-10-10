from flask import Flask, render_template
from card import make_detail_card_rows



app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
   return render_template('home.html')

@app.route("/card")
def card():
   card = make_detail_card_rows()

   return render_template('card.html', card=card)