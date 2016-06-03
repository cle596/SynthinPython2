import tkinter as tk
import pprint as pp
from audio import *

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(
            self,
            master
        )
        master.minsize(width=300, height=300)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(
            self,
            borderwidth=0,
            bg="white",
            highlightcolor="black",
            padx=10
        )
        self.hi_there["text"] = "play"
        self.hi_there["command"] = self.play
        self.hi_there.pack(side="left")

        self.QUIT = tk.Button(
            self,
            text="quit",
            fg="blue",
            command=root.destroy,
            borderwidth=0,
            bg="white",
            highlightcolor="black"
        )
        self.QUIT.pack(side="bottom")

    def play(self):
        print("playing music!")
        stream = p.open(format = p.get_format_from_width(1),
                        channels = 1,
                        rate = BITRATE,
                        output = True)
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()
        p.terminate()

root = tk.Tk()
root.wm_title("Giorgio Synth Looper")
app = Application(master=root)
app.mainloop()
