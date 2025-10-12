import random
import json

def make_random_cell_data():
    res = {'b':[],'i':[],'n':[],'g': [],'o': []}
    for key in res:
        while len(res[key]) < 5:
            rand_num = random.randint(0, 14)
            if rand_num not in res[key]:
                res[key].append(rand_num)
    return res



def make_detail_card_rows(filename):
    my_card = make_random_cell_data()
    res = []
    with open(filename, 'r') as file:
        data = json.load(file)
        keys = ['b','i','n','g','o']
        for key in keys:
            for idx in my_card[key]:
                res.append(data[key][idx])

    return res

  

# data from raw textfile -> json file w/ bingo dictionary
def get_and_format_bingo_data():
    try:
        content = {'b':[],'i':[],'n':[],'g':[],'o':[]}
        for key in content:

            with open(f'data/{key}.txt', 'r') as file:
                temp = []
                for line in file.readlines():
                    temp.append(line.strip())
                content[key] = temp
                file.close()
        with open('data/bingo.json', 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=4)
    # except FileNotFoundError:
    #     print("Error: The file 'lorem_ipsum.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")