from tkinter import * 
import stopwatch

ORANGE_COLOUR = '#FFb800'
YELLOW_COLOUR = '#FFF370'
FONT = None

class TFQuiz():
    def __init__(self):
        self.TF_window = Tk()
        self.TF_window.title('Homepage')
        self.TF_window.minsize(width=500, height=400)
        self.TF_window.maxsize(width=500, height=400 )
        self.TF_window.config(bg=YELLOW_COLOUR)

        self.TF_window.mainloop()


homepage = TFQuiz()