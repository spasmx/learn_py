import pygame


class HealthBar:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.boss = game.boss

        self.x, self.y = self.boss.rect.x, self.boss.rect.y - 30
        self.width, self.height = self.boss.rect.width, 10
        self.health_width = self.width
        self.max_health = self.settings.boss_hp

    def update(self):
        self.health = self.settings.boss_hp
        self.health_width = int(self.width * (self.health / self.max_health))

    def draw_hb(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, self.health_width, self.height))
