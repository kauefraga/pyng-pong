from game import Game
from menu import menu_scene
from gameplay import gameplay_scene

scenes = {
    0: menu_scene,
    1: gameplay_scene
}

def run_game():
    game = Game()

    while game.running:
        scene = scenes.get(game.scene)
        scene(game)

if __name__ == '__main__':
    run_game()
