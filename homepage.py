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

        self.mcq_button = Button(text='mcq', command=self.start_mcq)
        self.mcq_button.place(x=200,y=200)

        self.tf_button = Button(text='tf', command=self.start_tf)
        self.tf_button.place(x=200,y=250)

        self.scoreboard_button = Button(text='scoreboard', command=self.start_scoreboard)
        self.scoreboard_button.place(x=200,y=300)

        self.homepage_window.mainloop()

    def start_mcq(self):
        self.homepage_window.destroy()
        print('mcq has started')
    def start_tf(self):
        self.homepage_window.destroy()
        self.tf_quiz = tf_quiz.TF_Quiz()
        print('tf has started')
    def start_scoreboard(self):
        self.homepage_window.destroy()
        print('scoreboard has started')


homepage = HomePage()

