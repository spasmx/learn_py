import sys
import time
from random import randint

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
from components import Components
from boss import Boss
from human import Human
from bullet import Bullet
from enemy import Enemy
from boss_bullet import BossBullet
from health_bar import HealthBar


class MyGame:

    def __init__(self):
        """Initialize class and create game resources"""
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # For fullscreen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('The BEST GAME')
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)
        self.comp = Components(self)
        self.human = Human(self)
        self.boss = Boss(self)
        self.hb = HealthBar(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.boss_bullets = pygame.sprite.Group()

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
        available_space_y = self.settings.screen_height - (4 * enemy_height) - human_height
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
            self.sb.prep_level()
            self.sb.prep_humans()
            # Delete aliens and bullets
            self.enemies.empty()
            self.bullets.empty()
            # Create the new fleet and ship in center
            self._create_fleet()
            self.human.center_human()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
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
            self.comp.shot_sound.play()

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
                self.comp.kill_enemy_sound.play()
            self.sb.prep_score()
            self.sb.check_hight_score()
        if not self.enemies and not self.stats.level % 3 == 0:
            self._update_stats()
            self._create_fleet()
        else:
            self.create_boss()

    def _update_stats(self):
        if not self.boss.boss_defeated:
            self.bullets.empty()
            self.boss_bullets.empty()
            self.stats.level += 1
            self.settings.increase_speed()
            self.sb.prep_level()
            self.comp.win_sound.play()
            self.comp.show_win_image()
            pygame.display.flip()
            time.sleep(1.5)
            self.human.center_human()
        self.boss.boss_defeated = False

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

    def create_boss(self):
        if self.stats.level % 3 == 0 and not self.boss.boss_defeated:
            self.enemies.empty()
            self.boss.draw_boss()
            self._hit_boss()
            self._update_boss()
            self._create_health_bar()

    def _create_health_bar(self):
        self.hb.update()
        self.hb.draw_hb()

    def _hit_boss(self):
        if pygame.sprite.spritecollideany(self.boss, self.bullets):
            for bullet in self.bullets.sprites():
                self.boss.take_damage()
                bullet.kill()
            self._is_boss_dead()

    def _update_boss(self):
        self.boss.check_boss_edges()
        self._check_boss_edges()
        self.boss.update()
        if self.boss.rect.colliderect(self.human.rect):
            self._human_hit()
            self.sb.prep_humans()

    def _check_boss_edges(self):
        """React according to whether any of the aliens have reached the edge of the screen"""
        if self.boss.check_boss_edges():
            self._change_fleet_direction()

    def _change_boss_direction(self):
        """Descent of the fleet and change of direction"""
        self.boss.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _is_boss_dead(self):
        if self.settings.boss_hp <= 0:
            self.boss.kill()
            self.stats.score += self.settings.boss_points
            self._update_stats()
            self.boss.boss_defeated = True
            self.settings.boss_hp = 100

    def _shot(self):
        if randint(1, 1000) == 1:
            self.create_boss_bullets()

    def create_boss_bullets(self):
        if len(self.boss_bullets) < self.settings.boss_bullets_allowed:
            new_bullet = BossBullet(self)
            self.boss_bullets.add(new_bullet)
            self.comp.boss_shot_sound.play()

    def _update_boss_bullets(self):
        self.boss_bullets.update()
        for bullet in self.boss_bullets.copy():
            if bullet.rect.bottom < 0:
                self.boss_bullets.remove(bullet)

            if bullet.rect.colliderect(self.human.rect):
                self._human_hit()
                self.sb.prep_humans()
                self.boss_bullets.remove(bullet)

    def _human_hit(self):
        """React to the collision of the alien with the ship"""
        if self.stats.humans_left > 0:
            # Reduce ships_left
            self.stats.humans_left -= 1
            self.sb.prep_humans()
            # Delete all enemies and bullets
            self.enemies.empty()
            self.bullets.empty()
            self.boss_bullets.empty()
            # Create new fleet and ship
            self._create_fleet()
            self.human.center_human()
            # Pause
            self.comp.lose_sound.play()
            self.comp.show_lose_image()
            pygame.display.flip()
            time.sleep(1.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Refresh screen and switch to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.human.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.boss_bullets.sprites():
            bullet.draw_boss_bullet()
        self.enemies.draw(self.screen)
        self.sb.show_score()
        self.create_boss()
        self._update_boss()
        # Draw a button "Play" if the game not active
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def start_game(self):
        while True:
            self._check_events()
            self.play_button.update()
            if self.stats.game_active:
                self.human.update()
                self._update_bullets()
                self._update_enemies()
                if self.stats.level % 3 == 0:
                    self._update_boss_bullets()
                    self._shot()

            self._update_screen()


if __name__ == '__main__':
    game = MyGame()
    game.start_game()
