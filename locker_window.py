import pygame


class Locker:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.buttons = pygame.sprite.Group()

    def update(self):
        self.screen.blit(self.settings.locker_bg, (0, 0))

    def change_clothes(self):
        pass

    def save_avatar(self):
        pass
