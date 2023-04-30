import pygame
import sys
from settings import Settings
from human import Human
from bullet import Bullet


class MyGame:

    def __init__(self):
        """Initialize class and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_wight, self.settings.screen_height))
        pygame.display.set_caption('My Game')
        self.human = Human(self)
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.human.moving_right = True
        elif event.key == pygame.K_a:
            self.human.moving_left = True
        elif event.key == pygame.K_w:
            self.human.moving_up = True
        elif event.key == pygame.K_s:
            self.human.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.human.moving_right = False
        elif event.key == pygame.K_a:
            self.human.moving_left = False
        elif event.key == pygame.K_w:
            self.human.moving_up = False
        elif event.key == pygame.K_s:
            self.human.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add in bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet position and get rid of missing bullets"""
        # Update position
        self.bullets.update()
        # get rid of missing bullets
        for bullet in self.bullets.copy():
            if bullet.rect.top <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.human.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def start_game(self):
        while True:
            self._check_events()
            self.human.update()
            self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    game = MyGame()
    game.start_game()
