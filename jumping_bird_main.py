import pygame
from pygame.locals import *

from settings import Settings
from starting_window import StartingWindow
from game_window import GameWindow
from locker_window import Locker
from game_shop import Shop


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
        self.shop = Shop(self.screen, self.settings)

        self.choose_window_to_change(self.settings.cur_wnd)

        self.fpsClock = pygame.time.Clock()

    def run_game(self):
        """Метод с основным циклом игры"""
        while True:
            self.screen.fill((0, 0, 0))
            self.check_events()

            self.cur_window.update()

            pygame.display.flip()
            self.fpsClock.tick(self.settings.fps)

    def check_events(self):
        """Метод обрабатывающий события (взаимодействие с пользователем)"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.settings.terminate_program()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.check_buttons_clicked(event.pos)

            up = False
            down = False

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up = True
                if event.key == K_DOWN:
                    down = True

                if event.key == K_ESCAPE:
                    if self.settings.game_is_running:
                        self.game_window.set_pause()

            if event.type == KEYUP:
                if event.key == K_UP:
                    up = False
                if event.key == K_DOWN:
                    down = False

            self.game_window.dy = down - up

    def check_buttons_clicked(self, pos):
        for button in self.cur_window.buttons:
            if button.buttonRect.collidepoint(pos):
                button.do_task()
                self.choose_window_to_change(self.settings.cur_wnd)

    def choose_window_to_change(self, name_wnd):
        if name_wnd == 'starting_window':
            self.game_window.start_over()
            self.set_cur_window(self.starting_window)
        elif name_wnd == 'game_window':
            self.set_cur_window(self.game_window)
        elif name_wnd == 'locker_window':
            self.set_cur_window(self.locker)
        elif name_wnd == 'money_window':  # TODO: Изменить
            self.game_is_running = True
            self.set_cur_window(self.shop)

        elif name_wnd == 'xp_window':
            pass

    def set_cur_window(self, wnd):
        self.cur_window = wnd


if __name__ == '__main__':
    jb = JumpingBird()
    jb.run_game()
