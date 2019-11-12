# Flappy Bird

import pygame
from bird import Bird
from pipe import Pipe


def main():
    pygame.init()
    window_size = (1080, 1920)  # Full HD Resolution

    pygame.display.set_mode(window_size)
    pygame.display.set_caption("Flappy Bird")

    window_surface = pygame.display.get_surface()

    game = Game(window_surface)
    game.play()
    pygame.quit()


# Main game class
class Game:
    def __init__(self, surface):
        """
        :param surface: surface of the window
        """
        # game variables
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color('black')
        self.continue_game = True
        self.start_game = False
        self.key_pressed = False
        self.collision = False

        # fps counter
        self.fps = 50

        # background and ground
        self.background = pygame.image.load("./Assets/flappy_background.png").convert_alpha()
        self.ground = pygame.image.load("./Assets/ground.png").convert_alpha()
        self.bg_scroll = 0
        self.rel_x = self.bg_scroll % self.ground.get_rect().width

        # flappy objects
        self.player = Bird(surface, self.ground)
        self.all_sprites = pygame.sprite.Group(self.player)
        self.dt = None

        # bottom rect for collision
        self.bottom_rect = pygame.Rect(0, self.surface.get_height() - self.ground.get_rect().height,
                                       self.ground.get_rect().width, self.ground.get_rect().height)

        # pipe object
        self.pipe1 = Pipe(self.surface, self.ground)
        self.pipe2 = Pipe(self.surface, self.ground)
        # pipe scroll variables
        self.pipe1_rel_x = self.surface.get_width()
        self.min_pipe1_rel_x = -self.pipe1.pipe_width()

        self.pipe2_rel_x = self.surface.get_width() + 700
        self.min_pipe2_rel_x = -self.pipe2.pipe_width()

    def play(self):
        """
            Main Game Loop
        :return: None
        """
        while self.continue_game:
            self.dt = self.clock.tick(self.fps) / 1000
            self.event_handler()
            if self.start_game:
                self.game_start()
            self.player.image_animation(self.dt, self.start_game)
            self.draw()
            pygame.display.update()

    def event_handler(self):
        """
            Handles pygame events
        :return: None
        """
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                self.continue_game = False
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    self.start_game = True
                    self.player.jump()
                self.key_pressed = True
            if event.type == pygame.KEYUP:
                self.key_pressed = False
            if self.collision:
                self.continue_game = False

    def game_start(self):
        """
            Starts the game when space is pressed
        :return: None
        """
        self.pipe_scroll()
        self.check_bottom_collision()
        self.player.move()
        self.pipe_collision()

    def draw(self):
        """
            Draws the objects on the surface
        :return: None
        """
        self.surface.blit(self.background, (0, -self.ground.get_rect().height))
        self.all_sprites.draw(self.surface)
        if self.start_game:
            self.pipe1.draw(self.pipe1_rel_x)
            self.pipe2.draw(self.pipe2_rel_x)
        self.background_scroll()

    def background_scroll(self):
        """
            Infinite scroll of the ground
        :return: None
        """
        if self.continue_game:
            self.rel_x = self.bg_scroll % self.ground.get_rect().width
        self.surface.blit(self.ground, (
            self.rel_x - self.ground.get_rect().width, self.surface.get_height() - self.ground.get_rect().height))
        if self.rel_x < self.surface.get_width():
            self.surface.blit(self.ground, (self.rel_x, self.surface.get_height() - self.ground.get_rect().height))
        if self.continue_game:
            self.bg_scroll -= 10

    def pipe_scroll(self):
        """
            Moves the pipes 10 pixels
        :return: None
        """
        if self.pipe1_rel_x < self.min_pipe1_rel_x:
            self.pipe1_rel_x = self.surface.get_width()
            self.pipe1.pip_position()
        self.pipe1_rel_x -= 10

        if self.pipe2_rel_x < self.min_pipe2_rel_x:
            self.pipe2_rel_x = self.surface.get_width()
            self.pipe2.pip_position()
        self.pipe2_rel_x -= 10

    def pipe_collision(self):
        if self.pipe1.collision(self.player.rect):
            self.collision = True
        elif self.pipe2.collision(self.player.rect):
            self.collision = True

    def check_bottom_collision(self):
        """
            Check for collision of player sprite with the ground
        :return: None
        """
        if self.bottom_rect.collidepoint(self.player.rect.x, self.player.rect.y + self.player.rect.height):
            self.continue_game = False
            pygame.display.update()


main()
