import pygame


class Components:

    def __init__(self, game):

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.win_img = pygame.image.load('images/win_img.bmp')
        self.win_img_rect = self.win_img.get_rect()
        self.win_img_rect.center = self.screen_rect.center

        self.lose_img = pygame.image.load('images/lose_img.bmp')
        self.lose_img_rect = self.lose_img.get_rect()
        self.lose_img_rect.center = self.screen_rect.center
        # Sounds
        self.shot_sound = pygame.mixer.Sound('sounds/compute-key.wav')
        self.kill_enemy_sound = pygame.mixer.Sound('sounds/kill-enemy-8-bit.wav')
        self.boss_shot_sound = pygame.mixer.Sound('sounds/snake-hissing.mp3')
        self.win_sound = pygame.mixer.Sound('sounds/8-bit-mini-win-sound-effect.wav')
        self.lose_sound = pygame.mixer.Sound('sounds/lose-sound.wav')
        self.game_over_sound = pygame.mixer.Sound('sounds/8-bit-game-over.wav')

        self.kill_enemy_sound.set_volume(0.1)
        self.shot_sound.set_volume(0.3)

    def show_win_image(self):
        self.screen.blit(self.win_img, self.win_img_rect)

    def show_lose_image(self):
        self.screen.blit(self.lose_img, self.lose_img_rect)



