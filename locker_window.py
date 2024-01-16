import pygame
from btn import Button


class Locker:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.buttons = pygame.sprite.Group()
        self.create_buttons()

    def create_buttons(self):
        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               450, 450, 300, 100, 'TRY IT',
               self.change_clothes())

    def update(self):
        self.screen.blit(self.settings.locker_bg, (0, 0))
        for button in self.buttons:
            button.update()

    def change_clothes(self):
        pass
