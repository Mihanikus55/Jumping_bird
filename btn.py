import pygame
from pygame.sprite import Sprite


class Button(Sprite):
    def __init__(self, screen, settings, buttons, x, y, width, height, button_text, task,
                 wnd_x=0, wnd_y=0, color=(150, 150, 150)):
        super().__init__(buttons)
        self.screen = screen
        self.settings = settings
        self.task = task
        self.color = color
        self.x = x
        self.y = y

        self.buttonSurface = pygame.Surface((width, height))
        self.buttonRect = pygame.Rect(x + wnd_x, y + wnd_y, width, height)

        self.buttonSurf = self.settings.buttons_font.render(button_text, True, (20, 20, 20))

    def do_task(self):
        if self.task:
            self.task()

    def update(self):
        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill((102, 102, 102))
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill((51, 51, 51))
        else:
            self.buttonSurface.fill(self.color)
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.screen.blit(self.buttonSurface, (self.x, self.y))
