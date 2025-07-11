class Settings():
    """A class representing the game settings
    """

    def __init__(self,):
        """Initialize the game settings
        """

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (130, 200, 229)
        self.game_title = "Rain Flaw"

        # Rain settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
