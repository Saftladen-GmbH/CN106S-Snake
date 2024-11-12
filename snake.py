import tkinter as tk
import random


class snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake = None
        self.speed = 100
        self.last_pos = []
        self.tail = []
        self.collected = 0
        self.x = 0
        self.y = 0

    def create_snake(self):
        self.snake = self.canvas.create_rectangle(0, 0, 10, 10, fill="black")

    def move(self):
        self.last_pos = [self.canvas.coords(self.snake)]
        self.canvas.move(self.snake, self.x, self.y)
        # ? Uncomment the following lines to make the snake move continuously
        # self.x = 0
        # self.y = 0

    def kill(self):
        self.canvas.delete(self.snake)
        self.canvas.create_text(
            250, 250, text="Game Over", font=("Arial", 20), fill="red"
        )

    def border_collision(self):
        if len(self.canvas.coords(self.snake)) <= 0:
            return True
        elif self.canvas.coords(self.snake)[0] < 0:
            self.kill()
        elif self.canvas.coords(self.snake)[1] < 0:
            self.kill()
        elif self.canvas.coords(self.snake)[2] > 500:
            self.kill()
        elif self.canvas.coords(self.snake)[3] > 500:
            self.kill()

    def clean_pos(self):
        if len(self.tail) < len(self.last_pos):
            self.last_pos.pop(-1)

    def speed_up(self):
        self.speed -= 10

    def update_tail(self):
        for i in range(len(self.tail)):
            self.canvas.move(self.tail[i], self.last_pos[i][0], self.last_pos[i][1])

    def grow(self):
        x = self.last_pos[0][0]
        y = self.last_pos[0][1]
        self.tail.append(self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="black"))

    def collect_food(self):
        if self.canvas.coords(self.snake) == self.canvas.coords(self.food):
            self.collected += 1
            self.speed_up()
            self.canvas.delete(self.food)
            self.grow()
            self.generate_food()

    def generate_food(self):
        x = random.randrange(0, 500, 10)
        y = random.randrange(0, 500, 10)
        self.food = self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red")

    def update(self):
        self.clean_pos()
        print(self.last_pos)
        if not self.border_collision():
            self.move()
            self.collect_food()
            self.canvas.after(self.speed, self.update)

    def control(self, event):
        if event.keysym == "Up":
            self.y = -10
            self.x = 0
        elif event.keysym == "Down":
            self.y = 10
            self.x = 0
        elif event.keysym == "Left":
            self.x = -10
            self.y = 0
        elif event.keysym == "Right":
            self.x = 10
            self.y = 0
