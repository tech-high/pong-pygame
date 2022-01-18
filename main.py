from sys import exit
import pygame

from ball import Ball
from constants import *
from paddle import Paddle

screen = None
clock = None

left_paddle = None
right_paddle = None
ball = None

def init():
    global screen, clock, left_paddle, right_paddle, ball

    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    left_paddle = Paddle(PADDLE_OFFSET_X, HALF_WINDOW_HEIGHT - PADDLE_HEIGHT//2, screen)
    right_paddle = Paddle(
        WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_OFFSET_X,
        HALF_WINDOW_HEIGHT - PADDLE_HEIGHT//2,
        screen)
    ball = Ball(screen)

def main():
    init()
    while True:
        process_events()
        update()
        render()

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dispose()
        handle_paddle_movement(left_paddle, event, pygame.K_w, pygame.K_s)
        handle_paddle_movement(right_paddle, event, pygame.K_UP, pygame.K_DOWN)

def update():
    left_paddle.update()
    right_paddle.update()
    ball.update()
    handle_paddles_ball_collision()
    clock.tick(FPS)

def render():
    screen.fill(BG_COLOR)
    left_paddle.render()
    right_paddle.render()
    ball.render()
    pygame.display.flip()

def dispose():
    pygame.quit()
    exit()

def handle_paddle_movement(paddle, event, k_up, k_down):
    if event.type == pygame.KEYDOWN:
        if event.key == k_up:
            paddle.velocity_y -= PADDLE_SPEED
        if event.key == k_down:
            paddle.velocity_y += PADDLE_SPEED
    elif event.type == pygame.KEYUP:
        if event.key == k_up:
            paddle.velocity_y += PADDLE_SPEED
        if event.key == k_down:
            paddle.velocity_y -= PADDLE_SPEED

def handle_paddles_ball_collision():
    if ball.collides_with(left_paddle):
        ball.rect.left = left_paddle.rect.right
        ball.velocity_x *= -1
    elif ball.collides_with(right_paddle):
        ball.rect.right = right_paddle.rect.left
        ball.velocity_x *= -1

if __name__ == '__main__':
    main()