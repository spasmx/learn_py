import pygame
from pygame.sprite import Sprite


class Boss(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load('images/sashka.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.boss_defeated = False

    def check_boss_edges(self):
        pass

    def update(self):
        pass

    def take_damage(self):
        self.settings.boss_hp -= self.settings.bullets_damage

    def draw_boss(self):
        """Draw boss"""
        self.screen.blit(self.image, self.rect)






