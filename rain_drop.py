import sys
import pygame

from rain import Rain
from settings import Settings


class RainFlow():
    """A class representing the rain fl0w
    """

    def __init__(self,):
        """Initialize the settings and the game recourses"""
        pygame.init()
        self.settings = Settings()

        # # Fullscreen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height 


        # Normal screen mode
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) 
        
        """
        Note: To enable fullscreen mode, remove the '#' from the Fullscreen mode line and add '#' to the Normal mode line.
        """

        pygame.display.set_caption(self.settings.game_title) # The game title 

        # Make the rainflow in a group form
        self.rains = pygame.sprite.Group()

        # create a group of rainflow
        self._create_fleet()

    def run_game(self):
        """Reponse for the game running
        """
        game_running = True
        while game_running:
            self._check_events()
            self._update_rains()
            self._update_rainsflow()
            self._update_screen()

    def _check_events(self):
        """Respond to keypress and mouse events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_fleet(self):
        """Create the fleet of rain
        """
        # Create a rain and find the number of a rains in a row
        # Spacing between each rain is equal to one rain width.
        rain = Rain(self)  # rain is use for calculation and spacing here.

        rain_width, rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - (2 * rain_width)

        self.number_rains_x = available_space_x // (2 * rain_width)

        # Determine the number of rains that fit on the screen
        available_space_y = (self.settings.screen_height -
                             (3 * rain_height) - rain_height)
        self.number_rows = available_space_y // (2 * rain_height)

        # Create the full fleet of rains
        for row_number in range(self.number_rows):
            for rain_number in range(self.number_rains_x):
                self._create_rain(rain_number, row_number)

    def _create_rain(self, rain_number, row_number):
        """Create a rain
        """
        # Create a rain and place it in the row
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width + 2 * rain_width * rain_number
        rain.rect.x = rain.x

        rain.rect.y = rain.rect.height + 2 * rain.rect.height * row_number

        self.rains.add(rain) # add rain in the rains flow group

    def _update_rainsflow(self):
        """Update position of rains and get rid of old rains.
        """
        # Get rid of rains that has disappeared
        for rain in self.rains.copy():
            if rain.rect.bottom >= self.settings.screen_height:
                self.rains.remove(rain)
                # Create new rain row
                for rain_number in range(self.number_rains_x):
                    self._create_rain(rain_number,  0) 


    def _update_rains(self):
        """Check if an rain is at edge, 
            then update the position of all rains in the fleet.
        """
        self._check_fleet_edges()
            # checking the position of the rain and determinding an action to do with each fleet.
    
        self.rains.update() # update the rain in the screen

    def _check_fleet_edges(self):
        """Respond appropriately if any rains have reached an edge.
        """
        for rain in self.rains.sprites():
            if rain.check_edges():  # call check_edges funtion from the rain.py
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction.
        """
        for rain in self.rains.sprites():
            rain.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    
    def _update_screen(self):
        """Update the screen
        """
        self.screen.fill(self.settings.bg_color)
        self.rains.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    """Create an instance and run the rainflow game"""
    rain_game = RainFlow()
    rain_game.run_game()
