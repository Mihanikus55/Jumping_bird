import sys

import pygame
from pygame.locals import *

from settings import Settings
from starting_window import StartingWindow
from game_window import GameWindow
from locker_window import Locker


class JumpingBird:
    """Класс иницилизирующий игру на поверхностном уровне"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        pygame.display.set_icon(self.settings.icon)

        self.starting_window = StartingWindow(self.screen, self.settings)
        self.game_window = GameWindow(self.screen, self.settings)
        self.locker = Locker(self.screen, self.settings)

        self.game_is_running = False
        self.set_cur_window(self.starting_window)

        self.fpsClock = pygame.time.Clock()

    def run_game(self):
        """Метод с основным циклом игры"""
        while True:
            self.check_events()

            self.cur_window.update()

            pygame.display.flip()
            self.fpsClock.tick(self.settings.fps)

    def check_events(self):
        """Метод обрабатывающий события (взаимодействие с пользователем)"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and not self.game_is_running:
                    self.check_buttons_clicked(event.pos)

                # TODO: Реализовать меню паузы чтобы можно было нормально вернуться на начальное окно
                else:
                    self.cur_window = self.starting_window
                    self.screen.fill((0, 0, 0))
                    self.game_is_running = False

    def check_buttons_clicked(self, pos):
        for button in self.cur_window.buttons:
            if button.buttonRect.collidepoint(pos):
                button.do_task()
                self.choose_window_to_change(self.settings.cur_wnd)

    def choose_window_to_change(self, name_wnd):
        if name_wnd == 'starting_window':
            self.set_cur_window(self.starting_window)
        elif name_wnd == 'game_window':
            self.game_is_running = True  # TODO: Реализовать нормальную смену состояния игры
            self.set_cur_window(self.game_window)
        elif name_wnd == 'locker_window':
            self.game_is_running = True  # TODO: Убрать
            self.set_cur_window(self.locker)

        elif name_wnd == 'money_window':  # TODO: Изменить
            pass
        elif name_wnd == 'xp_window':
            pass

    def set_cur_window(self, wnd):
        self.screen.fill((0, 0, 0))
        self.cur_window = wnd


if __name__ == '__main__':
    jb = JumpingBird()
    jb.run_game()
