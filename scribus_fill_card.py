
from make_card import make_detail_card_rows
from filename import filename, img_filename
from test import check_overflow


def set_styles(cell_style, cell_name):
    scribus.setTextAlignment(cell_style['alignmentX'], cell_name)
    scribus.setTextVerticalAlignment(cell_style['alignmentY'], cell_name)
    # scribus.setLineColor(cell_style['font_color'],cell_name)
    scribus.setFontSize(cell_style['font_size'],cell_name)
    # Some font is not included with scribus and needs to be downloaded manually
    scribus.setFont(cell_style['font_name'], cell_name)


def draw_content_boxes(cell_style, free_space=None):
    origX = cell_style['origX']
    origY = cell_style['origY']
# 5 columns
    for i in range(25):
        if i % 5 == 0:
            origY = cell_style['origY']
            origX +=  cell_style["orig_shiftX"]

        cell = f"cell{i}"
        if free_space and i == free_space['idx']:
            scribus.createImage(origX+.05, origY + .05, 1,1,cell)
        else:
            scribus.createText(origX, origY, cell_style['cell_width'],cell_style['cell_height'],cell)
            set_styles(cell_style,cell)
        origY +=  cell_style["orig_shiftY"]


def fill_box_with_text(free_space=None):
    my_card = make_detail_card_rows(filename)
    for i in range(25):
        cell = f"cell{i}"
        if free_space and i == free_space['idx']:
            scribus.loadImage(free_space['filename'], cell)
            scribus.setScaleImageToFrame(True,True,cell)
            scribus.setCornerRadius(25, cell)
        elif i == 12:
            scribus.insertText("FREE", -1, cell)
        else:
          
            scribus.insertText(my_card[i], -1, cell)
            check_overflow(cell, my_card[i])

        # remove cell lines
        scribus.setLineWidth(0, cell)

def make_title_boxes(cell_style):
    origX = cell_style['origX']
    origY = cell_style['origY']

    for letter in ["B","I","N","G","O"]:
        cell = f"{letter}"
        scribus.createText(origX, origY, cell_style['cell_width'],cell_style['cell_height'],cell)
        set_styles(cell_style,cell)
        scribus.insertText(letter, -1, cell)
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
            scribus.deleteObject(cell)



title_cell_style = {
    "font_name":"Ultra Regular" ,
    "font_color":"Black",
    "font_size": 30,
    "origX":1.25,
    "origY":4.1,
    "cell_width": 1.1,
    "cell_height":1,
    "alignmentX": scribus.ALIGN_CENTERED,
    "alignmentY": scribus.ALIGNV_TOP,
    "orig_shiftX": 1.2,
    "orig_shiftY": 0
}
# test 1 uses 18pt
# test 2 uses 16pt

other_cell_style = {
    "font_name": "EB Garamond Bold",
    "font_color":"Black",
    "font_size": 16,
    "origX":0.05,
    "origY":4.9,
    "cell_width": 1.1,
    "cell_height":1.05,
    "alignmentX": scribus.ALIGN_CENTERED,
    "alignmentY": scribus.ALIGNV_CENTERED,
    "orig_shiftX": 1.2,
    "orig_shiftY": 1.1 
}

free_space_cell = {
    "filename": img_filename,
    "idx":12
}
# dev delete boxes to quickly redo-boxes
delete_all_boxes()
make_title_boxes(title_cell_style)
draw_content_boxes(other_cell_style, free_space_cell)
fill_box_with_text(free_space_cell)