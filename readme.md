projekt_ordner/ /n
│ /n
├── main.py              # Der "Manager", der zwischen Spielen wechselt
├── settings.py          # Die globalen SuperSettings
├── base_game.py         # Die Superklasse (Super_init)
└── games/               # Unterordner für die Sub-Spiele
    ├── __init__.py      # Macht den Ordner zum Python-Package
    ├── game_one.py
    ├── game_two.py
    └── game_three.py
