import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

is_game_running = True
while is_game_running: 
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_game_running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        is_game_running = False
 
  # Render!
  cornflower_blue = (100, 149, 237)
  screen.fill(cornflower_blue)
  pygame.draw.rect(screen, (255, 0, 0), (20, 30, 100, 10))
  pygame.draw.circle(screen, (0, 255, 0), (screen_width // 2, screen_height // 2), 30)
  pygame.draw.line(screen, (0, 0, 0), (0, 0), (screen_width, screen_height))
  pygame.display.flip()

