import scribus
from test import check_overflow
import json
from filename import *

"""
generate table for drawing bingo cards cells
3 pages
U.S. Letter landscape
"""

def draw_content_boxes(cell_style):
    # for j in range(1, cell_style['pages'] + 1):
    #     scribus.gotoPage(j)
    page = 0
    origX = cell_style['origX']
    origY = cell_style['origY']

    for i in range(75):

        if i % 5 == 0:
            if page == 3:
                page = 0
                origX += cell_style['cell_width']
            page += 1
            scribus.gotoPage(page)
            origY = cell_style['origY']

        cell = f"cell{i}"
        scribus.createText(origX, origY, cell_style['cell_width'],cell_style['cell_height'],cell)
        origY += cell_style['cell_height']



def get_all_bingo_key_values(my_bingo_json_file):

    with open(my_bingo_json_file, 'r') as file:
        data = json.load(file)
        col = -1
        table_name = ""
        for key in data:
            col += 1
            table_num = 0
            for i, value in enumerate(data[key]):
                # i += 1
                row = (i) % 5
                if row == 0:
                    table_num += 1
                    table_name = f"bingo_table_{table_num}"
                text_string = f"{key.upper()}  {value}"
                scribus.setCellText(row,col,str(text_string),table_name)
            


def draw_tables(page_numbers):
    for i in range(1,page_numbers + 1):
        scribus.gotoPage(i)
        for j in range(5):
            scribus.createText()
def delete_all_boxes():
    # for letter in ["B","I","N","G","O"]:
    #     title_cell = f"{letter}"
    #     if scribus.objectExists(title_cell):
    #         scribus.deleteText(title_cell)
    #         scribus.deleteObject(title_cell)
    for i in range(75):
        cell = f"cell{i}"
        if scribus.objectExists(cell):
            scribus.deleteObject(cell)

def style():
    scribus.createCharStyle("my_text")
             

def remove_table(page_numbers):
    for i in range(1,page_numbers + 1):
        scribus.gotoPage(i)
        if scribus.objectExists(f"bingo_table_{i}"):
            scribus.deleteObject(f"bingo_table_{i}")


""" 
JSON Format
* there are exactly 15 values in each list *
{
    "b" : [word1,word2... word15],
    "i" : [...],
    "n" : [...],
    "g" : [...],
    "o" : [...]
}
"""
usable_page_height = 7.5
usable_page_width = 10

cell_style = {
    "font_name": "EB Garamond Bold",
    "font_color":"Black",
    "font_size": 20,
    "origX":0.5,
    "origY":0.5,
    "cell_width": usable_page_width/5,
    "cell_height": usable_page_height/5,
    "alignmentX": scribus.ALIGN_CENTERED,
    "alignmentY": scribus.ALIGNV_CENTERED
}


delete_all_boxes()
draw_content_boxes(cell_style)
# style()
# get_all_bingo_key_values(my_bingo_json_file=filename)
