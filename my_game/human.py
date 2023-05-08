import pygame
from pygame.sprite import Sprite


class Human(Sprite):
    """Human control class"""

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('images/1.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def change_size(self):
        """Change size image for display human life"""
        new_size = (self.image.get_width() // 2, self.image.get_height() // 2)
        resized_human = pygame.transform.scale(self.image, new_size)
        self.image = resized_human
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-self.rect.width // 2, -self.rect.height // 2)

    def _update_x_coordinate(self):
        """Update human position based on move x-coordinate"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.human_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.human_speed

        self.rect.x = self.x

    def _update_y_coordinate(self):
        """Update human position based on move y-coordinate"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.human_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.human_speed

        self.rect.y = self.y

    def update(self):
        """Update human position based on move indicator"""
        self._update_x_coordinate()
        self._update_y_coordinate()

    def blitme(self):
        """Draw the human in current location"""
        self.screen.blit(self.image, self.rect)

    def center_human(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
