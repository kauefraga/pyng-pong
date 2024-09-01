import pygame
from components import text, button

class Game:
  """The game object/main manager"""

  def __init__(self):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Pyng Pong')
    pygame.display.set_icon(pygame.image.load('assets/icon.png'))
    self.sm_text_font = pygame.font.Font('assets/fonts/cocogoose.ttf', 20)
    self.md_text_font = pygame.font.Font('assets/fonts/cocogoose.ttf', 56)
    self.number_font = pygame.font.Font('assets/fonts/roboto.ttf', 72)
    self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    self.clock = pygame.time.Clock()
    self.running = True
    self.delta = 0
    self.scene = 0

    self.ui_components = {
      'menu': {},
      'gameplay': {}
    }

    menu_title_surface = self.md_text_font.render('Pyng Pong', True, '#cd412b')
    self.ui_components['menu']['title'] = text.Text(
      (
        self.screen.get_width() / 2 - menu_title_surface.get_width() / 2,
        self.screen.get_height() / 4 - menu_title_surface.get_height() / 2
      ),
      self.screen,
      menu_title_surface
    )

  def __del__(self):
    pygame.font.quit()
    pygame.quit()
