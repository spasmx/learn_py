import pygame


class Button:

    def __init__(self, game):
        """Initialize button atr"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Create background for button
        self.bg_image = pygame.image.load('images/Untitled.bmp')
        self.bg_image_rect = self.bg_image.get_rect()

        # Create image button
        self.image = pygame.image.load('images/play_button.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.blit(self.bg_image, self.bg_image_rect)
        self.screen.blit(self.image, self.image_rect)
