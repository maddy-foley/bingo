import random
import json

def nums_to_card(numbers):
    data = get_bingo_data()
    keys = ["b","i","n","g","o"]
    res = [None] * 75

    for i in numbers:
        key = keys[i//15]
        res[i] = data[key][i % 15]
    return res

def draw_bingo_card():

    random_integer = random.randint(1, 75)
    data = get_drawn_card_data()
    while random_integer in data:
        random_integer = random.randint(1, 75)
    data.append(random_integer)
    save_drawn_card_data(data)

    return nums_to_card(data)


def get_drawn_card_data():
    with open('flask-app/data/drawn_cards.json','r') as file:
        data = json.load(file)
        file.close()
        return data

def save_drawn_card_data(data):
    with open('flask-app/data/drawn_cards.json','w') as file:
        json.dump(data,file,indent=4)
        file.close()

def get_bingo_data():
    with open('data/bingo.json', 'r') as file:
        data = json.load(file)
        file.close()
        return data