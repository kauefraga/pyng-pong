import pygame

from game import Game
from ui import text

def menu_scene(game: Game):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game.running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        game.scene = 1

  title = text.Text(
    pygame.Vector2(
      game.screen.get_width() / 2,
      game.screen.get_height() / 4
    ),
    'Pyng Pong',
    '#3776ab'
  )
  hit_enter = text.Text(
    pygame.Vector2(
      game.screen.get_width() / 2,
      game.screen.get_height() / 2
    ),
    'Hit enter to start',
    'white'
  )

  game.screen.fill('#141418')

  title.process(game.screen, game.lg_text_font)
  hit_enter.process(game.screen, game.md_text_font)

  pygame.display.flip()
  game.delta = game.clock.tick(60) / 1000
