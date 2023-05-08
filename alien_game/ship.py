import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Ship control class"""

    def __init__(self, ai_game):
        """Initialize the ship and set its default position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Download ship image and get its rect
        self.image = pygame.image.load('images/ship_white.bmp')
        self.rect = self.image.get_rect()

        # Create a new ship each time down and in the center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Save float for a ship position on x-coordinate
        self.x = float(self.rect.x)

        # Move indicator
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position based on move indicator"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw the ship in current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

