import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """Create one enemy"""

    def __init__(self, game):
        """Initialize the enemy and set its default position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Download enemy image and get its rect
        self.image = pygame.image.load('images/1c.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True ia enemy is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.settings.enemy_speed * self.settings.fleet_direction
        self.rect.x = self.x
