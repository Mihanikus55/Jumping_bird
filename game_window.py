import pygame
from btn import Button
from bird import Bird


class GameWindow:
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen

    def start_over(self):
        self.pause_wnd = Pause(self.screen, self.settings)
        self.buttons = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        Bird(self.screen, self.settings, self.all_sprites)
        self.create_buttons()

    def create_buttons(self):
        Button(self.screen, self.settings, self.buttons,
               520, 580, 150, 80, 'Start',
               self.start_game)

    def start_game(self):
        self.settings.game_is_running = True
        self.buttons = pygame.sprite.Group()

    def set_pause(self):
        self.settings.game_is_running = False
        self.settings.pause_game = True
        self.buttons = self.pause_wnd.buttons

    def resume_game(self):
        self.settings.game_is_running = True
        self.settings.pause_game = False

    def exit_game(self):
        if not self.settings.game_is_running:
            self.settings.set_starting_wnd()

    def update(self):
        self.settings.game_background.update(self.screen, self.settings.game_is_running)

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        if self.settings.pause_game:
            self.pause_wnd.update()

        self.buttons.update()


class Pause(GameWindow):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.window_x = 350
        self.window_y = 200
        self.text = self.settings.pause_font.render("Pause", True, (0, 200, 0))
        self.buttons = pygame.sprite.Group()
        self.create_buttons()

    def create_buttons(self):
        Button(self.settings.pause_bg, self.settings, self.buttons,
               290, 190, 135, 50, 'Resume', self.resume_game,
               wnd_x=self.window_x, wnd_y=self.window_y)

        Button(self.settings.pause_bg, self.settings, self.buttons,
               70, 190, 135, 50, 'Exit', self.exit_game,
               wnd_x=self.window_x, wnd_y=self.window_y)

    def update(self):
        self.screen.blit(self.settings.pause_bg, (self.window_x, self.window_y))
        self.screen.blit(self.text, (530, 250))
        self.buttons.update()
