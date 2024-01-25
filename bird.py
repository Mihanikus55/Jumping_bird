import pygame
from pygame.sprite import Sprite


class Bird(Sprite):
    def __init__(self, screen, settings, all_sprites):
        super().__init__(all_sprites)
        self.screen = screen
        self.settings = settings

        self.frames = []
        self.cut_sheet(self.settings.sheet, 4)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(300, 450)
        self.start_time = pygame.time.get_ticks()
        self.delay = 100

    def cut_sheet(self, sheet, columns):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height())
        for i in range(columns):
            frame_location = (self.rect.w * i, 0)
            self.frames.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def move(self, dy):
        self.rect.move_ip(0, self.settings.bird_speed * dy)

    def update(self):
        self.cur_frame = ((pygame.time.get_ticks() - self.start_time) // self.delay) % len(self.frames)
        self.image = self.frames[self.cur_frame]
