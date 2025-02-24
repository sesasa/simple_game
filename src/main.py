import pygame
import os

# Initialize pygame
pygame.init()

# Get the absolute path of the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Asset directories
IMAGE_DIR = os.path.join(BASE_DIR, "assets", "images")
SOUND_DIR = os.path.join(BASE_DIR, "assets", "sounds")

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced Game")

# Load assets
player_image_path = os.path.join(IMAGE_DIR, "player.png")
if not os.path.exists(player_image_path):
    raise FileNotFoundError(f"Error: {player_image_path} not found! Place your sprite there.")

player_image = pygame.image.load(player_image_path)
player_image = pygame.transform.scale(player_image, (50, 50))  # Resize

# Colors
WHITE = (255, 255, 255)

# Player setup
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
velocity = 5

# Load sounds
pygame.mixer.init()
background_music_path = os.path.join(SOUND_DIR, "background.mp3")
move_sound_path = os.path.join(SOUND_DIR, "move.wav")

# Check if sound files exist
if os.path.exists(background_music_path):
    pygame.mixer.music.load(background_music_path)
    pygame.mixer.music.play(-1)  # Loop forever
else:
    print(f"Warning: Background music file '{background_music_path}' not found.")

if os.path.exists(move_sound_path):
    move_sound = pygame.mixer.Sound(move_sound_path)
else:
    move_sound = None
    print(f"Warning: Move sound file '{move_sound_path}' not found.")

# Game loop
running = True
score = 0
font = pygame.font.Font(None, 36)

while running:
    pygame.time.delay(30)  # Frame rate control
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= velocity
        if move_sound: move_sound.play()
    if keys[pygame.K_RIGHT]:
        player.x += velocity
        if move_sound: move_sound.play()
    if keys[pygame.K_UP]:
        player.y -= velocity
        if move_sound: move_sound.play()
    if keys[pygame.K_DOWN]:
        player.y += velocity
        if move_sound: move_sound.play()

    # Draw the sprite instead of a rectangle
    screen.blit(player_image, (player.x, player.y))

    # Display score
    score += 1  # Increase score over time
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
