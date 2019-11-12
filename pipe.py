import pygame
from random import randint


class Pipe:
    def __init__(self, surface, ground):
        """

        :param surface:
        :param ground:
        """
        self.surface = surface
        self.low_pipe = pygame.image.load("./Assets/pipe.png").convert_alpha()
        self.up_pipe = pygame.transform.flip(self.low_pipe, 0, 1)

        self.low_rect = self.low_pipe.get_rect()
        self.up_rect = self.up_pipe.get_rect()
        self.low_rect.y = randint(596, 1476)
        self.up_rect.bottomleft = (0, self.low_rect.y - 500)

    def pip_position(self):
        """

        :return:
        """
        self.low_rect.y = randint(596, 1476)
        self.up_rect.bottomleft = (0, self.low_rect.y - 500)

    def draw(self, rel_x):
        """

        :return:
        """
        self.low_rect.x = rel_x
        self.up_rect.x = rel_x

        self.surface.blit(self.low_pipe, (self.low_rect.x, self.low_rect.y))
        self.surface.blit(self.up_pipe, (self.up_rect.x, self.up_rect.y))

    def collision(self, rect):
        if self.low_rect.colliderect(rect):
            return True
        elif self.up_rect.colliderect(rect):
            return True
        else:
            return False

    def pipe_width(self):
        return self.low_rect.width
