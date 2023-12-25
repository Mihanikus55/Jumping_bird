import sys

import pygame
from pygame.locals import *

from settings import Settings


#0134910491042
class JumpingBird:
    """Класс иницилизирующий игру на поверхностном уровне"""
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Jumping Bird")
        pygame.display.set_icon(pygame.image.load("data/game_icon.png").convert_alpha())

        self.fpsClock = pygame.time.Clock()

    def run_game(self):
        """Метод с основным циклом игры"""
        while True:
            self.check_events()

            self.update_screen()

    def check_events(self):
        """Метод обрабатывающий события (взаимодействие с пользователем)"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def update_screen(self):
        """Метод в котором происходит основная отрисовка игры"""
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()
        self.fpsClock.tick(self.settings.fps)


if __name__ == '__main__':
    jb = JumpingBird()
    jb.run_game()
