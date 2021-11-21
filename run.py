import pygame
from fruits import Apple, Strawberry
from player import Player
from bomb import Bomb
from random import randint

pygame.init()
screen = pygame.display.set_mode([500, 500])

clock = pygame.time.Clock()
apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()

running = True
while running:
  collected = 0
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
  
  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)
  all_sprites.add(apple)
  all_sprites.add(strawberry)
  all_sprites.add(bomb)

  fruit_sprites = pygame.sprite.Group()
  fruit_sprites.add(apple)
  fruit_sprites.add(strawberry)

  for entity in all_sprites:
    entity.move()
    entity.render(screen)

    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
      fruit.reset()
      collected += 1
      apple.dy += 0.05
      strawberry.dx += 0.05

    if pygame.sprite.collide_rect(player, bomb):
      bomb.reset()
      player.dx = 220
      player.dy = 220
      apple.reset()
      apple.dy = (randint(0, 200) / 100) + 1
      strawberry.reset()
      strawberry.dx = (randint(0, 200) / 100) + 1
      collected = 0
      # running = False

  pygame.display.flip()
  clock.tick(90)