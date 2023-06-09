# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
size = width, height = 320, 240
screen: pygame.Surface = pygame.display.set_mode(size)
clock: pygame.time.Clock = pygame.time.Clock()
running = True
dt = 0

player_pos: pygame.Vector2 = pygame.Vector2(
    screen.get_width() / 2, screen.get_height() / 2
)
status_text: pygame.font.Font = pygame.font.Font(None, 32)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color to wipe away anything from last frame.
    screen.fill("purple")

    # Draw player.
    radius: float = 40
    pygame.draw.circle(screen, "red", player_pos, radius)

    # Directional input.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Collision detection with the world.
    if player_pos.x - radius < 0:
        player_pos.x = radius
    if player_pos.x + radius > width:
        player_pos.x = width - radius
    if player_pos.y - radius < 0:
        player_pos.y = radius
    if player_pos.y + radius > height:
        player_pos.y = height - radius

    # Update status text.
    text_surf: pygame.Surface = status_text.render(
        f"({round(player_pos.x, 1)}, {round(player_pos.y, 1)})", True, "black"
    )
    text_rect: pygame.Rect = text_surf.get_rect()
    screen.blit(text_surf, (width - text_rect.width - 10, height - text_rect.height))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
