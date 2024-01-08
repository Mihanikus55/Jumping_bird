import pygame

from btn import Button
from settings import Settings


class GameWindow:
    def __init__(self, screen):
        self.settings = Settings()
        self.screen = screen
        self.gamemode = self.settings.gamemode
        self.buttons = pygame.sprite.Group()

    def update(self):
        self.screen.fill(self.settings.bg_color)



