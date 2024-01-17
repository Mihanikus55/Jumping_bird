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

        self.locker_bg = pygame.transform.scale(pygame.image.load('data/locker_bg.png'),
                                                (self.screen_width, self.screen_height))

        self.shop_bg = pygame.transform.scale(pygame.image.load('data/shop_bg.png'),
                                              (self.screen_width, self.screen_height))

        self.buttons_font = pygame.font.SysFont('Arial', 40)

    def toggle_state_game(self):
        self.game_is_running = not self.game_is_running

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
        self.gamemode = 'easy'
        self.game_background = PB(self.screen_width, self.screen_height, 'game_background_1', 5)
        print(self.gamemode)

    def set_normal_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.gamemode = 'normal'
        self.game_background = PB(self.screen_width, self.screen_height, 'game_background_2', 7)
        print(self.gamemode)

    def set_hard_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.gamemode = 'hard'
        self.game_background = PB(self.screen_width, self.screen_height, 'game_background_3', 8)
        print(self.gamemode)

    def set_infinity_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.gamemode = 'infinity'
        self.game_background = PB(self.screen_width, self.screen_height, 'game_background_4', 8)
        print(self.gamemode)
