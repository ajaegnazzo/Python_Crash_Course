#Alien Invasion Game Code
import sys

import pygame

from settings import Settings #calling settings.py
from ship import Ship

class AlienInvasion:
    """Overall class to manage game asserts and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #initializes the background settings nessary for pygame to work
        self.settings = Settings() #creating an instance of settings

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #creating the game to be fullscreen
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) #brings in the ship, references the instance of alien invasion

        # Set the background color
        self.bg_color = (230, 230, 230) #these are color values

    def run_game(self): #this controls the game
        """Start the main loop for the game."""
        while True:
            self._check_events() #this is going to check the check events method
            self.ship.update() #ship's position is updated after there has been a check for keyboard events and before the screen is updated
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
            self.ship.moving_right = True #now we are saying rather than move right by 1, we just flag that it is moving right
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #adding a shortcut to click 'q' when you want to quit
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on teh screen, and flip to the new screen."""
         # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color) #referencing the settings
        self.ship.blitme() #ship appears on top of the background

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion() #making sure the game is only run when it is called directly
    ai.run_game()

