import pygame
from game import Game

from entities.ball import Ball

ball = Ball(25, '#ffd343')

def gameplay_scene(game: Game):
  if not ball.is_loaded:
    ball.load_resources()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game.running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        game.scene = 0

  game.screen.fill('#141418')

  ball.process(game.screen, game.delta)

  pygame.display.flip()
  game.delta = game.clock.tick(60) / 1000
