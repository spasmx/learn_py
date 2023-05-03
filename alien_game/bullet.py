import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for manage a ship bullets"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect at (0, 0) and task to correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_wight, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

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
        pygame.draw.rect(self.screen, self.color, self.rect)
