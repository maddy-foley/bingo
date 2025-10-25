import json
import os
import random

# mostly file management for a game of bingo
class BingoDataManager:
    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name
        self.version = 0
        self.check_version()

    def check_version(self):
        if not os.path.exists(self.curr_file_name()):
            self.new_file()
        else:
            my_files = os.listdir(self.path)
            len([f for f in my_files if self.file_name in f])

    def get_all_files_from_path(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        
        files = os.listdir(self.path)
        return files
    
    def get_all_file_versions_data(self):
        data = []
        for f in self.get_all_files_from_path():
            if self.file_name in f:
                with open(self.path + '/' + f,'r') as file:
                    data += json.load(file)
                    file.close()
        return data
            
    def curr_file_name(self):
        curr_file_name = self.path + "/" + self.file_name + "_" + str(self.version) + ".json"
        return curr_file_name

    
    def save_data_to_curr_file(self, data):
        with open(self.curr_file_name(),'w') as file:
            json.dump(data,file,indent=4)
            file.close()

    def new_file(self):
        with open(self.curr_file_name(),'w') as file:
            json.dump([],file,indent=4)
            file.close()


    def get_curr_file_data(self):
        data = []
        with open(self.curr_file_name(),'r') as file:
            data = json.load(file)
            file.close()
        return data

    def delete_last_item(self):
        data = self.get_curr_file_data()
        if len(data) <= 0:
            return 
        data.pop()
        self.save_data_to_curr_file(data)

    def delete_all_files_with_file_name(self):
        for file in self.get_all_files_from_path():
            if self.file_name in file:
                try:
                    os.remove(file)
                except:
                    print(f"error removing{file}")
        self.version = 0
        self.new_file()




# basic bingo logic
class BingoManager(BingoDataManager):
    def __init__(self, path, file_name):
        super().__init__(path=path, file_name=file_name)
        self.columns = ["b","i","n","g","o"]
        self.rows = 15
        self.database = "data/bingo.json"


    def get_column_letter(self,num):
        return self.columns[num // self.rows]
    
    def get_bingo_data(self):
        with open(self.database, 'r') as file:
            data = json.load(file)
            file.close()
            return data
        
    def get_number_as_bingo_data(self, numbers):
        data = self.get_bingo_data()
        res = [[] for key in range(5)]
        if isinstance(numbers,list):
            for i in numbers:
                key = self.get_column_letter(i)
                res[i//15].append(data[key][i%15])
        else:
            i = numbers
            key = self.get_column_letter(i)
            res = data[key][i%15]

        return res
    
    def get_curr_file_formatted_data(self):
        data = self.get_curr_file_data()
        newest_card = None
        newest_card_column = None
        if data != []:
            n = data[-1]
            newest_card = self.get_number_as_bingo_data(n)
            newest_card_column = self.get_column_letter(n)

        return self.get_number_as_bingo_data(data), newest_card, newest_card_column
    
    def draw_random_available_bingo_card(self):
        random_integer = random.randint(0, 74)
        data = self.get_all_file_versions_data()
        while random_integer in data:
            random_integer = random.randint(0, 74)
        data.append(random_integer)

        self.save_data_to_curr_file(data)

        return self.get_number_as_bingo_data(data), self.get_number_as_bingo_data(random_integer)

# seperated just to keep it a little organized
# memory and file manager, and small bingo conversions
bingo = BingoManager("flask-app/data","bingo_round")