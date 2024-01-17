import pygame
from pygame.sprite import Sprite


class ParalaxBackground:
    def __init__(self, screen_width, screen_height, bg_name, layers_cnt):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg = bg_name
        self.layers_cnt = layers_cnt
        self.bg_layers = pygame.sprite.Group()
        self.load_paralax_background()

    def load_paralax_background(self):
        speed = 1.5
        for i in range(1, self.layers_cnt + 1):

            l_s_v = 0.3  # На сколько поднимается скорость каждого последующего слоя

            Layer(self.bg_layers, f'data/{self.bg}/layer_{i}.png',
                  self.screen_width, self.screen_height, speed)

            speed = round(l_s_v + speed, 1)

    def update(self, screen, game_is_running):
        self.bg_layers.update(screen, game_is_running)


class Layer(Sprite):
    def __init__(self, layers, layer, width, height, layer_speed):
        super().__init__(layers)
        self.layer_moving = True
        self.bg_width = width
        self.bg_height = height
        self.speed = layer_speed
        self.bg_layer = self.load_layer(layer)
        self.layer_rect = self.bg_layer.get_rect()

    def load_layer(self, layer):
        return pygame.transform.scale(pygame.image.load(layer),
                                      (self.bg_width, self.bg_height)).convert_alpha()

    def move(self, dx):
        self.layer_rect.x -= dx
        # print(dx)
        if self.layer_rect.x <= -self.bg_width:
            self.layer_rect.x += self.bg_width

    def update(self, screen, game_is_running):
        screen.blit(self.bg_layer, (self.layer_rect.x, self.layer_rect.y))
        screen.blit(self.bg_layer, (self.layer_rect.x + self.bg_width, self.layer_rect.y))
        if game_is_running:
            self.move(self.speed)
