# Font class for Flappy Bird

import pygame


class Font:
    """
        Create the texts and images of text to be displayed
    """
    def __init__(self, surface, bottom):
        """
            Creating the intro and outro of the game
        :param surface: Main Surface window
        :param bottom: Ground surface
        """
        self.surface = surface
        self.bottom = bottom

        self.game_font = pygame.font.Font("./Assets/font/FB.ttf", 100)
        self.score_font = pygame.font.Font("./Assets/font/FB.ttf", 130)

        restart = pygame.image.load("./Assets/images/restart.png").convert_alpha()
        self.restart = pygame.transform.scale(restart, (int(214 * 1.5), int(75 * 1.5)))

        score_card = pygame.image.load("./Assets/images/score.png").convert_alpha()
        self.score_card = pygame.transform.scale2x(score_card)

        self.main_text = self.game_font.render("Flappy Bird", True, pygame.Color("white"))
        self.main_text2 = self.game_font.render("Flappy Bird", True, pygame.Color("black"))

        self.game_over_text = self.game_font.render("Game Over", True, pygame.Color("white"))
        self.game_over_text2 = self.game_font.render("Game Over", True, pygame.Color("black"))

        self.middle_position = self.surface.get_height() // 2 - self.bottom.get_rect().height

    def draw_intro(self):
        """
            Blits the intro on the screen
        :return: None
        """
        self.surface.blit(self.main_text2,
                          (self.surface.get_width() // 2 - self.main_text.get_width() // 2 + 10, self.middle_position - 400 + 10))
        self.surface.blit(self.main_text, (self.surface.get_width() // 2 - self.main_text.get_width() // 2, self.middle_position - 400))

    def draw_game_over(self, score):
        """
            Blits the game over screen
        :return: None
        """
        self.surface.blit(self.game_over_text2,
                          (self.surface.get_width() // 2 - self.game_over_text.get_width() // 2 + 10, self.middle_position + 10))

        self.surface.blit(self.game_over_text, (self.surface.get_width() // 2 - self.game_over_text.get_width() // 2, self.middle_position))

        score_text = self.score_font.render(score, True, pygame.Color('white'))
        score_text2 = self.score_font.render(score, True, pygame.Color('black'))
        x = self.surface.get_width() // 2 - self.score_card.get_rect().width // 2
        y = self.middle_position + 150

        self.surface.blit(self.score_card, (x, y))
        self.surface.blit(score_text2, (x + self.score_card.get_rect().width//2 - score_text.get_rect().width//2 + 10, y + self.score_card.get_rect().height//2 - score_text.get_rect().height//2 + 10))
        self.surface.blit(score_text, (x + self.score_card.get_rect().width//2 - score_text.get_rect().width//2, y + self.score_card.get_rect().height//2 - score_text.get_rect().height//2))

        self.surface.blit(self.restart, (self.surface. get_width() // 2 - self.restart.get_rect().width // 2, self.middle_position + self.score_card.get_rect().height + 170))

    def draw_score(self, score):
        """
            Blit the current score on the screen
        :return: None
        """
        score_text = self.score_font.render(score, True, pygame.Color('white'))
        score_text2 = self.score_font.render(score, True, pygame.Color('black'))
        self.surface.blit(score_text2, (self.surface.get_width() // 2 + 10, self.surface.get_height() * 0.1 + 10))
        self.surface.blit(score_text, (self.surface.get_width() // 2, self.surface.get_height() * 0.1))
