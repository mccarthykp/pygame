# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
  # remove width & height and add img here
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height))
    # self.surf.fill((255, 0, 255))
    # self.rect = self.surf.get_rect()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
  
  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# box = GameObject(120, 300, 50, 50)

# Create the game loop
# running = True
# while running:
#   screen.fill((255, 255, 255))
  
#   # Looks at events
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       running = False
  
#   for index in range(9):
#     x = ((index % 3) * 170) + 40
#     y = (int(index / 3) * 170) + 40

#     if index == 0 or index == 2 or index == 4 or index == 6 or index == 8:
#       apple = GameObject(x, y, 'apple.png')
#       apple.render(screen)
#     elif index == 1 or index == 3 or index == 5 or index == 7 or index == 9:
#       strawberry = GameObject(x, y, 'strawberry.png')
#       strawberry.render(screen)

  # box.render(screen)
  # apple.render(screen)
  # strawberry.render(screen)
  # Update the window
  # pygame.display.flip()
