import pygame

from btn import Button
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
        Button(self.screen, self.buttons, 500, 500, 150, 80, 'MEDIUM')
        Button(self.screen, self.buttons, 1000, 500, 150, 80, 'HARD')
        Button(self.screen, self.buttons, 250, 600, 700, 80, 'БЕСКОНЕЧНАЯ ИГРА')

    def update(self):
        self.screen.blit(self.settings.starting_bg, (0, 0))

        for button in self.buttons:
            button.update()

