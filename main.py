import tkinter
from snake import snake

root = tkinter.Tk()
root.title("Snake")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=500, height=500)
canvas.pack()

root.mainloop()
