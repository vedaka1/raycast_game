import math


WIDTH = 1280
HEIGHT = 720
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 80
FPS_POS = (WIDTH - 65, 5)
MAP_SCALE = 5
MAP_TILE = TILE / MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 320
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
SCALE = WIDTH / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = DIST * TILE


player_position = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 220, 0)
RED = (220, 0, 0)
SKYBLUE = (0, 90, 220)
DARKGRAY = (110, 110, 110)
YELLOW = (220, 220, 0)