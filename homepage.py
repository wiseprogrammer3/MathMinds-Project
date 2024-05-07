import mcq_quiz
import tf_quiz
import scoreboard
import tkinter as tk 


ORANGE_COLOUR = '#FFb800'
YELLOW_COLOUR = '#FFF370'
FONT = None

class HomePage():
    def __init__(self):
        self.homepage_window = tk.Tk()
        self.homepage_window.title('Homepage')
        self.homepage_window.minsize(width=500, height=400)
        self.homepage_window.maxsize(width=500, height=400 )
        self.homepage_window.config(bg=YELLOW_COLOUR)
        self.app_name = tk.Label(text = 'Math Minds', fg=ORANGE_COLOUR, bg=YELLOW_COLOUR, font=("Chilanka", 35))
        self.app_name.place(x=115,y=20)

        self.homepage_window.mainloop()


homepage = HomePage()