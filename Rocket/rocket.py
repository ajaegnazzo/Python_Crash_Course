#rocket.py
import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, rocket_game):
        """Initialize the rocket and its starting position."""
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        self.image = pygame.image.load('/Users/andrewgnazzo/Python/Python Crash Course/Projects/Rocket/images/ship.bmp')
        self.rect = self.image.get_rect()

        #starting the rocket in the center of the screen
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: #this all makes it so we can edit the rocket_speed to change the speed
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0: #this is keeping the rocket on the screen
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x # still the position of the rocket
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect) #puts the image at the location specificed by self.rect