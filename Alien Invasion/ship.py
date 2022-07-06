# Ship.py
import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game): #references self and to alien invasion instance
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen #this allows us to place the image on the screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #rect means rectangle

        # Load the ship image and get its rect.
        self.image = pygame.image.load('/Users/andrewgnazzo/Python/Python Crash Course/Projects/Alien Invasion/images/ship.bmp')
        self.rect = self.image.get_rect() 

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x) # this helps us figure out where the ship is

        # Movement flag
        self.moving_right = False #setting the movement initially right to be false, so not moving
        self.moving_left = False

    def update(self): #updating the movement, which moves the ship right if the flag is true
        """Update the ship's position based on the flag."""
        # Update the ship's x value, not the rect. 
        if self.moving_right and self.rect.right < self.screen_rect.right: #this all makes it so we can edit the ship_speed to change the speed
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: #this is keeping the ship on the screen
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x # still the position of the ship

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) #puts the image at the location specificed by self.rect