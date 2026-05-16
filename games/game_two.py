import pygame
from base_game import BaseGame

class GameTwo(BaseGame):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.font = pygame.font.SysFont("Arial", 32)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Münze sammeln
                    self.settings.gold_coins -= 1

    def update(self):
        pass

    def draw(self):
        self.screen.fill((50, 50, 150)) # Blaues Design
        text = self.font.render(f"Spiel 2 - Gold: {self.settings.gold_coins} - ENTER zum Wechseln", True, (255, 255, 255))
        self.screen.blit(text, (50, 250))