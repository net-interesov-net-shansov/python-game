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
        self.y = -2

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:

                self.score.hit()

                return True
    
    def draw(self):
        
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:

            self.y = 2
        if pos[3] >= self.canvas_height:

            self.hit_bottom = True
            canvas.create_text(250, 120, text='You Looose', font=('Courier', 30), fill='red')

            if self.hit_paddle(pos) == True
        
