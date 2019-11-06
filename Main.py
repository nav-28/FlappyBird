import pygame


def main():
    window_size = (1080, 1920)

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

        # fps counter
        self.fps = 30
        self.max_fps = 60

        # bird variables
        self.color = pygame.Color('white')
        self.bird = pygame.Rect(surface.get_width() // 2, surface.get_height() // 2, 50, 50)
        self.bird_x_velocity = 5
        self.isJump = False
        self.max_jump = 10
        self.jump_count = 0

        # background
        self.background = pygame.image.load("./Assets/flappy_background.png").convert()
        self.bg_scorll = 0
        self.bottom = pygame.image.load("./Assets/Bottom_border.png").convert()

    def play(self):
        while self.continue_game:
            self.event_handler()

            self.draw()
            self.update()

            self.check_border()
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
        self.surface.blit(self.background, (0, 0))
        pygame.draw.rect(self.surface, self.color, self.bird)
        self.background_scroll()


    def update(self):
        self.jump()
        pygame.display.update()

    def background_scroll(self):

        rel_x = self.bg_scorll % self.bottom.get_rect().width
        self.surface.blit(self.bottom, (rel_x - self.bottom.get_rect().width, self.surface.get_height() - self.bottom.get_rect().height))
        if rel_x < self.surface.get_width():
            self.surface.blit(self.bottom, (rel_x, self.surface.get_height() - self.bottom.get_rect().height))
        self.bg_scorll -= 5

    def check_border(self):
        if self.bird.y > self.surface.get_height() + 100:
            self.continue_game = False

    def jump(self):
        if self.isJump:
            self.jump_count = self.max_jump
            self.isJump = False
        neg = 1
        if self.jump_count < 0:
            neg = -neg
        self.bird.y -= self.jump_count ** 2 * neg * 0.5
        if self.jump_count > 0:
            self.jump_count -= 1
        else:
            self.jump_count -= 0.5


main()
