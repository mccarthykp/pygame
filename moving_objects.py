import pygame
from random import randint, choice
from drawing_objects import GameObject
from player import Player

class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.y > 500:
      self.reset()
  
  def reset(self):
    x_coordinates = [93, 218, 343]
    self.x = choice(x_coordinates)
    self.y = -64
  
class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x > 500:
      self.reset()
  
  def reset(self):
    y_coordinates = [93, 218, 343]
    self.x = -64
    self.y = choice(y_coordinates)


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
