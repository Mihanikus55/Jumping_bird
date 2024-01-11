import pygame
from settings import Settings


class Locker:
    def __init__(self, screen):
        self.settings = Settings()
        self.buttons = pygame.sprite.Group()
        self.screen = screen


    def update_screen(self):
        self.screen.blit(self.settings.starting_bg, (0, 0))
