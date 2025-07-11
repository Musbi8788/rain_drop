import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """A class respond to the rain image
    """

    def __init__(self, rd_game):
        """Initialize Sprite and set the rain attributes"""
        super().__init__()

        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the image and set in rect attributes
        self.image = pygame.image.load("images/rain_drop.bmp")
        self.rect = self.image.get_rect()

        # show each new rain flow near to the top screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the rain flow exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if rain is at edge of screen
        """
        # get the screen rect
        screen_rect = self.screen.get_rect()

        # checking the rainflow fleet position in the screen
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, ):
        """Move the rain top to down"""
        self.x += (self.settings.rain_speed * self.settings.fleet_direction)

        # Update the rect.x position
        self.rect.x = self.x
