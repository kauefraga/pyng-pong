import random

import pygame

class Ball:
  def __init__(self, radius: float, color: str):
    self.radius = radius
    self.color = color
    self.position = pygame.Vector2(0, 0)
    self.speed = pygame.Vector2(0, 0)

  def process(self, screen: pygame.Surface, delta: float):
    if self.position == (0, 0):
      self.position.x = screen.get_width() / 2
      self.position.y = screen.get_height() / 2

    if self.speed == (0, 0):
      self.speed.x = 250 if round(random.randint(0, 1)) == 0 else -250
      self.speed.y = 100 if round(random.randint(0, 1)) == 0 else -100

    # collision left
    if self.position.x - self.radius <= 0:
      self.speed.x *= -1

    # collision top
    if self.position.y - self.radius <= 0:
      self.speed.y *= -1

    # collision right
    if self.position.x + self.radius >= screen.get_width():
      self.speed.x *= -1

    # collision bottom
    if self.position.y + self.radius >= screen.get_height():
      self.speed.y *= -1

    self.position += self.speed * delta

    pygame.draw.circle(screen, self.color, self.position, self.radius)
