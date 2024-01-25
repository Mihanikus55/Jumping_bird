import pygame
import random

pygame.init()

empty_space = 400
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

pipe_img = pygame.transform.scale(pygame.image.load('data/pipes/pipe_long.png'),
                                  (300, 250))

pipe_img_flipped = pygame.transform.flip(pipe_img, False, True)  # Перевернутое изображение трубы


class Pipe:
    def __init__(self, x, y, flipped):
        self.image = pipe_img_flipped if flipped else pygame.transform.scale(pygame.image.load('data/pipes/pipe_long.png'),
                                                                             (300, 650))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 2  # Скорость движения трубы

    def draw(self):
        screen.blit(self.image, self.rect)


pipes = []


def generate_pipe():
    gap_y1 = random.randint(-200, -15)
    pipes.append(Pipe(screen_width, gap_y1, True))  # Верхняя труба
    pipes.append(Pipe(screen_width, screen_height + gap_y1 - empty_space, False))  # Нижняя труба


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))  # Цвет фона

    # Добавляем новые трубы каждые 400 кадров
    if len(pipes) == 0 or pipes[-1].rect.x < screen_width - 400:
        generate_pipe()

    for pipe in pipes:
        pipe.update()
        pipe.draw()

    pygame.display.flip()  # Отображение

    clock.tick(60)  # Ограничение частоты кадров

pygame.quit()
