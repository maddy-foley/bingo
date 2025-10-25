from flask import Flask, render_template, redirect, request
from bingo_file_manager import bingo

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    cards, newest_card, newest_card_column = bingo.get_curr_file_formatted_data()
    return render_template("bingo.html", cards=cards, new_card=newest_card, newest_card_column=newest_card_column)

@app.route('/draw_card', methods=['GET','POST'])
def draw_card():
    cards, newest_card = bingo.draw_random_available_bingo_card()
    return redirect('/')

@app.route('/delete_last_card', methods=['GET','POST'])
def delete_last_card():
    bingo.delete_last_item()
    return redirect('/')

@app.route('/delete_all', methods=['GET','POST'])
def delete_all():
    bingo.delete_all_files_with_file_name()
    return redirect('/')