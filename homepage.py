import mcq_quiz
import tf_quiz
import scoreboard
import tkinter as tk 


class HomePage():
    def __init__(self):
        homepage_window = tk.Tk()
        homepage_window.title('Homepage')
        homepage_window.minsize(width=500, height=400)
        homepage_window.maxsize(width=500, height=400 )
        

        homepage_window.mainloop()


homepage = HomePage()