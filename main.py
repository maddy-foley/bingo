from flask import Flask, render_template, redirect, url_for, request
from card import make_detail_card_rows



app = Flask(__name__, static_folder='static')

@app.route("/", methods=['GET'])
def hello_world():
   card = make_detail_card_rows()

   return render_template('card.html', card=card)


