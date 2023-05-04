import sys
import time

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
from human import Human
from bullet import Bullet
from enemy import Enemy


class MyGame:

    def __init__(self):
        """Initialize class and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # For fullscreen
        pygame.display.set_caption('The BEST GAME')
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)
        self.human = Human(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self)

    def _create_fleet(self):
        """Create enemy's fleet"""
        # Create new enemies and determine the number of new enemies in a row
        # The distance between enemies is equal to the width of one enemy
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        available_space_x = self.settings.screen_width - (2 * enemy_width)
        number_enemies_x = available_space_x // (2 * enemy_width)

        # Determine how many rows of enemies fit on the screen
        human_height = self.human.rect.height
        available_space_y = (self.settings.screen_height - (6 * enemy_height) - human_height)
        number_rows = available_space_y // (2 * enemy_height)

        # Create the all rows of enemies
        for row_number in range(number_rows):
            for enemy_number in range(number_enemies_x):
                self._create_enemy(enemy_number, row_number)

    def _create_enemy(self, enemy_number, row_number):
        """Create enemy and put it in a row"""
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.x = enemy_width + 2 * enemy_width * enemy_number
        enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
        enemy.rect.x = enemy.x
        self.enemies.add(enemy)

    def _check_fleet_edges(self):
        """React according to whether any of the aliens have reached the edge of the screen"""
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Descent of the fleet and change of direction"""
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.image_rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            # Delete aliens and bullets
            self.enemies.empty()
            self.bullets.empty()
            # Create the new fleet and ship in center
            self._create_fleet()
            self.human.center_human()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.human.moving_right = True
        elif event.key == pygame.K_a:
            self.human.moving_left = True
        elif event.key == pygame.K_w:
            self.human.moving_up = True
        elif event.key == pygame.K_s:
            self.human.moving_down = True
        elif event.key == pygame.K_ESCAPE:
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
        self._check_bullet_enemy_collisions()

    def _check_bullet_enemy_collisions(self):
        # Check if bullet shot in enemy, delete bullet and enemy
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
        self.sb.prep_score()
        if not self.enemies:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_enemies(self):
        self._check_fleet_edges()
        self.enemies.update()

        if pygame.sprite.spritecollideany(self.human, self.enemies):
            self._human_hit()
        self._check_enemies_bottom()

    def _check_enemies_bottom(self):
        screen_rect = self.screen.get_rect()
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= screen_rect.bottom:
                self._human_hit()

    def _human_hit(self):
        """React to the collision of the alien with the ship"""
        if self.stats.humans_left > 0:
            # Reduce ships_left
            self.stats.humans_left -= 1
            # Delete all enemies and bullets
            self.enemies.empty()
            self.bullets.empty()
            # Create new fleet and ship
            self._create_fleet()
            self.human.center_human()
            # Pause
            time.sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Refresh screen and switch to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.human.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)
        self.sb.show_score()
        # Draw a button "Play" if the game not active
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def start_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.human.update()
                self._update_bullets()
                self._update_enemies()
            self._update_screen()


if __name__ == '__main__':
    game = MyGame()
    game.start_game()
