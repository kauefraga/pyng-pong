import pygame

class Game:
  """The game object/main manager"""

  def __init__(self):
    pygame.init()
    pygame.display.set_caption('Pyng Pong')
    pygame.display.set_icon(pygame.image.load('assets/icon.png'))
    self.screen = pygame.display.set_mode((1280, 720))

    pygame.font.init()
    self.md_text_font = pygame.font.Font('assets/fonts/cocogoose.ttf', 32)
    self.lg_text_font = pygame.font.Font('assets/fonts/cocogoose.ttf', 72)
    self.number_font = pygame.font.Font('assets/fonts/roboto.ttf', 72)

    self.clock = pygame.time.Clock()
    self.running = True
    self.delta = 0
    self.scene = 0

  def __del__(self):
    pygame.font.quit()
    pygame.quit()
