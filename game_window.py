import pygame
from btn import Button


class GameWindow:
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.pause_wnd = Pause(self.screen, self.settings)
        self.buttons = pygame.sprite.Group()
        self.create_buttons()

    def create_buttons(self):
        self.start = Button(self.screen, self.settings, self.buttons, (150, 150, 150),
                            520, 580, 150, 80, 'Start',
                            self.start_game)

    def update(self):
        self.settings.game_background.update(self.screen, self.settings.game_is_running)

        if self.settings.pause_game:
            self.pause_wnd.update()

        self.buttons.update()

    def start_game(self):
        self.settings.game_is_running = True
        self.buttons.remove(self.start)

    def set_pause(self):
        self.settings.pause_game = True
        self.settings.game_is_running = False
        self.buttons = self.pause_wnd.buttons


class Pause:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.buttons = pygame.sprite.Group()
        self.create_buttons()

    def create_buttons(self):
        Button(self.settings.pause_bg, self.settings, self.buttons, (150, 150, 150),
               290, 190, 135, 50, 'Resume',
               self.resume_game)

        Button(self.settings.pause_bg, self.settings, self.buttons, (150, 150, 150),
               70, 190, 90, 50, 'Exit',
               self.exit_game)

    def resume_game(self):
        self.settings.game_is_running = True
        self.settings.pause_game = False
        # self.screen.fill((255, 255, 255))

    def exit_game(self):
        self.settings.pause_game = False
        self.settings.set_starting_wnd()

    def update(self):
        self.screen.blit(self.settings.pause_bg, (350, 200))
        self.buttons.update()
