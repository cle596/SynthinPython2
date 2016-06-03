import tkinter as tk
import pprint as pp
from gaudio import *
from gapp import *

root = tk.Tk()

w = 600
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.wm_title("Giorgio Synth Looper")
root.configure(bg="white", width=1000)

app = Application(master=root)
app.mainloop()
