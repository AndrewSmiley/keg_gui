from Tkinter import *
import os

"""
Just an extended class to allow us to prioritize the buttons added
"""


class GEButton(Button):
    def __init__(self, priority, *args, **kwargs):
        # priority just tells us where it lands left to right, top to bottom
        self.priority = priority
        super(GEButton, self).__init__(*args, **kwargs)


class GECanvas(Tk,object):
    def __init__(self, h, w):
        self.h = h
        self.w = w
        super(GECanvas, self).__init__()
    def build_ge_canvas(self):
        # self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.w, self.h))


def button_callback():
    print "button click"


# just create an array of buttons

def build_button(parent, image_name, func):
    photo = PhotoImage(file=image_name)
    B1 = Button(parent, image=photo, command=func)
    B1.pack()


def place_buttons(buttons):
    pass


buttons = []

print os.getcwd()
# top = Tk()
# make it cover the entire screen
w, h = 800, 480  # top.winfo_screenwidth(), top.winfo_screenheight()
canvas = GECanvas(h, w)
# top.overrideredirect(1)
# top.geometry("%dx%d+0+0" % (w, h))
canvas.build_ge_canvas()
# Code to add widgets will go here...
photo = PhotoImage(file="button.gif")
B1 = Button(canvas, image=photo, command=button_callback)
B1.pack()
# x is where it's placed Left to right, y is top to buttom, images are placed by 0,0
first_button_x, first_button_y = (w / 2) - (photo.width() / 2), (h / 2) - (photo.height() / 2)
B1.place(x=(w / 2) - ((photo.width() / 2) - 50), y=(h / 2) - (photo.height() / 2))

B2 = Button(canvas, image=photo, command=button_callback)
B2.pack()
# x is where it's placed Left to right, y is top to buttom
B2.place(x=first_button_x - (photo.width()), y=first_button_y)
# B2.place(x=(w/2)-(photo.width()/2)*2, y=(h/2)-(photo.height()/2))

B3 = Button(canvas, image=photo, command=button_callback)
B3.pack()
# x is where it's placed Left to right, y is top to buttom
B3.place(x=(w / 2) + (photo.width() / 2) * 2, y=(h / 2) - (photo.height() / 2))
canvas.mainloop()
