import pygame


class Settings:
    """Класс с настройками всей игры"""

    def __init__(self):
        self.gamemode = None
        self.screen_width = 1200
        self.screen_height = 800
        self.icon = pygame.image.load("data/game_icon.png")
        self.caption = "Jumping Bird"

        self.fps = 60

        self.bg_color = (230, 230, 230)
        self.starting_bg = pygame.transform.scale(pygame.image.load('data/start_background_2.png'),
                                                  (self.screen_width, self.screen_height))
        self.cur_wnd = 'starting_wnd'

        self.locker_bg = pygame.transform.scale(pygame.image.load('data/locker_bg.png'),
                                                (self.screen_width, self.screen_height))

        self.buttons_font = pygame.font.SysFont('Arial', 40)

    def load_paralax_background(self, bg):
        game_bg_layers = []
        for i in range(1, 6):
            game_bg_layer = pygame.transform.scale(pygame.image.load(f'data/{bg}/layer_{i}.png'),
                                                   (self.screen_width, self.screen_height)).convert_alpha()
            game_bg_layers.append(game_bg_layer)
        return game_bg_layers

    def set_easy_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.gamemode = 'easy'
        self.game_background = 'game_background_1'
        print(self.gamemode)

    def set_normal_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.gamemode = 'normal'
        print(self.gamemode)

    def set_hard_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.gamemode = 'hard'
        print(self.gamemode)

    def set_infinity_gamemode_wnd(self):
        self.cur_wnd = 'game_window'
        self.gamemode = 'infinity'
        print(self.gamemode)

    def set_locker_wnd(self):
        self.cur_wnd = 'locker'
