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

        self.buttons_font = pygame.font.SysFont('Arial', 40)

    def load_game_background(self, bg):
        pass

    def set_easy_gamemode(self):
        self.gamemode = 'easy'
        print(self.gamemode)

    def set_normal_gamemode(self):
        self.gamemode = 'normal'
        print(self.gamemode)

    def set_hard_gamemode(self):
        self.gamemode = 'hard'
        print(self.gamemode)

    def set_infinity_gamemode(self):
        self.gamemode = 'infinity'
        print(self.gamemode)
