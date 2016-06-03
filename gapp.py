import tkinter as tk
import pprint as pp
from gaudio import *

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(
            self,
            master
        )
        self.bind("<Button-1>", self.callback)
        self.pack(fill=tk.BOTH, expand=True)
        self.createWidgets(master)

    def callback(self,event):
        print ("clicked at", event.x, event.y)

    def createWidgets(self,master):
        self.PLAY = tk.Button(
            self,
            borderwidth=1,
            relief="ridge",
            bg="white",
            font=("Arial", 10)
        )
        self.PLAY["text"] = "play"
        self.PLAY["command"] = self.play
        self.PLAY.pack()

        self.QUIT = tk.Button(
            self,
            text="quit",
            command=master.destroy,
            borderwidth=1,
            relief="ridge",
            bg="white",
            font=("Arial", 10)
        )
        self.QUIT.pack()

    def play(self):
        stream = p.open(format=p.get_format_from_width(1),
                        channels=1,
                        rate=BITRATE,
                        output=True)
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()
        p.terminate()