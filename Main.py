import pygame


def main():
    window_size = (1000, 1500)

    pygame.display.set_mode(window_size)
    pygame.display.set_caption("Flappy Bird")

    window_surface = pygame.display.get_surface()

    game = Game(window_surface)
    game.play()
    pygame.quit()


class Game:
    def __init__(self, surface):
        # game variables

        self.surface = surface
        self.clock = pygame.time.Clock()
        self.continue_game = True
        self.fps = 30
        self.max_fps = 60
        self.color = pygame.Color('white')
        self.bird = pygame.Rect(surface.get_width()//2, surface.get_width()//2, 50, 50)

    def play(self):
        while self.continue_game:
            self.event_handler()
            self.draw()
            self.update()
            self.clock.tick(self.fps)

    def event_handler(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.continue_game = False

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.bird)

    def update(self):
        pygame.display.update()



main()
