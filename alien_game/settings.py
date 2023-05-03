class Settings:
    """A class to save all settings"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_wight = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.ship_limit = 3

        self.bullet_wight = 1000
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5
        # fleet_direction 1 meaning move direction on the right, -1 - on the left
        self.fleet_direction = 1
        self.alien_points = 1000

    def increase_speed(self):
        """Speed Up"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)