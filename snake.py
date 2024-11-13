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
