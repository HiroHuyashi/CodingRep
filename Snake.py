import pygame 
import random

pygame.init()

WIDTH, HEIGHT = 600,400
SNAKE = [(100,100), (80,100), (60,100)]
BLOCK_SIZE = 20
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0,)
WHITE = (255,255,255)
RUNNING = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
SNAKE_DIRECTION = (BLOCK_SIZE,0)
CLOCK = pygame.time.Clock()
SCORE=0
font=pygame.font.SysFont(None, 48)


def generate_food():
    return (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE, random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

FOOD = generate_food()

def draw_food(FOOD):
    pygame.draw.rect(screen, RED, (*FOOD, BLOCK_SIZE, BLOCK_SIZE))

def draw_snake(SNAKE):
    for segment in SNAKE:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

def draw_score(SCORE):
    text_surface = font.render(str(SCORE),True,WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT-50))

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and SNAKE_DIRECTION != (0, BLOCK_SIZE):
                SNAKE_DIRECTION = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and SNAKE_DIRECTION != (0, -BLOCK_SIZE):
                SNAKE_DIRECTION = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and SNAKE_DIRECTION != (BLOCK_SIZE, 0):
                SNAKE_DIRECTION = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and SNAKE_DIRECTION != (-BLOCK_SIZE, 0):
                SNAKE_DIRECTION = (BLOCK_SIZE, 0)

    new_head = (SNAKE[0][0] + SNAKE_DIRECTION[0], SNAKE[0][1] + SNAKE_DIRECTION[1])
    SNAKE.insert(0, new_head)
    if new_head == FOOD:
        FOOD = generate_food()
        SCORE+=1
    else:
        SNAKE.pop()
    
    screen.fill((BLACK))
    draw_snake(SNAKE)
    draw_food(FOOD)
    draw_score(SCORE)
    screen.blit(font.render(str(SCORE),True,WHITE), (WIDTH//2,HEIGHT-50))
    pygame.display.flip()

    CLOCK.tick(10)