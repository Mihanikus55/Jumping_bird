import pygame


class Settings:
    """Класс с настройками всей игры"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.icon = pygame.image.load("data/game_icon.png")
        self.caption = "Jumping Bird"

        self.fps = 60

        self.bg_color = (230, 230, 230)
        self.starting_bg = pygame.transform.scale(pygame.image.load('data/background_1.png'),
                                                  (self.screen_width, self.screen_height))

