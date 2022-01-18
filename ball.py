from random import choice
import pygame

from constants import *

class Ball:
    def __init__(self, screen):
        self.screen = screen

        self.reset()

    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.handle_wall_collision()
        self.handle_screen_out()

    def render(self):
        pygame.draw.ellipse(self.screen, WHITE_COLOR, self.rect)

    def reset(self):
        self.rect = pygame.Rect(
            HALF_WINDOW_WIDTH - BALL_SIZE//2,
            HALF_WINDOW_HEIGHT - BALL_SIZE//2,
            BALL_SIZE,
            BALL_SIZE)
        self.velocity_x = choice([-BALL_SPEED, BALL_SPEED])
        self.velocity_y = choice([-BALL_SPEED, BALL_SPEED])

    def handle_wall_collision(self):
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity_y *= -1
        elif self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.velocity_y *= -1

    def handle_screen_out(self):
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.reset()

    def collides_with(self, object):
        return self.rect.colliderect(object)