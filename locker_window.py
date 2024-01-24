import pygame

from btn import Button


class Locker:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.buttons = pygame.sprite.Group()
        self.create_buttons()

    def create_buttons(self):
        Button(self.screen, self.settings, self.buttons, 450, 450, 300, 100, 'TRY IT',
               self.settings.set_starting_wnd)

        Button(self.screen, self.settings, self.buttons, 50, 150, 200, 100, 'yellow bird',
               self.yellow_clothes, color=(255, 255, 0))
        Button(self.screen, self.settings, self.buttons, 950, 600, 200, 100, 'blue bird',
               self.blue_clothes, color=(255, 255, 0))
        Button(self.screen, self.settings, self.buttons, 50, 300, 200, 100, 'brown bird',
               self.brown_clothes, color=(255, 255, 0))
        Button(self.screen, self.settings, self.buttons, 50, 450, 200, 100, 'grey bird',
               self.grey_clothes, color=(255, 255, 0))
        Button(self.screen, self.settings, self.buttons, 50, 600, 200, 100, 'green bird',
               self.green_clothes, color=(255, 255, 0))
        Button(self.screen, self.settings, self.buttons, 950, 150, 200, 100, 'red bird',
               self.red_clothes, color=(255, 255, 0))
        Button(self.screen, self.settings, self.buttons, 950, 380, 200, 100, 'purple bird',
               self.purple_clothes, color=(255, 255, 0))

        self.surface = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.bird = pygame.image.load('data/Bird2-1tit.png')
        self.rect = self.bird.get_rect()

        self.transparent = (0, 0, 0, 0)

    def update(self):
        self.screen.blit(self.settings.locker_bg, (0, 0))
        self.screen.blit(self.surface, (550, 300))
        self.surface.blit(self.bird, self.rect)

        for button in self.buttons:
            button.update()

    def yellow_clothes(self):
        self.settings.set_bird("Bird2-1.png")
        self.surface.fill(self.transparent)
        self.bird = pygame.image.load('data/Bird2-1tit.png')

    def blue_clothes(self):
        self.settings.set_bird("Bird2-2.png")
        self.surface.fill(self.transparent)
        self.bird = pygame.image.load('data/Bird2-2tit.png')

    def brown_clothes(self):
        self.settings.set_bird("Bird2-3.png")
        self.surface.fill(self.transparent)
        self.bird = pygame.image.load('data/Bird2-5tit.png')

    def grey_clothes(self):
        self.settings.set_bird("Bird2-4.png")
        self.surface.fill(self.transparent)
        self.bird = pygame.image.load('data/Bird2-6tit.png')

    def green_clothes(self):
        self.settings.set_bird("Bird2-5.png")
        self.surface.fill(self.transparent)
        self.bird = pygame.image.load('data/Bird2-4tit.png')

    def red_clothes(self):
        self.settings.set_bird("Bird2-6.png")
        self.surface.fill(self.transparent)
        self.bird = pygame.image.load('data/Bird2-3tit.png')

    def purple_clothes(self):
        self.settings.set_bird("Bird2-7.png")
        self.surface.fill(self.transparent)
        self.bird = pygame.image.load('data/Bird2-7tit.png')

    def save_avatar(self):
        pass
