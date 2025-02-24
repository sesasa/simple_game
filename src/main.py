import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Window")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player setup
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
velocity = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Delay to control frame rate
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= velocity
    if keys[pygame.K_RIGHT]: player.x += velocity
    if keys[pygame.K_UP]: player.y -= velocity
    if keys[pygame.K_DOWN]: player.y += velocity

    pygame.draw.rect(screen, RED, player)
    pygame.display.update()

pygame.quit()
