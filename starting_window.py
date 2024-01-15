import pygame

from btn import Button


class StartingWindow:
    def __init__(self, screen, settings):
        self.settings = settings
        self.buttons = pygame.sprite.Group()
        self.screen = screen
        self.create_buttons()

    def create_buttons(self):
        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               870, 30, 300, 100, 'LOCKER',
               self.settings.set_locker_wnd)

        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               30, 30, 120, 80, 'MONEY',
               None)

        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               160, 30, 120, 80, 'XP',
               None)

        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               100, 580, 150, 80, 'EASY',
               self.settings.set_easy_gamemode_wnd)

        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               520, 580, 150, 80, 'NORMAL',
               self.settings.set_normal_gamemode_wnd)

        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               1000, 580, 150, 80, 'HARD',
               self.settings.set_hard_gamemode_wnd)

        Button(self.screen, self.settings, self.buttons, (150, 150, 150),
               250, 680, 700, 80, 'INFINITY',
               self.settings.set_infinity_gamemode_wnd)

    def update(self):
        self.screen.blit(self.settings.starting_bg, (0, 0))

        self.buttons.update()
