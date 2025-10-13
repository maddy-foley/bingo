import scribus
from make_card import make_detail_card_rows
from filename import filename

origX = 1.2
origY = 5.2

my_card = make_detail_card_rows(filename)

box_width=5
box_height=5

# 5 columns
for i in range(5):
    column = f"column{i}"
    scribus.createText(origX,origY,1,6,column)
    scribus.setTextAlignment(scribus.ALIGN_CENTERED, column)
    scribus.setLineColor("Black",column)
    scribus.setFontSize(18,column)
    scribus.setFont("Roman", column)
    for j in range(5):
        scribus.insertText(my_card[i+j], -1, column)
        scribus.insertText( "\n\n",-1, column)
        origY += 1.2
    break
    origY = 6
    origX += 1.2