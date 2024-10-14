import pygame
from game import Game

from entities.ball import Ball
from entities.player import Player

ball = Ball(25, "#ffd343")

left_player = Player("left", "#3776ab")
right_player = Player("right", "#3776ab")


def gameplay_scene(game: Game):
    if not ball.is_loaded:
        ball.load_resources()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game.scene = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_player.move_up()
    if keys[pygame.K_s]:
        left_player.move_down()
    if keys[pygame.K_UP]:
        right_player.move_up()
    if keys[pygame.K_DOWN]:
        right_player.move_down()

    game.screen.fill("#141418")

    left_player.process(game.screen, game.delta)
    right_player.process(game.screen, game.delta)

    ball.process(game.screen, game.delta)

    pygame.display.flip()
    game.delta = game.clock.tick(60) / 1000
