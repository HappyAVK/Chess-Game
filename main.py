import pygame
from sys import exit
import pandas as pd
from pieces import Piece


pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
color = 0
Game_Start = False
board_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
board_y = [8, 7, 6, 5, 4, 3, 2, 1]
White_Turn = True


class Square:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def instantiate(self, colour):

        a_tile = pygame.draw.rect(screen, colour, (self.x_pos+100, self.y_pos+80, 80, 80))

    @staticmethod
    def colour_decision(value):
        white = (200, 200, 200)  # RGB values for B/W
        black = (10, 10, 10)
        if (value % 2) == 0:

            return black
        else:

            return white


class Board:
    def __init__(self):
        self.board_positions = [[board_x], [board_y]]
        self.tile_objects = {}

    def add_tile(self, x, y):

        letter = board_x[int(x/80)]

        number = board_y[int(y/80)]

        self.tile_objects[f"{letter}{number}"] = (square.x_pos+100, square.y_pos+80)
        # a dictionary of lists containing x y gamepy positions and classic chess positions

    def set_pieces(self):
        df = pd.read_csv("Chess_piece_info.csv")
        for p in df.loc[:, "White-position"]:
            img = df.loc[df["White-position"] == p, "White-Image"].squeeze()
            l_img = pygame.image.load(img).convert_alpha()
            test_piece = Piece(l_img)
            test_position = test_piece.placement(board.tile_objects[p])  # chess co-ordinates are similar to the ones
            screen.blit(test_piece.image, test_position)

        for p in df.loc[:, "Black-position"]:
            img = df.loc[df["Black-position"] == p, "Black-Image"].squeeze()
            l_img = pygame.image.load(img).convert_alpha()
            test_piece = Piece(l_img)
            test_position = test_piece.placement(board.tile_objects[p])  # chess co-ordinates are similar to the ones
            screen.blit(test_piece.image, test_position)


while True:
    # chess board setup
    if not Game_Start:

        board = Board()
        # These for loops should procedurally place tiles and
        # create a dictionary of each tile that corresponds to real life chess positions
        for X in range(0, 640, 80):

            for Y in range(0, 640, 80):
                if Y == 0:
                    color += 1
                square = Square(X, Y)
                c = square.colour_decision(value=color)

                square.instantiate(c)
                board.add_tile(x=X, y=Y)
                color += 1

        board.set_pieces()
        print(board.tile_objects)
        # testing instantiation of a piece

        Game_Start = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
