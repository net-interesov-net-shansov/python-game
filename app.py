import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_SIZE = 12
BRICK_WIDTH, BRICK_HEIGHT = 75, 30
WHITE, RED, BLUE, YELLOW, GREEN, BLACK = (255, 255, 255), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (0, 0, 0)
BACKGROUND = pygame.image.load('img/background.jpg')
BACKGROUND1 = pygame.image.load('img/background1.jpg')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()

class Paddle:
    def __init__(self):
        self.x = WIDTH // 2 - PADDLE_WIDTH // 2
        self.y = HEIGHT - 40
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = WHITE
        self.speed = 70
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=20)
    
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = BALL_SIZE
        self.color = WHITE
        self.dx = 4.8
        self.dy = -4.5
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x >= WIDTH:
            self.dx = -self.dx
        if self.y <= 0:
            self.dy = -self.dy

class Brick:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = BRICK_WIDTH
        self.height = BRICK_HEIGHT
        self.color = color
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

def main_menu():
    while True:
        screen.blit(BACKGROUND, (0, 0))
        font1 = pygame.font.Font('fonts/Geon.otf', 90)
        font = pygame.font.Font('fonts/Geon.otf', 50)
        text = font1.render("Arkanoid", 1, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))
        
        start_btn = font.render("Start Game", 1, WHITE)
        start_btn_rect = start_btn.get_rect(center=(WIDTH // 2, 200))
        screen.blit(start_btn, start_btn_rect)
        
        quit_btn = font.render("Quit", 1, WHITE)
        quit_btn_rect = quit_btn.get_rect(center=(WIDTH // 2, 300))
        screen.blit(quit_btn, quit_btn_rect)

        controls = pygame.image.load('img/controls.png')
        screen.blit(controls, (WIDTH // 2 - controls.get_width() // 2, 300))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn_rect.collidepoint(event.pos):
                    game_loop()
                elif quit_btn_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def game_loop():
    paddle = Paddle()
    ball = Ball()
    bricks = [Brick(x * (BRICK_WIDTH + 5), y * (BRICK_HEIGHT + 5), WHITE) for y in range(5) for x in range(WIDTH // (BRICK_WIDTH + 5))]

    running = True
    while running:
        screen.blit(BACKGROUND1, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle.move("left")
                elif event.key == pygame.K_RIGHT:
                    paddle.move("right")
                elif event.key == pygame.K_a:
                    paddle.move("left")
                elif event.key == pygame.K_d:
                    paddle.move("right")

        ball.move()

        
        if ball.y + BALL_SIZE > paddle.y and ball.x > paddle.x and ball.x < paddle.x + paddle.width:
            ball.dy *= -1
        for brick in bricks[:]:
            if brick.x < ball.x < brick.x + brick.width and brick.y < ball.y < brick.y + brick.height:
                bricks.remove(brick)
                ball.dy *= -1
                break

        if ball.y > HEIGHT:
            running = False
            main_menu()

        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

def main():
    main_menu()

if __name__ == "__main__":
    main()