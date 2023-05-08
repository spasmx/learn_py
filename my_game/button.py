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

    # def change_bg_size(self):
    #     if self.bg_image_rect.width < self.screen_rect.width or self.bg_image_rect.height < self.screen_rect.height:
    #         scale = min(self.screen_rect.width / self.bg_image_rect.width,
    #                     self.screen_rect.height / self.bg_image_rect.height)
    #         new_width = int(self.bg_image_rect.width * scale)
    #         new_height = int(self.bg_image_rect.height * scale)
    #         new_size = pygame.transform.scale(self.bg_image, (new_width, new_height))
    #
    #         self.bg_image_rect = new_size.get_rect(center=self.screen.get_rect().center)

    def draw_button(self):
        self.screen.blit(self.bg_image, self.bg_image_rect)
        self.screen.blit(self.image, self.image_rect)


