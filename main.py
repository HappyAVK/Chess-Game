import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
color = 0
board_made = False
class Square:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def instantiate(self, colour):
        pygame.draw.rect(screen, colour, (self.x_pos, self.y_pos, 80, 80))

    @staticmethod
    def colourDecision(value):
        white = (200, 200, 200)
        black = (10, 10, 10)
        if (value % 2) == 0:
            print(value % 2)
            return black
        else:
            print(value % 2)
            return white



## chess board setup

while True:
    if board_made != True:
        board = pygame.draw.rect(screen, (100, 100, 100), (10, 10, 640, 640))
        for X in range(0, 640, 80):

            for Y in range(0, 640, 80):
                if Y == 0:
                    color += 1
                square = Square(X, Y)
                c = square.colourDecision(value=color)
                print(c)
                square.instantiate(c)
                color += 1
        board_made = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)