import pygame

class Text:
  """Text component"""

  def __init__(self, position: tuple[float, float], screen_surface: pygame.Surface, text_surface: pygame.Surface):
    self.position = position
    self.screen_surface = screen_surface
    self.text_surface = text_surface

  def process(self):
    self.screen_surface.blit(self.text_surface, self.position)
