import pygame

class BaseGame:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.active = True
        self.next_game = None # Signalisiert, welches Spiel als nächstes kommt

    def handle_events(self, events):
        """Muss im Sub-Spiel überschrieben werden"""
        pass

    def update(self):
        """Muss im Sub-Spiel überschrieben werden"""
        pass

    def draw(self):
        """Muss im Sub-Spiel überschrieben werden"""
        pass