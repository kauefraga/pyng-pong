import pygame

class Text:
  """Text component"""

  def __init__(self, position: tuple[float, float], surface: pygame.Surface, text_surface: pygame.Surface):
    self.position = position
    self.surface = surface
    self.text_surface = text_surface

  def process(self):
    self.surface.blit(self.text_surface, self.position)
