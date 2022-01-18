import pygame

from constants import *
from math_utils import clamp

class Paddle:
    def __init__(self, x, y, screen):
        self.screen = screen

        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.velocity_y = 0

    def update(self):
        self.rect.y += self.velocity_y
        self.rect.y = clamp(self.rect.y, 0, WINDOW_HEIGHT - PADDLE_HEIGHT)

    def render(self):
        pygame.draw.rect(self.screen, WHITE_COLOR, self.rect)