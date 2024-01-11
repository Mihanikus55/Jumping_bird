import pygame
from pygame.sprite import Sprite

from settings import Settings


class Button(Sprite):
    def __init__(self, screen, buttons, x, y, width, height, button_text):
        super().__init__(buttons)
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_text = button_text
        self.settings = Settings()
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.settings.buttons_font.render(self.button_text, True, (20, 20, 20))

    def update(self):
        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill((102, 102, 102))
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill((51, 51, 51))
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)
