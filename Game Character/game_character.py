#Exercise 12-2. Game Character
import sys

import pygame

# Importing settings
from settings import Settings

# Importing Boo
from boo import Boo

class BooGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Boo Game")

        self.boo = Boo(self)

    def run_game(self):
        """Start the main loop for game."""
        while True:
            # Watching for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.boo.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run it
    bg = BooGame()
    bg.run_game()
