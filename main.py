import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
color = 0
board_made = False
board_x =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
board_y =[8, 7, 6, 5, 4, 3, 2, 1]
class Square:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def instantiate(self, colour):
        pygame.draw.rect(screen, colour, (self.x_pos, self.y_pos, 80, 80))

    @staticmethod
    def colour_decision(value):
        white = (200, 200, 200) # RGB values for B/W
        black = (10, 10, 10)
        if (value % 2) == 0:

            return black
        else:

            return white

class Board:
    def __init__(self):
        self.board_positions = [[board_x],[board_y]]
        self.tile_objects = {}

    def add_tile(self, tile, x ,y):
        letter = board_x[int(x/80)]
        print(int(x/80),int(y/80))
        number = board_y[int(y/80)]
        self.tile_objects[tile] = [letter, number, [x, y]] # a dictionary of lists containing x y gamepy positions and classic chess positions






while True:
    ## chess board setup
    if not board_made:
        board = pygame.draw.rect(screen, (100, 100, 100), (10, 10, 640, 640))
        board = Board()
        for X in range(0, 640, 80):

            for Y in range(0, 640, 80):
                if Y == 0:
                    color += 1
                square = Square(X, Y)
                c = square.colour_decision(value=color)

                square.instantiate(c)
                board.add_tile(tile=f"{X}, {Y}", x=X, y=Y)
                color += 1
        print(board.tile_objects)
        board_made = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)