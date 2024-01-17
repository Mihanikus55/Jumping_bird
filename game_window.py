import pygame


class GameWindow:
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.gamemode = self.settings.gamemode
        self.buttons = pygame.sprite.Group()

    def update(self):
        self.settings.game_background.update(self.screen, self.settings.game_is_running)




