import tkinter
from snake import snake

root = tkinter.Tk()
root.title("Snake")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=500, height=500)
canvas.pack()
s = snake(canvas)
s.create_snake()
s.generate_food()
root.bind("<KeyPress>", lambda event: s.control(event))
s.update()
root.mainloop()
