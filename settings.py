class SuperSettings:
    def __init__(self):
        # Bildschirm-Konstanten
        self.screen_width = 800
        self.screen_height = 600
        self.fps = 60
        
        # Spiel-Übergreifende Daten (Items, Stats)
        self.gold_coins = 0
        self.lives = 3
        self.current_level = 0