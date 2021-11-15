import pygame
from fruits import Apple, Strawberry
from player import Player

pygame.init()
screen = pygame.display.set_mode([500, 500])

clock = pygame.time.Clock()
apple = Apple()
strawberry = Strawberry()
player = Player()

running = True
while running:
  screen.fill((255, 255, 255))
  
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # Check for event type KEYBOARD
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
  
  strawberry.move()
  strawberry.render(screen)

  apple.move()
  apple.render(screen)

  player.move()
  player.render(screen)

  pygame.display.flip()
  clock.tick(90)