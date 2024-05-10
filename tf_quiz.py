from tkinter import *
import random 
import stopwatch

ORANGE_COLOUR = '#FFb800'
YELLOW_COLOUR = '#FFF370'
FONT = None


class TF_Quiz():
    def __init__(self):
        self.tf_window = Tk() 
        self.tf_window.title('True/False')
        self.tf_window.minsize(width=500,height=400)
        self.tf_window.maxsize(width=500,height=400)
        self.tf_window.config(bg=YELLOW_COLOUR)
        self.app_name = Label(text = 'Math Minds', fg=ORANGE_COLOUR, bg=YELLOW_COLOUR, font=("Segoe UI Black", 35))
        self.app_name.place(x=115,y=20)

        self.tf_window.mainloop()