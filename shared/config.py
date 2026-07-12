SCREEN_W, SCREEN_H = 960, 540
TILE_SIZE = 32
FPS_CAP = 120

# Simulation (MUST match on client + server)
FIXED_DT = 1 / 60  # seconds of simulated time per physics step
GRAVITY = 2000.0  # px/s^2  (M.2)
MOVE_SPEED = 260.0  # px/s
TERMINAL_VY = 1400.0  # px/s fall-speed cap

# Jump tuned by desired height in tiles (derived in Stage 1.5)
JUMP_HEIGHT_TILES = 3.2
JUMP_VELOCITY = (2 * GRAVITY * JUMP_HEIGHT_TILES * TILE_SIZE) ** 0.5  # = √(2gH), M.6

# Networking
TICK_RATE = 30  # authoritative snapshots per second
INTERP_DELAY = 0.10  # render remote players 100 ms in the past (8.8)

# Combat
BULLET_SPEED = 700.0
SWORD_COOLDOWN = 0.35
GUN_COOLDOWN = 0.18
IFRAME_TIME = 0.8
