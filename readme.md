Basic "Game-Engine" - an example on how to switch between several games in pygame while the basic game window stays the same. Variables can be in-game or in the super game class.


projekt_ordner/
    main.py              # Der "Manager", der zwischen Spielen wechselt
    settings.py          # Die globalen SuperSettings
    base_game.py         # Die Superklasse (Super_init)
    games/               # Unterordner für die Sub-Spiele
        __init__.py      # Macht den Ordner zum Python-Package
        game_one.py
        game_two.py
        game_three.py
    
by me & Marco Gilg
