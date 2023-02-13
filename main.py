import pygame
from sys import exit
import pandas as pd

import pieces
from pieces import Piece
from Game_Mechanics import Turn

pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
color = 0
Game_Start = False
board_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
board_y = [8, 7, 6, 5, 4, 3, 2, 1]
White_Turn = True
white_pieces = {}
black_pieces = {}
selecting = False
image_ = pygame.image.load("graphics/Pawn_Black.png").convert_alpha()
places = {}
df = pd.read_csv("Chess_piece_info.csv")

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

        for p in df.loc[:, "White-position"]:

            img = df.loc[df["White-position"] == p, "White-Image"].squeeze()



            test_piece = Piece()

            piece_position = test_piece.placement(board.tile_objects[p], img, screen)

            name = df.loc[df["White-position"] == p, "Piece"].squeeze()

            white_pieces["{}".format(name)] = piece_position # a dictionary of white_pieces



        for p in df.loc[:, "Black-position"]:

            img = df.loc[df["Black-position"] == p, "Black-Image"].squeeze()



            test_piece = Piece()

            piece_position = test_piece.placement(board.tile_objects[p], img, screen)

            name = df.loc[df["Black-position"] == p, "Piece"].squeeze()

            black_pieces["{}".format(name)] = piece_position  # a dictionary of black_pieces




while True:
    pygame.display.update()
    mouse = pygame.mouse.get_pos()
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

        # testing instantiation of a piece

        Game_Start = True
    else:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():


            if White_Turn:

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    w_turn = Turn()
                    for key, value in white_pieces.items():


                        if not selecting:
                            selections_, selected_piece = w_turn.start_move(piece=value, mousepos=mouse, selecting_=selecting)

                        for index, i in enumerate(selections_):
                            pos_option_rect = image_.get_rect(topleft=i)
                            screen.blit(image_, pos_option_rect)
                            places["place {}".format(index)] = pos_option_rect

                            selecting = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and selecting:
                    print(places)

                    for k, v in places.items():

                        n_piece = pieces.Piece
                        name = list(white_pieces.keys())[list(white_pieces.values()).index(selected_piece)]
                        replace_img = df.loc[df["Piece"] == name, "White-Image"].squeeze()
                        new_pos = w_turn.get_new_place(mouse, v, replace_img, screen)


                         #new_pos = new_piece.placement()

                    # Selected piece needs to be moved somehow to the new location, there should be a way to do this




        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(60)
