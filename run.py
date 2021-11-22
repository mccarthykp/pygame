import pygame
from fruits import Apple, Strawberry
from player import Player
from bomb import Bomb
from random import randint

pygame.init()
screen = pygame.display.set_mode([500, 500])
myfont = pygame.font.SysFont('Comic Sans', 30)

# TODO: Add function to change background on count collected
# TODO: Pygame doesn't support .gif - write a function to update each frame of .gif?
# level_one = pygame.image.load('background/level_one.gif')
# level_two = pygame.image.load('background/level_two.gif')
level_three = pygame.image.load('background/level_three.gif')
# level_four = pygame.image.load('background/level_four.gif')
# level_five = pygame.image.load('background/level_five.gif')
# level_six = pygame.image.load('background/level_six.gif')
# level_seven = pygame.image.load('background/level_seven.gif')

clock = pygame.time.Clock()
apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()
bomb2 = Bomb()
collected = 0

running = True
while running:
  screen.fill((0, 0, 0))
  screen.blit(level_three, [0, 0])
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

  if collected == 2:
    all_sprites.add(bomb2)
    
  for entity in all_sprites:
    entity.move()
    entity.render(screen)

    fruit = pygame.sprite.spritecollideany(player, fruit_sprites, pygame.sprite.collide_rect_ratio(.85))
    if fruit:
      fruit.reset()
      collected += 1
      apple.dy += 0.05
      strawberry.dx += 0.05

    if pygame.sprite.collide_rect_ratio(.85)(player, bomb):
      bomb.reset()
      player.dx = 220
      player.dy = 220
      apple.reset()
      apple.dy = (randint(0, 200) / 100) + 1
      strawberry.reset()
      strawberry.dx = (randint(0, 200) / 100) + 1
      collected = 0
      # running = False

    score_obj = myfont.render(f'Collected: {collected}', True, (0, 0, 0))
    screen.blit(score_obj, (25, 450))

  pygame.display.flip()
  clock.tick(60)
