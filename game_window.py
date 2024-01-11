import pygame


class GameWindow:
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.gamemode = self.settings.gamemode
        self.buttons = pygame.sprite.Group()

    def update(self):
        for i in range(5):
            self.screen.blit(self.settings.load_paralax_background(self.settings.game_background)[i], (0, 0))



