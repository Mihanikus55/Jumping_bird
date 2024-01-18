import pygame
from paralax_bg import ParalaxBackground as PB


class Settings:
    """Класс с настройками всей игры"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.icon = pygame.image.load("data/game_icon.png")
        self.caption = "Jumping Bird"

        self.fps = 60

        self.starting_bg = pygame.transform.scale(pygame.image.load('data/start_background_2.png'),
                                                  (self.screen_width, self.screen_height))
        self.cur_wnd = 'starting_wnd'
        self.gamemode = None
        self.game_is_running = False
        self.pause_game = False

        self.locker_bg = pygame.transform.scale(pygame.image.load('data/locker_bg.png'),
                                                (self.screen_width, self.screen_height))

        self.pause_bg = pygame.transform.scale(pygame.image.load('data/pause_background.png'), (480, 275))

        self.buttons_font = pygame.font.SysFont('Arial', 40)

    def set_starting_wnd(self):
        self.cur_wnd = 'starting_window'

    def set_locker_wnd(self):
        self.cur_wnd = 'locker_window'

    def set_money_window(self):
        self.cur_wnd = 'money_window'

    def set_xp_window(self):
        self.cur_wnd = 'xp_window'

    def set_easy_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.game_background = PB(self.screen_width, self.screen_height, 'game_background_1', 5, 1)

    def set_normal_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.game_background = PB(self.screen_width, self.screen_height, 'game_background_2', 7, 1)

    def set_hard_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.game_background = PB(self.screen_width, self.screen_height, 'game_background_3', 8, 1)

    def set_infinity_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.game_background = PB(self.screen_width, self.screen_height, 'game_background_4', 8, 2)
