#Settings for alien_invasion
class Settings:
    """A class to store all settings for the Rocket Game."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.rocket_speed = 1.5