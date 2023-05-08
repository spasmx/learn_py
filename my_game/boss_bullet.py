import pygame
from pygame.sprite import Sprite
from random import randint



class BossBullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.boss = game.boss

        self.image = pygame.image.load('images/1c.bmp')
        self.rect = self.image.get_rect()

        self.rect.centerx = game.boss.rect.centerx
        self.rect.top = game.boss.rect.bottom

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet down the screen"""
        # Update the decimal position of the ball
        self.y += self.settings.boss_bullet_speed
        # Update rect position
        self.rect.y = self.y
        if self.rect.bottom < 0:
            self.kill()

    def draw_boss_bullet(self):
        self.screen.blit(self.image, self.rect)

