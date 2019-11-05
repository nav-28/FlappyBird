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
        self.bg_color = pygame.Color('black')
        self.continue_game = True
        self.key_pressed = False

        self.fps = 30
        self.max_fps = 60

        self.color = pygame.Color('white')
        self.bird = pygame.Rect(surface.get_width()//2, surface.get_height() - 50, 50, 50)
        self.isJump = False
        self.max_jump = 10
        self.jump_count = self.max_jump

    def play(self):
        while self.continue_game:
            self.event_handler()

            self.draw()
            self.update()

            self.clock.tick(self.fps)

    def event_handler(self):
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                self.continue_game = False
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    self.isJump = True
                self.key_pressed = True
            if event.type == pygame.KEYUP:
                self.key_pressed = False

    def draw(self):
        self.surface.fill(self.bg_color)
        pygame.draw.rect(self.surface, self.color, self.bird)

    def update(self):
        if self.isJump:
            self.jump()
        pygame.display.update()

    def jump(self):
        if self.jump_count >= -10:
            neg = 1
            if self.jump_count < 0:
                neg = -neg
            self.bird.y -= self.jump_count ** 2 * neg
            self.jump_count -= 1
        else:
            self.jump_count = self.max_jump
            self.isJump = False

main()
