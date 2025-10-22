import scribus
from test import check_overflow
import json
from filename import *


COL_COLORS_CMYK = [("pink",0,20,10,0),("blue",30,15,0,0),("red",0,65,50,0),("yellow",0,0,25,0),("green",12,0,20,0)]

"""
generate table for drawing bingo cards cells
3 pages
U.S. Letter landscape
"""
def set_styles(cell_style, cell_name, col_num):
    scribus.setTextAlignment(cell_style['alignmentX'], cell_name)
    scribus.setTextVerticalAlignment(cell_style['alignmentY'], cell_name)
    # scribus.setLineColor(cell_style['font_color'],cell_name)
    scribus.setFontSize(cell_style['font_size'],cell_name)
    # Some font is not included with scribus and needs to be downloaded manually
    scribus.setFont(cell_style['font_name'], cell_name)
    scribus.setFillColor(COL_COLORS_CMYK[col_num][0], cell_name)
    scribus.setLineSpacing(20, cell_name)

    scribus.setLineColor("brown", cell_name)

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

        cell_name = f"cell{i}"
        scribus.createText(origX, origY, cell_style['cell_width'],cell_style['cell_height'],cell_name)
        set_styles(cell_style, cell_name, i // 15)
        origY += cell_style['cell_height']



def fill_boxes(my_bingo_json_file):

    with open(my_bingo_json_file, 'r') as file:
        data = json.load(file)
        for i, key in enumerate(data):
            for j, value in enumerate(data[key]):

                cell = f"cell{j + (i * 15)}"

                scribus.insertText(str(key.upper() + "\n\n"),-1, cell)
                scribus.insertText(str(value),-1, cell)
            

def delete_all_boxes():
    for i in range(75):
        cell = f"cell{i}"
        if scribus.objectExists(cell):
            scribus.deleteText(cell)
            scribus.deleteObject(cell)

def style(colors_cmyk):
    for item in colors_cmyk:
        scribus.defineColorCMYK(*item)
    scribus.defineColor("brown",70,100,100,15)
             

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
    "font_size": 22,
    "origX":0.5,
    "origY":0.5,
    "cell_width": usable_page_width/5,
    "cell_height": usable_page_height/5,
    "alignmentX": scribus.ALIGN_CENTERED,
    "alignmentY": scribus.ALIGNV_CENTERED
}


delete_all_boxes()

# add cmyk colors
style(COL_COLORS_CMYK)
draw_content_boxes(cell_style)
fill_boxes(filename)
