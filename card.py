import numpy as np
import json
from data import details


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
        card_rows += curr_row
        data.append(curr_row) 
    return card_rows

def make_detail_card_rows():
    my_card = make_card_rows()
    res = []
    for i in range(len(my_card)):
        # truncate to max 20 char
        if i == len(my_card)//2: 
            res.append("Free")
        else:
            res.append(details[i][:20])
    
    return ["B", "I", "N", "G", "O"] + res

        


def make_json_cards(filename):
    my_card = make_card_rows()
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_card, f, indent=4)

def get_and_format_lorem_ipsum():
    try:
        content = ""
        with open('data/lorem_ipsum.txt', 'r') as file:
            content = file.read()
            file.close()
        items = [s for s in content.split("\n") if s != ""]
        with open('data.py','w') as f:
            my_string = "details = [\"" + "\", \n\"".join(items) + "\"]"
            f.write(my_string)
        # with open('lorem_ipsum.json', 'w', encoding='utf-8') as f:
        #     json.dump(items[:76], f, indent=4)

    except FileNotFoundError:
        print("Error: The file 'lorem_ipsum.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")