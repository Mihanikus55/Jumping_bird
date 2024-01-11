import pygame

from btn import Button
from game_window import GameWindow
from settings import Settings


class StartingWindow:
    def __init__(self, screen):
        self.settings = Settings()
        self.buttons = pygame.sprite.Group()
        self.screen = screen
        self.create_buttons()

    def create_buttons(self):
        Button(self.screen, self.buttons, 870, 30, 300, 100, 'LOCKER')
        Button(self.screen, self.buttons, 30, 30, 120, 80, 'MONEY')
        Button(self.screen, self.buttons, 160, 30, 120, 80, 'XP')
        Button(self.screen, self.buttons, 100, 500, 150, 80, 'EASY')
        Button(self.screen, self.buttons, 500, 500, 150, 80, 'NORMAL')
        Button(self.screen, self.buttons, 1000, 500, 150, 80, 'HARD')
        Button(self.screen, self.buttons, 250, 600, 700, 80, 'INFINITY')

    def update(self):
        self.screen.blit(self.settings.starting_bg, (0, 0))

        for button in self.buttons:
            button.update()

    def check_button_action(self, name):
        if name == 'LOCKER':
            pass
        elif name == 'MONEY':
            pass
        elif name == 'XP':
            pass
        elif name == 'EASY':
            self.settings.set_easy_gamemode()
            return 'game_window'
        elif name == 'NORMAL':
            self.settings.set_normal_gamemode()
            return 'game_window'
        elif name == 'HARD':
            self.settings.set_hard_gamemode()
            return 'game_window'
        elif name == 'INFINITY':
            self.settings.set_infinity_gamemode()
            return 'game_window'

