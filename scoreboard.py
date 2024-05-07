import tkinter as tk 


ORANGE_COLOUR = '#FFb800'
YELLOW_COLOUR = '#FFF370'
FONT = None

class Scoreboard():
    def __init__(self):
        self.scoreboard_window = tk.Tk()
        self.scoreboard_window.title('Scoreboard')
        self.scoreboard_window.minsize(width=500, height=400)
        self.scoreboard_window.maxsize(width=500, height=400 )
        self.scoreboard_window.config(bg=YELLOW_COLOUR)


        self.scoreboard_window.mainloop()


homepage = Scoreboard()