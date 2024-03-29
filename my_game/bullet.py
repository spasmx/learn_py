import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for manage a human bullets"""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = game.human.rect.midtop

        # Save bullet position in float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the ball
        self.y -= self.settings.bullet_speed
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on the screen"""
        self.screen.blit(self.image, self.rect)