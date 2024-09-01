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

  for component_name in game.ui_components['menu']:
    component = game.ui_components['menu'][component_name]
    component.process()

  pygame.display.flip()
  game.delta = game.clock.tick(60) / 1000
