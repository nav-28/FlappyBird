# Flappy Bird

import pygame
import math


class Bird(pygame.sprite.Sprite):
    def __init__(self, surface, bottom):
        super().__init__()

        self.surface = surface
        self.group_images = [pygame.image.load("./Assets/bird_1.png").convert_alpha(),
                             pygame.image.load("./Assets/bird_2.png").convert_alpha(),
                             pygame.image.load("./Assets/bird_3.png").convert_alpha()]
        self.image_index = 0
        self.image = pygame.image.load("./Assets/bird_1.png")

        self.rect = self.image.get_rect()

        self.rect.x = surface.get_width() // 2
        self.rect.y = surface.get_height() // 2 - bottom.get_rect().height

        self.animation_time = 0.1
        self.current_time = 0
        self.x = 0
        self.time = 1

    def image_animation(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.image_index = (self.image_index + 1) % len(self.group_images)
            self.image = self.group_images[self.image_index]

            self.rect.y += 20 * math.sin(self.x)
            self.x += 1

    def height(self):
        return self.rect.height

    def change_pos(self, new_position):
        self.rect.y -= new_position
