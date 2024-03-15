import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# defining fonts
font = pygame.font.SysFont('Times New Roman', 30)

# defining game variables
margin = 50
player_score = 0

# colours
back_ground = (25, 15, 164)

def draw_board():
    screen.fill(back_ground)
    pygame.draw.line(screen, (255, 255, 255), (0, margin), (SCREEN_WIDTH, margin))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 100, 20)
        self.speed = 7

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.move_ip(-1 * self.speed, 0)
        elif key[pygame.K_d]:
            self.rect.move_ip(self.speed, 0)
        elif key[pygame.K_LEFT]:
            self.rect.move_ip(-1 * self.speed, 0)
        elif key[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

paddle = Paddle(SCREEN_WIDTH//2, SCREEN_HEIGHT-50)

run = True
while run:

    draw_board()
    draw_text('TEXT', font, (255, 255, 255), 20, 10)

    # drawing
    paddle.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()