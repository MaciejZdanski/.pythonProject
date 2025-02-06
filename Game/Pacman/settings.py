from pygame.math import Vector2 as vec

# wymiary ekranu
WIDTH, HEIGHT = 610, 670
FPS = 60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER

# ustawienia kolorystyki
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOUR = (190, 194, 15)

ROWS = 30
COLS = 28

# ustawienia textu
START_TEXT_SIZE = 16
START_FONT = "arial black"


# ustawienia gracza
#PLAYER_START_POS = 0


# ustawienia wrogów (mob)