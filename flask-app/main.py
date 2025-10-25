from flask import Flask, render_template, redirect, request
from bingo_file_manager import BingoManager

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # bingo = BingoManager("")
    cards, newest_card, newest_card_column = get_all_formated_drawn_cards()
    return render_template("bingo.html", cards=cards, new_card=newest_card, newest_card_column=newest_card_column)

@app.route('/draw_card', methods=['GET','POST'])
def draw_card():
    cards, newest_card = draw_bingo_card()
    return redirect('/')

@app.route('/delete_last_card', methods=['GET','POST'])
def delete_last_card():
    delete_last_drawn_card()
    return redirect('/')