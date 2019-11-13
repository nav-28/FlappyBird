# Bird Class of Flappy Bird

import pygame
import math


class Bird(pygame.sprite.Sprite):
    def __init__(self, surface, background):
        """
        :param surface: surface of the window
        :param ground: ground rect
        """
        super().__init__()
        # loading images
        self.surface = surface
        self.group_images = [pygame.image.load("./Assets/images/bird_1.png").convert_alpha(),
                             pygame.image.load("./Assets/images/bird_2.png").convert_alpha(),
                             pygame.image.load("./Assets/images/bird_3.png").convert_alpha()]
        for i in range(3):
            self.group_images[i] = pygame.transform.scale(self.group_images[i], (138, 96))
        self.image_index = 0
        self.image = self.group_images[0]

        # bird position variables
        self.rect = self.image.get_rect()
        self.rect.x = surface.get_width() * 0.4 - self.rect.width//2
        self.rect.y = background.get_rect().height * 0.35

        # flapping animation variables
        self.flapping_animation_time = 0.1
        self.flapping_current_time = 0
        self.bounce_x = 0

        # rotation animation variables
        self.rotation_animation_time = 0.1
        self.rotation_current_time = 0
        self.rotation_angle = 0

        # game variables
        self.isUp = False
        self.isDown = False
        self.isJump = False

        # moving variables
        self.max_jump = 10
        self.jump_count = 0

    def image_animation(self, dt, game_start):
        """
            Animation for the bird sprite
        :param dt: int, for frame animation
        :param game_start: Bool
        :return: None
        """
        if game_start:
            self.flapping_current_time += dt
            if self.flapping_current_time >= self.flapping_animation_time:
                self.flapping_current_time = 0
                self.image_index = (self.image_index + 1) % len(self.group_images)
                self.image = self.group_images[self.image_index]

        if not game_start:
            self.flapping_current_time += dt
            if self.flapping_current_time >= self.flapping_animation_time:
                self.flapping_current_time = 0
                self.rect.y += 20 * math.sin(self.bounce_x)
                self.bounce_x += 0.5
                if self.bounce_x > 2*math.pi:
                    self.bounce_x = 0

    def move(self):
        """
            Moves the Bird based on player input
        :return: None
        """
        if self.isJump:
            self.jump_count = self.max_jump
            self.isJump = False

        neg = 1     # for changing direction of the parabola
        if self.jump_count < 0:
            neg = -1

        self.rect.y -= self.jump_count**2 * neg * 0.5

        if self.jump_count < 0:
            self.jump_count -= 0.5      # slows down the Bird Falling
        else:
            self.jump_count -= 1

    def jump(self):
        """
            changes the isJump when player jumps
        :return: None
        """
        self.isJump = True

    def return_pos(self):
        return self.rect.x
