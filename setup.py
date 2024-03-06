import pygame
from tkinter import *
import time
import random

tk = Tk()
tk.title('Python Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=1920, height=1080, highlightthickness=0) #изменено разрешение
canvas.pack()
tk.update()


class Ball:

    def __init__(self, canvas, paddle, score, color):

        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 960, 200) #зависит от разрешения

        starts = [-2, -1, 1, 2]

        random.shuffle(starts)

        self.x = starts[0]
        self.y = starts[1]
        