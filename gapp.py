import tkinter as tk
import pprint as pp
from gaudio import *

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(
            self,
            master
        )
        self.bind("<Button-1>", self.clickCallback)
        self.pack(fill=tk.BOTH, expand=True)
        self.createWidgets(master)

    def clickCallback(self,event):
        print ("clicked at", event.x, event.y)

    def createWidgets(self,master):

        self.DRAW = tk.Canvas(
            self,
            width=600,
            height=230
        )
        self.DRAW.pack(side="top")
        self.DRAW.create_oval(30,30,60,60)

        self.PLAY = tk.Button(
            self,
            borderwidth=1,
            relief="groove",
            bg="white",
            font=("Arial", 10)
        )
        self.PLAY["text"] = "play"
        self.PLAY["command"] = play
        self.PLAY.pack()

        self.QUIT = tk.Button(
            self,
            text="quit",
            command=master.destroy,
            borderwidth=1,
            relief="groove",
            bg="white",
            font=("Arial", 10)
        )
        self.QUIT.pack()
