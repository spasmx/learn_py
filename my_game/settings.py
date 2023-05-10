class Settings:
    """A class to save all settings"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (185, 185, 185)

        self.human_limit = 3

        # self.bullet_width = 30
        # self.bullet_height = 30
        # self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10
        self.bullets_damage = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.boss_bullets_allowed = 100000
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.human_speed = 1.5
        self.bullet_speed = 0.8
        self.enemy_speed = 0.3
        self.boss_speed = 0.1
        self.boss_bullet_speed = 0.3

        # fleet_direction 1 meaning move direction on the right, -1 - on the left
        self.fleet_direction = 1
        self.enemy_points = 50
        self.boss_points = 10000
        self.boss_hp = 100

    def increase_speed(self):
        """Speed Up"""
        self.human_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.boss_bullet_speed += 0.1
        self.enemy_speed *= self.speedup_scale
        self.enemy_points = int(self.enemy_points * self.score_scale)

