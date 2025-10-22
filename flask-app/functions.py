import random
import json

def draw_bingo_card():
    keys = ["b","i","n","g","o"]
    random_integer = random.randint(1, 75)
    with open('data/bingo.json', 'r') as file:
        data = json.load(file)
        print(data[keys[random_integer % 5]][random_integer % 15])
