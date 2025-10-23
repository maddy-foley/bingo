import random
import json

def get_column_letter(n):
    keys = ["b","i","n","g","o"]
    return keys[n // 15]

def nums_to_card(numbers):
    data = get_bingo_data()
    res = [[] for key in range(5)]
    if isinstance(numbers,list):
        for i in numbers:
            key = get_column_letter(i)
            res[i//15].append(data[key][i%15])
    else:
        i = numbers
        key = get_column_letter(i)
        res = data[key][i%15]

    return res

def get_all_formated_drawn_cards():
    data = get_drawn_card_data()
    newest_card = None
    newest_card_column = None
    if data != []:
        newest_card = nums_to_card(data[-1])
        newest_card_column = get_column_letter(data[-1])

    return nums_to_card(data), newest_card, newest_card_column

def draw_bingo_card():
    random_integer = random.randint(0, 74)
    data = get_drawn_card_data()
    while random_integer in data:
        random_integer = random.randint(0, 74)
    data.append(random_integer)

    save_drawn_card_data(data)

    return nums_to_card(data), nums_to_card(random_integer)


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
    
def delete_last_drawn_card():
    data = get_drawn_card_data()
    if len(data) <= 0:
        return 
    data.pop()
    save_drawn_card_data(data)
    return True
    

def delete_all_drawn_cards():
    save_drawn_card_data([])
    is_deleted = get_drawn_card_data() == []
    return is_deleted
