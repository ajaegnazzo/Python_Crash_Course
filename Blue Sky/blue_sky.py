#Exercise 12-1. Blue Sky: Make a Pygame window with a blue background.

import sys

import pygame

class BlueSky:
    """Overall class to incorporate a pygame window"""

    def __init__(self):
        # Initializing the game
        pygame.init()

        # Setting the screen size
        self.screen = pygame.display.set_mode((1200, 800))

        # Setting the caption for the screen
        pygame.display.set_caption("Blue Sky")

        # Set the background color
        self.bg_color = (0, 0, 255)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Giving option to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Making the screen visible
            pygame.display.flip()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

if __name__ == '__main__':
    # Make a game instance and run the game
    bs = BlueSky()
    bs.run_game()