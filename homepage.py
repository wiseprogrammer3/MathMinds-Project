import mcq_quiz
import tf_quiz
import scoreboard
from tkinter import *


ORANGE_COLOUR = '#FFb800'
YELLOW_COLOUR = '#FFF370'
FONT = None

class HomePage():
    def __init__(self):
        self.homepage_window = Tk()
        self.homepage_window.title('Homepage')
        self.homepage_window.minsize(width=500, height=400)
        self.homepage_window.maxsize(width=500, height=400 )
        self.homepage_window.config(bg=YELLOW_COLOUR)
        self.app_name = Label(text = 'Math Minds', fg=ORANGE_COLOUR, bg=YELLOW_COLOUR, font=("Segoe UI Black", 35))
        self.app_name.place(x=115,y=20)

        self.mcq_button = Button(height=20,width=59, text = 'here')
        self.mcq_button.place(200,200)


        self.homepage_window.mainloop()


homepage = HomePage()