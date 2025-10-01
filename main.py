from flask import Flask
from flask import render_template
from card import make_card_rows



app = Flask(__name__, static_folder='static')

@app.route("/")
def hello_world():
   card = make_card_rows()

   return render_template('card.html', card=card)


