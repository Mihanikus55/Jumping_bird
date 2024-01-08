import sys
import pygame

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

buttons = []


class Button():
    def __init__(self, x, y, width, height, buttonText):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        buttons.append(self)

    def clicking(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill((255, 255, 255))
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill((128, 128, 128))
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill((64, 64, 64))
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


Button(870, 30, 300, 100, 'LOCKER')
Button(30, 30, 120, 80, 'MONEY')
Button(160, 30, 120, 80, 'XP')
Button(100, 500, 150, 80, 'EASY')
Button(500, 500, 150, 80, 'MEDIUM')
Button(1000, 500, 150, 80, 'HARD')
Button(250, 600, 700, 80, 'БЕСКОНЕЧНАЯ ИГРА')

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for button in buttons:
        button.clicking()
    pygame.display.flip()
    fpsClock.tick(fps)
