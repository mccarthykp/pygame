from game_object import GameObject
from random import randint, choice

class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'src/images/bomb.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  # add ability to move up, down, left or right
  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
      self.reset()

    if self.x > 500:
      self.reset()

  # reset should randomly choose whether the bomb will move up, down, left or right
  def reset(self):
    x_coordinates = [93, 218, 343]
    y_coordinates = [-64, 564]
    self.x = choice(x_coordinates)
    self.y = choice(y_coordinates)
    