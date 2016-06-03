import tkinter as tk
import pprint as pp


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
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

root = tk.Tk()
app = Application(master=root)
app.mainloop()
