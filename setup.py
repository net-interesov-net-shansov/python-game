from tkinter import *
import time
import random

tk = Tk()
tk.title('Python Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=1000, height=800, highlightthickness=0)  # изменено разрешение
canvas.pack()
tk.update()


class Ball:

    def __init__(self, canvas, paddle, score, color):

        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 500, 400)  # зависит от разрешения

        starts = [-20, -10, 10, 20]

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
        return False

    def draw(self):

        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 5
        if pos[3] >= self.canvas_height:

            self.hit_bottom = True
            canvas.create_text(500, 400, text='You Looose', font=('Courier', 30), fill='red')

        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):

        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 20, fill=color)

        start_1 = [40, 60, 90, 120, 150, 180, 200, 400, 450, 500, 550, 600, 670, 850, 900, 960]
        random.shuffle(start_1)

        self.starting_point_x = start_1[0]
        self.canvas.move(self.id, self.starting_point_x, 700)
        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

        self.started = False

        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def turn_right(self, event):
        self.x = 4
    def turn_left(self, event):
        self.x = -4
    def start_game(self, event):
        self.started = True
    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

class Score:
    def __init__(self, canvas, color):

        self.score = 0
        self.canvas = canvas

        self.id = canvas.create_text(900, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

score = Score(canvas, 'blue')
paddle = Paddle(canvas, 'White')
ball = Ball(canvas, paddle, score, 'Grey')

while not ball.hit_bottom:
    if paddle.started == True:

        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.009)
time.sleep(3)
