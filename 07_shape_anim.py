import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

circle_radius = 30
circle_x = random.randint(circle_radius, screen_width - circle_radius)
circle_y = random.randint(circle_radius, screen_height - circle_radius)
circle_vel_x = random.uniform(-1, 1)
circle_vel_y = random.uniform(-1, 1)

is_game_running = True
while is_game_running: 
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_game_running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        is_game_running = False

  # Update
  circle_x += circle_vel_x
  circle_y += circle_vel_y
  if circle_x <= circle_radius: 
    circle_vel_x *= -1
    circle_x = circle_radius + 1
  elif circle_x >= screen_width - circle_radius: 
    circle_vel_x *= -1
    circle_x = screen_width - circle_radius - 1
  if circle_y <= circle_radius: 
    circle_vel_y *= -1
    circle_y = circle_radius + 1
  elif circle_y >= screen_height - circle_radius: 
    circle_vel_y *= -1
    circle_y = screen_height - circle_radius - 1
 
  # Render!
  cornflower_blue = (100, 149, 237)
  screen.fill(cornflower_blue)
  pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), circle_radius)
  pygame.display.flip()

