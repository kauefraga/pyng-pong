import pygame
from game import Game

def menu_scene(game: Game):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game.running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        game.scene = 1

  game.screen.fill('white')

  welcome_text_surface = game.text_font.render('Welcome!', True, 'black')
  game.screen.blit(welcome_text_surface, (
    game.screen.get_width() / 2 - welcome_text_surface.get_width() / 2,
    game.screen.get_height() / 2 - welcome_text_surface.get_height() / 2
  ))

  pygame.display.flip()
  game.delta = game.clock.tick(60) / 1000
