import scribus
from make_card import make_detail_card_rows
from filename import filename

origX = 0.5
origY = 0.5

# scribus.createText(origX,origY,5,6,"Box1")
# scribus.insertText("testing", -1, "Box1")
my_card = make_detail_card_rows(filename)
scribus.createText(origX,origY,5,6,"Box1")
scribus.insertText(my_card[0], -1, "Box1")