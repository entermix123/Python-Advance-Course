from tkinter import Tk, Canvas              # import functional module Tkinter


def create_root():                          # root function
    root = Tk()                             # var root is main function

    root.title('Headline')           # HEADLINE
    root.resizable(False, False)     # cant be resized ot full screened
    root.geometry('700x600')         # size of the window # can be set offset like root.geometry('700x600+1000+200')

    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)     # create Canvas frame
    frame.grid(row=0, column=0)                     # put invisible layer (the frame) over the root geometry

    return frame


root = create_root()
frame = create_frame()


