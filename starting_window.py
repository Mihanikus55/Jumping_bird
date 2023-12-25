from settings import Settings


class StartingWindow:
    def __init__(self):
        self.settings = Settings()

    def update(self, screen):
        screen.blit(self.settings.starting_bg, (0, 0))

