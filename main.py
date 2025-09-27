import numpy as np


def get_random_row():
    return np.random.randint([1,16,31,46,61], [16,31,46,61,75])

# def get_random_num():


def make_card():
    card = []

    for i in range(5):
        curr_row = get_random_row().tolist()
        if i == 2:
            curr_row[2] = "Free"
        print(curr_row)

make_card()