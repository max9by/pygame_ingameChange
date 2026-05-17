import pygame
import sys
from settings import SuperSettings
from games.game_one import GameOne
from games.game_two import GameTwo

class SuperManager:
    def __init__(self):
        pygame.init()
        self.settings = SuperSettings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Mein Super Pygame Projekt")
        self.clock = pygame.time.Clock()

        # Spielauswahl als Liste/Array
        # Wir initialisieren die Spiele hier oder dynamisch beim Wechsel
        self.game_list = [
            GameOne(self.screen, self.settings),
            GameTwo(self.screen, self.settings), 
            # GameThree(self.screen, self.settings)
        ]
        
        self.current_game_index = 0
        self.running = True

    def handle_enter_key(self):
        self.current_game_index += 1
        if self.current_game_index >= len(self.game_list):
            self.current_game_index = 0
        self.switch_game(self.current_game_index)
        
   #    Variable change of games using modolo operation 
   # def handle_enter_key(self):
   #     """Behandelt die Enter-Taste zum Wechsel des Spiels"""
   #     # Zum nächsten Spiel wechseln (zyklisch)
   #     next_index = (self.current_game_index + 1) % len(self.game_list)
   #     self.switch_game(next_index)

    def run(self):
        while self.running:
            # Aktuelles Sub-Spiel holen
            current_game = self.game_list[self.current_game_index]
            
            # Events zentral sammeln
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.handle_enter_key()

            # Logik des Sub-Spiels
            current_game.handle_events(events)
            current_game.update()
            
            # Zeichnen
            current_game.draw()
            pygame.display.flip() # = pygame.display.update()
            self.clock.tick(self.settings.fps)

        pygame.quit()
        sys.exit()

    def switch_game(self, next_index):
        print(f"Wechsel zu Spiel Index: {next_index}")

if __name__ == "__main__":
    manager = SuperManager()
    manager.run()
