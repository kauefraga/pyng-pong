import pygame

from game import Game
from ui import text

from entities.ball import Ball

ball = Ball(25, '#ffd343')

def menu_scene(game: Game):
  if not ball.is_loaded:
    ball.load_resources()

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

  ball.process(game.screen, game.delta)
  title.process(game.screen, game.lg_text_font)
  hit_enter.process(game.screen, game.md_text_font)

  pygame.display.flip()
  game.delta = game.clock.tick(60) / 1000
