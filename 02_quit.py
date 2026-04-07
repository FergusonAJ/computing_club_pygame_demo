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
