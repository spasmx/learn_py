import pygame


class Components:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.win_img = pygame.image.load('images/win_img.bmp')
        self.win_img_rect = self.win_img.get_rect()
        self.win_img_rect.center = self.screen_rect.center

        self.lose_img = pygame.image.load('images/lose_img.bmp')
        self.lose_img_rect = self.lose_img.get_rect()
        self.lose_img_rect.center = self.screen_rect.center

    def show_win_image(self):
        self.screen.blit(self.win_img, self.win_img_rect)

    def show_lose_image(self):
        self.screen.blit(self.lose_img, self.lose_img_rect)



