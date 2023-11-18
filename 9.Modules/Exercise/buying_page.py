from json import load, dump         # import load for reading json file
from tkinter import Button

from canvas import frame, root      # import frame
from PIL import Image, ImageTk      # import image represent and image display
from helpers import clean_screen    # import clean screen


def display_products():     # after successful login
    clean_screen()          # clear screen
    display_stock()         # display stock db (products.json)


def display_stock():
    global info

    with open("db/products_data.json", 'r') as stock:       # open file with products data dictionary (db)
        info = load(stock)                                  # make variable for products like strings

    x, y = 150, 50      # like in matrix fill indexes       # first item position

    for item_name, item_info in info.meds():               # iterate true info and take name and info dict
        # for opening images --> terminal pip install Pillow
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))   # take image from products_data.json["image"] path
        images.append(item_img)                                         # save current image in list to present all

        frame.create_text(x, y, text=item_name, font=("Cosmic Sans MS", 15))    # create text to every image
        frame.create_image(x, y + 100, image=item_img)                          # create image frame for every image

        if item_info["quantity"] > 0:                       # if quantity is more than 0
            color = "green"                                 # set green color of the text
            text = f'In stock: {item_info["quantity"]}'     # set the text

            item_btn = Button(              # set button to buy
                root,                       # set root for button
                text="Buy",                 # set text
                font=("Comic Sans MS", 12), # set font
                bg="green",                 # set back ground color
                fg="white",                 # set front ground color
                width=5,                    # set width
                # key moment --> call lambda and save current item name
                command=lambda z=item_name: buy_product(z)      # after button is triggered, quantity is decreased by 1
            )

            frame.create_window(x, y + 230, window=item_btn)        # set button location
        else:                           # if stock is 0
            color = "red"               # set color of text
            text = "Out of stock"       # set text

        frame.create_text(x, y + 180, text=text, font=("Comic Sans MS", 12), fill=color)    # set location of the text

        x += 200        # on every loop fill new index in display matrix with add 200 to x

        if x > 550:     # if x is at the end of the display matrix
            x = 150     # reset x to star position
            y += 230    # add 230 to y, nex index of screen matrix


def buy_product(name_of_product):                                      # create function for buying products
    info[name_of_product]["quantity"] -= 1                      # subtract quantity when buy product

    with open("db/products_data.json", 'w') as stock:   # open db file
        dump(info, stock)                               # save quantity

    display_products()                                  # refresh display products


images = []             # create list to append every image true for cycle
info = {}               # create dictionary for buying products
