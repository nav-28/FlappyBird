# Flappy Bird

import pygame
from bird import Bird
import math


def main():
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
        # game variables
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color('black')
        self.continue_game = True
        self.start_game = False
        self.key_pressed = False

        # fps counter
        self.fps = 30
        self.max_fps = 60

        # background
        self.background = pygame.image.load("./Assets/flappy_background.png").convert()
        self.bg_scorll = 0
        self.bottom = pygame.image.load("./Assets/Bottom_border.png").convert()

        # flappy variables
        self.max_jump = 10
        self.jump_count = 0

        self.player = Bird(surface, self.bottom)
        self.all_sprite = pygame.sprite.Group(self.player)

        self.dt = None

        # Jumping variables
        self.isJump = False

        # bottom rect for collision
        self.bottom_rect = pygame.Rect(0, self.surface.get_height() - self.bottom.get_rect().height,
                                       self.bottom.get_rect().width, self.bottom.get_rect().height)

    def play(self):
        # main game loop
        while self.continue_game:
            self.dt = self.clock.tick(self.fps) / 1000
            self.event_handler()
            if self.start_game:
                self.jump()

            self.draw()
            self.check_bottom_collision()
            pygame.display.update()

    def event_handler(self):
        # check for event in pygame
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                self.continue_game = False
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    self.start_game = True
                    self.isJump = True
                self.key_pressed = True
            if event.type == pygame.KEYUP:
                self.key_pressed = False

    def draw(self):
        # draws the objects on the surface
        self.surface.blit(self.background, (0, -self.bottom.get_rect().height))
        self.player.image_animation(self.dt)
        self.all_sprite.draw(self.surface)
        if self.continue_game:
            self.background_scroll()

    def background_scroll(self):
        # infinite scroll of the ground when game is being played
        rel_x = self.bg_scorll % self.bottom.get_rect().width
        self.surface.blit(self.bottom, (
            rel_x - self.bottom.get_rect().width, self.surface.get_height() - self.bottom.get_rect().height))
        if rel_x < self.surface.get_width():
            self.surface.blit(self.bottom, (rel_x, self.surface.get_height() - self.bottom.get_rect().height))
        self.bg_scorll -= 5

    def check_bottom_collision(self):
        # checking for end game collision
        if self.bottom_rect.collidepoint(self.player.rect.x, self.player.rect.y + self.player.rect.height):
            self.continue_game = False
            pygame.display.update()

    def jump(self):
        # jumping function for the bird
        if self.isJump:
            self.jump_count = self.max_jump
            self.isJump = False
        neg = 1
        if self.jump_count < 0:
            neg = -neg
        self.player.change_pos(self.jump_count ** 2 * neg * 0.5)
        if self.jump_count > 0:
            self.jump_count -= 1
        else:
            self.jump_count -= 0.5


main()
