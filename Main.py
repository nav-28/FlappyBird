# Flappy Bird

import pygame
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
        self.flappy = Bird(surface, self.bottom)
        self.max_jump = 10
        self.jump_count = 0

        # Jumping variables
        self.isJump = False

        # bottom rect for collision
        self.bottom_rect = pygame.Rect(0, self.surface.get_height() - self.bottom.get_rect().height,
                                       self.bottom.get_rect().width, self.bottom.get_rect().height)

    def play(self):
        # main game loop
        while self.continue_game:
            self.event_handler()
            if self.start_game:
                self.jump()
            else:
                self.flappy.dance()
            self.draw()
            self.check_bottom_collision()
            pygame.display.update()
            self.clock.tick(self.fps)

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
        self.flappy.draw()
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
        if self.bottom_rect.collidepoint(self.flappy.x, self.flappy.y + self.flappy.height()):
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
        self.flappy.change_pos(self.jump_count ** 2 * neg * 0.5)
        if self.jump_count > 0:
            self.jump_count -= 1
        else:
            self.jump_count -= 0.5


class Bird:
    def __init__(self, surface, bottom):
        self.surface = surface
        self.img = [pygame.image.load("./Assets/bird_1.png").convert_alpha(),
                    pygame.image.load("./Assets/bird_2.png").convert_alpha(),
                    pygame.image.load("./Assets/bird_3.png").convert_alpha()]
        self.img_counter = 0
        self.x = surface.get_width() * 0.4
        self.y = surface.get_height() * 0.5 - bottom.get_rect().height
        self.dance_x = 0
        self.time = 1
        self.time2 = 0
        self.up = False
        self.down = False

    def draw(self):
        self.surface.blit(self.img[self.img_counter], (self.x, self.y))
        self.time += 1
        if self.time > 5:
            self.img_counter += 1
            if self.img_counter > 2:
                self.img_counter = 0
            self.time = 1

    def dance(self):
        self.time2 += 1
        if self.time2 > 5:
            self.y += 30 * math.sin(self.dance_x)
            self.time2 = 0
        self.dance_x += 2

    def height(self):
        return self.img[0].get_rect().height

    def change_pos(self, new_position):
        self.y -= new_position


main()
