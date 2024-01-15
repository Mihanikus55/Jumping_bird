import pygame


class GameWindow:
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.gamemode = self.settings.gamemode
        self.buttons = pygame.sprite.Group()
        self.scroll = 0

    def update(self):
        self.scroll += 3 if self.settings.game_is_running else 0

        for i in range(2):
            speed = 1
            for layer in self.settings.game_background:
                self.screen.blit(layer, ((self.settings.screen_width * i) - self.scroll * speed, 0))
                speed += 0.3

                # if self.scroll * speed >= self.settings.screen_width:
                #     self.scroll =




