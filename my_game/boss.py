from random import randint

import pygame
from pygame.sprite import Sprite

from boss_bullet import BossBullet


class Boss(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load('images/sashka.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y = self.rect.top + 120

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.boss_defeated = False

    def check_boss_edges(self):
        """Return True ia enemy is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.settings.boss_speed * self.settings.fleet_direction
        self.rect.x = self.x



    def take_damage(self):
        self.settings.boss_hp -= self.settings.bullets_damage

    def draw_boss(self):
        self.screen.blit(self.image, self.rect)






