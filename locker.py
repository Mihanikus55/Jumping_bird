import pygame
from settings import Settings


class Locker:
    def __init__(self, screen):
        self.settings = Settings()
        self.buttons = pygame.sprite.Group()
        self.screen = screen

    def update_screen(self):
        self.screen.blit(self.settings.starting_bg, (0, 0))

    def change_clothes(self):
        pass

    def save_avatar(self):
        pass
