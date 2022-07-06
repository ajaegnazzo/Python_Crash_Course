#Exercise 12-4. Rocket

import sys

import pygame

from rocket import Rocket

from settings import Settings

class RocketGame:
    """Overall class to manage the game and assert behaviors."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #creating the game to be fullscreen
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self) #brings in the ship, references the instance of alien invasion

    def run_game(self): #this controls the game
        """Start the main loop for the game."""
        while True:
            self._check_events() #this is going to check the check events method
            self.rocket.update() #ship's position is updated after there has been a check for keyboard events and before the screen is updated
            self._update_screen() #checking update screen below
    
    def _check_events(self): #moved this method down to separate
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get(): #event is an action performed in the game
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN: #this detects when there is a "keydown" event
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:  #when the key is no longer pressed, the ship is no longer moving right!
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event): #creating a new method to say what happens when key is clicked
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT: #this is when the right arrow key is pressed
            self.rocket.moving_right = True #now we are saying rather than move right by 1, we just flag that it is moving right
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q: #adding a shortcut to click 'q' when you want to quit
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to releases."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """Update images on teh screen, and flip to the new screen."""
         # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color) #referencing the settings
        self.rocket.blitme() #ship appears on top of the background

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rg = RocketGame() #making sure the game is only run when it is called directly
    rg.run_game()