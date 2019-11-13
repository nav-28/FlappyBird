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

        # font objects
        self.game_font = pygame.font.Font("./Assets/font/FB.ttf", 100)
        self.score_font = pygame.font.Font("./Assets/font/FB.ttf", 130)
        self.intro_font = pygame.font.Font("./Assets/font/katyfont.ttf", 50)
        # restart image
        restart = pygame.image.load("./Assets/images/restart.png").convert_alpha()
        self.restart = pygame.transform.scale(restart, (int(214 * 1.5), int(75 * 1.5)))

        # score card image
        score_card = pygame.image.load("./Assets/images/score.png").convert_alpha()
        self.score_card = pygame.transform.scale2x(score_card)

        # main text surface
        self.main_text = self.game_font.render("Flappy Bird", True, pygame.Color("white"))
        self.main_text2 = self.game_font.render("Flappy Bird", True, pygame.Color("black"))     # black shadow

        # intro text surface
        self.intro_text = self.intro_font.render("Press SPACE to start the game", True, pygame.Color(83, 55, 70))

        # game over surface
        self.game_over_text = self.game_font.render("Game Over", True, pygame.Color("white"))
        self.game_over_text2 = self.game_font.render("Game Over", True, pygame.Color("black"))  # black shadow

        # center y co-ordinate of the surface
        self.middle_position = self.surface.get_height() // 2 - self.bottom.get_rect().height - 300

    def draw_intro(self):
        """
            Blits the intro on the screen
        :return: None
        """
        # intro text
        x = self.surface.get_width() // 2 - self.main_text.get_width() // 2
        y = self.surface.get_height() // 2 - self.bottom.get_rect().height - 400
        self.surface.blit(self.main_text2, (x + 10, y + 10))
        self.surface.blit(self.main_text, (x, y))
        self.surface.blit(self.intro_text, (x - 140, y + 160))

    def draw_game_over(self, score):
        """
            Blits the game over screen
        :return: None
        """
        # game over text
        x = self.surface.get_width() // 2 - self.game_over_text.get_width() // 2
        self.surface.blit(self.game_over_text2, (x + 10, self.middle_position + 10))
        self.surface.blit(self.game_over_text, (x, self.middle_position))

        # score text variable
        score_text = self.score_font.render(score, True, pygame.Color('white'))
        score_text2 = self.score_font.render(score, True, pygame.Color('black'))

        # score card
        x = self.surface.get_width() // 2 - self.score_card.get_rect().width // 2
        y = self.middle_position + 150
        self.surface.blit(self.score_card, (x, y))

        # score text
        x = x + self.score_card.get_rect().width//2 - score_text.get_rect().width//2
        y = y + self.score_card.get_rect().height//2 - score_text.get_rect().height//2
        self.surface.blit(score_text2, (x + 10, y + 10))
        self.surface.blit(score_text, (x, y))

        # restart
        self.surface.blit(self.restart, (self.surface. get_width() // 2 - self.restart.get_rect().width // 2, self.middle_position + self.score_card.get_rect().height + 170))

    def draw_score(self, score):
        """
            Blit the current score on the screen
        :return: None
        """
        # score text
        x = self.surface.get_width() // 2
        y = self.surface.get_height() * 0.1
        score_text = self.score_font.render(score, True, pygame.Color('white'))
        score_text2 = self.score_font.render(score, True, pygame.Color('black'))
        self.surface.blit(score_text2, (x + 10, y + 10))
        self.surface.blit(score_text, (x, y))
