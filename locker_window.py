import pygame

from btn import Button


class Locker:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.buttons = pygame.sprite.Group()
        self.create_buttons()

    def update(self):
        self.screen.blit(self.settings.locker_bg, (0, 0))

        self.buttons.update()

    def create_buttons(self):
        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               30, 30, 110, 60, 'Back',
               self.settings.set_starting_wnd)  # Временая кнопка

    def change_clothes(self):
        pass

    def save_avatar(self):
        pass
