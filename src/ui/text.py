import pygame

class Text:
  """Text component"""

  def __init__(self, position: pygame.Vector2, label: str, color: str):
    """Prepare a text component to be rendered"""
    self.position = position
    self.label = label
    self.color = color

  def process(self, screen: pygame.Surface, font: pygame.font.Font):
    """Render the text component on the screen"""
    text_surface = font.render(self.label, True, self.color)

    self.position.x -= text_surface.get_width() / 2
    self.position.y -= text_surface.get_height() / 2

    screen.blit(text_surface, self.position)
