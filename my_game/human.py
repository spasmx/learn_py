import pygame


class Human:
    """Human control class"""

    def __init__(self, my_game):
        self.screen = my_game.screen
        self.settings = my_game.settings
        self.screen_rect = my_game.screen.get_rect()

        self.image = pygame.image.load('images/sashka.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def _update_x_coordinate(self):
        """Update human position based on move x-coordinate"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed

        self.rect.x = self.x

    def _update_y_coordinate(self):
        """Update human position based on move y-coordinate"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.speed

        self.rect.y = self.y

    def update(self):
        """Update human position based on move indicator"""
        self._update_x_coordinate()
        self._update_y_coordinate()

    def blitme(self):
        """Draw the human in current location"""
        self.screen.blit(self.image, self.rect)
