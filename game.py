import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Pyng Pong')
        pygame.display.set_icon(pygame.image.load('assets/icon.png'))
        self.main_font = pygame.font.Font('assets/fonts/cocogoose.ttf', 42)
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.delta = 0
        self.scene = 0

    def __del__(self):
        pygame.font.quit()
        pygame.quit()
