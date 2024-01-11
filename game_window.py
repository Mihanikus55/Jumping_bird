import pygame


class GameWindow:
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.gamemode = self.settings.gamemode
        self.buttons = pygame.sprite.Group()

    def update(self):
        for layer in self.settings.game_background:
            self.screen.blit(layer, (0, 0))



