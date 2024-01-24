import pygame

from btn import Button


class StartingWindow:
    def __init__(self, screen, settings):
        self.settings = settings
        self.buttons = pygame.sprite.Group()
        self.screen = screen
        self.create_buttons()

    def create_buttons(self):
        Button(self.screen, self.settings, self.buttons, 870, 30, 300, 100, 'LOCKER',
               self.settings.set_locker_wnd)

        Button(self.screen, self.settings, self.buttons, 30, 30, 120, 80, 'Exit',
               self.settings.terminate_program)

        Button(self.screen, self.settings, self.buttons, 100, 580, 150, 80, 'EASY',
               self.settings.set_easy_gamemode_wnd)

        Button(self.screen, self.settings, self.buttons, 520, 580, 150, 80, 'NORMAL',
               self.settings.set_normal_gamemode_wnd)

        Button(self.screen, self.settings, self.buttons, 1000, 580, 150, 80, 'HARD',
               self.settings.set_hard_gamemode_wnd)

        Button(self.screen, self.settings, self.buttons, 250, 680, 700, 80, 'INFINITY',
               self.settings.set_infinity_gamemode_wnd)

    def update(self):
        self.screen.blit(self.settings.starting_bg, (0, 0))

        self.buttons.update()
