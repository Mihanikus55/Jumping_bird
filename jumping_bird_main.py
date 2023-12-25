import sys

import pygame
from pygame.locals import *

from settings import Settings
from starting_window import StartingWindow


#0134910491042
class JumpingBird:
    """Класс иницилизирующий игру на поверхностном уровне"""
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.starting_window = StartingWindow()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        pygame.display.set_icon(self.settings.icon)

        self.is_start_window = True

        self.fpsClock = pygame.time.Clock()

    def run_game(self):
        """Метод с основным циклом игры"""
        while True:
            self.check_events()
            if self.is_start_window:
                self.starting_window.update(self.screen)
            else:
                self.update_screen()

            pygame.display.flip()
            self.fpsClock.tick(self.settings.fps)

    def check_events(self):
        """Метод обрабатывающий события (взаимодействие с пользователем)"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def update_screen(self):
        """Метод в котором происходит основная отрисовка игры"""
        self.screen.fill(self.settings.bg_color)


if __name__ == '__main__':
    jb = JumpingBird()
    jb.run_game()
