import scribus
from make_card import make_detail_card_rows
from filename import filename


def draw_content_boxes(cell_style):
    origX = cell_style['origX']
    origY = cell_style['origY']
    cell_width = cell_style['cell_width']
    cell_height = cell_style['cell_height']
# 5 columns
    for i in range(25):
        if i % 5 == 0:
            origY = cell_style['origY']
            origX +=  cell_style["orig_shiftX"]

        cell = f"cell{i}"
        scribus.createText(origX,origY,cell_width,cell_height,cell)
        scribus.setTextAlignment(scribus.ALIGN_CENTERED, cell)
        scribus.setLineColor(cell_style['font_color'],cell)
        scribus.setFontSize(cell_style['font_size'],cell)

        # Font is not included with scribus and needs to be downloaded to OS system manually
        scribus.setFont(cell_style['font_name'], cell)
        origY +=  cell_style["orig_shiftY"]


def fill_box_with_text():
    my_card = make_detail_card_rows(filename)
    for i in range(25):
        cell = f"cell{i}"
        scribus.insertText(my_card[i], -1, cell)

def make_title_boxes(cell_style):
    origX = cell_style['origX']
    origY = cell_style['origY']

    for letter in ["B","I","N","G","O"]:
        cell = f"{letter}"
        scribus.createText(origX,origY, cell_style['cell_width'], cell_style['cell_height'], cell)
        scribus.insertText(letter, -1, cell)
        scribus.setTextAlignment(scribus.ALIGN_CENTERED, cell)
        scribus.setLineColor(cell_style['font_color'],cell)
        scribus.setFontSize(cell_style['font_size'],cell)
        scribus.setFont(cell_style['font_name'], cell)
        origX += cell_style["orig_shiftX"]

def delete_all_boxes():
    for letter in ["B","I","N","G","O"]:
        title_cell = f"{letter}"
        if scribus.objectExists(title_cell):
            scribus.deleteText(title_cell)
            scribus.deleteObject(title_cell)
    for i in range(25):
        cell = f"cell{i}"
        if scribus.objectExists(cell):
            scribus.deleteText(cell)
            scribus.deleteObject(cell)



title_cell_style = {
    "font_name":"Ultra Regular" ,
    "font_color":"Black",
    "font_size": 30,
    "origX":1.25,
    "origY":4.1,
    "cell_width": 1.1,
    "cell_height":1,
    "alignment": scribus.ALIGN_CENTERED,
    "orig_shiftX": 1.2,
    "orig_shiftY": 0
}

other_cell_style = {
    "font_name": "EB Garamond Bold",
    "font_color":"Black",
    "font_size": 18,
    "origX":0,
    "origY":4.9,
    "cell_width": 1.1,
    "cell_height":1,
    "alignment": scribus.ALIGN_CENTERED,
    "orig_shiftX": 1.2,
    "orig_shiftY": 1.1 
}
# dev delete boxes to quickly redo-boxes
delete_all_boxes()
# make_title_boxes(title_cell_style)
# draw_content_boxes(other_cell_style)
# fill_box_with_text()