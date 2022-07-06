# Importing and accessing the image of boo
#adding extra detail for git
import pygame

class Boo:
    """A class to manage boo."""

    def __init__(self, bg_game):
        """Intialize boo and its starting position."""
        self.screen = bg_game.screen
        self.screen_rect = bg_game.screen.get_rect()

        self.image = pygame.image.load('/Users/andrewgnazzo/Python/Python Crash Course/Projects/Game Character/images/boo.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)