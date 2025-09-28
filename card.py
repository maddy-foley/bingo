import numpy as np
import json


def get_random_row(card_rows):

    my_list = np.random.randint([1,16,31,46,61], [16,31,46,61,76]).tolist()

    for item in my_list: 
        if item in card_rows:
            return get_random_row(card_rows)
    return my_list

def make_card_rows():
    card_rows = []
    data = []
    for i in range(5):
        curr_row = get_random_row(card_rows)
        if i == 2:
            curr_row[2] = "Free"
        card_rows += curr_row
        data.append(curr_row)
    return data

def make_card():
    my_card = [["B","I","N","G","O"]]
    my_card += make_card_rows()
    return my_card

def make_json_cards(filename):
    my_card = make_card()
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_card, f, indent=4)

make_json_cards("test.json")