# Pipe class for Flappy BIrd

import pygame
from random import randint


class Pipe:
    def __init__(self, surface, ground):
        """

        :param surface: Surface to draw the pipe on
        :param ground: Ground for calculating the pipe's position
        """
        self.surface = surface
        self.low_pipe = pygame.image.load("./Assets/images/pipe.png").convert_alpha()
        self.up_pipe = pygame.transform.flip(self.low_pipe, 0, 1)

        self.low_rect = self.low_pipe.get_rect()
        self.up_rect = self.up_pipe.get_rect()
        self.low_rect.y = randint(596, 1476)
        self.pip_difference = 500
        self.up_rect.bottomleft = (0, self.low_rect.y - self.pip_difference)

    def pip_position(self):
        """
            Change the pipe height every time it respawn
        :return: None
        """
        self.low_rect.y = randint(596, 1476)
        self.up_rect.bottomleft = (0, self.low_rect.y - self.pip_difference)

    def draw(self, rel_x):
        """
            blits the pipe on the surface
        :return: None
        """
        self.low_rect.x = rel_x
        self.up_rect.x = rel_x

        self.surface.blit(self.low_pipe, (self.low_rect.x, self.low_rect.y))
        self.surface.blit(self.up_pipe, (self.up_rect.x, self.up_rect.y))

    def collision(self, rect):
        """
            Check for the collision of the player and the pipes
        :param rect:
        :return: bool
        """
        if self.low_rect.colliderect(rect):
            return True
        elif self.up_rect.colliderect(rect):
            return True
        else:
            return False

    def pipe_width(self):
        """
            Return the pipe width
        :return: pipe width
        """
        return self.low_rect.width
