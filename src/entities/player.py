import pygame

FRICTION = 1.0


class Player:
    def __init__(self, player: str, color: str):
        self.player = player

        if self.player != "left" and self.player != "right":
            self.player = "left"

        self.color = color
        self.position = pygame.Vector2(0, 0)
        self.width = 25.0
        self.height = 100.0
        self.speed = 0.0
        self.acceleration = 0.0

    def move_up(self):
        self.acceleration -= FRICTION + 0.5

    def move_down(self):
        self.acceleration += FRICTION + 0.5

    def process(self, screen: pygame.Surface, delta: float):
        if self.position == (0, 0) and self.player == "left":
            self.position = pygame.Vector2(
                20, screen.get_height() / 2 - self.height / 2
            )

        if self.position == (0, 0) and self.player == "right":
            self.position = pygame.Vector2(
                screen.get_width() - self.width - 20,
                screen.get_height() / 2 - self.height / 2,
            )

        # collision top
        if self.position.y <= 0:
            self.speed *= -1

        # collision bottom
        if self.position.y + self.height >= screen.get_height():
            self.speed *= -1

        if self.acceleration < 0:
            self.speed += self.acceleration
            self.acceleration += FRICTION

        if self.acceleration > 0:
            self.speed += self.acceleration
            self.acceleration -= FRICTION

        self.position.y += self.speed * delta

        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(self.position.x, self.position.y, self.width, self.height),
        )
