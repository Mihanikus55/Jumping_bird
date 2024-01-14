import pygame


class Shop:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.buttons = pygame.sprite.Group()

    def update(self):
        self.screen.blit(self.settings.shop_bg, (0, 0))

    def buy_skin(self):
        pass
