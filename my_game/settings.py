class Settings:
    """A class to save all settings"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (185, 185, 185)
        self.human_speed = 1.5
        self.human_limit = 3

        self.bullet_speed = 1.0
        self.bullet_width = 30
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.enemy_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction 1 meaning move direction on the right, -1 - on the left
        self.fleet_direction = 1