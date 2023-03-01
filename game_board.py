import pygame
import pieces
board_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
board_y = [8, 7, 6, 5, 4, 3, 2, 1]



class Square:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def instantiate(self, colour, scr):

        pygame.draw.rect(scr, colour, (self.x_pos+100, self.y_pos+80, 80, 80))

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

    def add_tile(self, x, y, sqr):

        letter = board_x[int(x/80)]

        number = board_y[int(y/80)]

        self.tile_objects[f"{letter}{number}"] = (sqr.x_pos+100, sqr.y_pos+80)
        # a dictionary of lists containing x y gamepy positions and classic chess positions

    def set_pieces(self, df, scr, w, b):

        for p in df.loc[:, "White-position"]:

            img = df.loc[df["White-position"] == p, "White-Image"].squeeze()

            test_piece = pieces.Piece()

            piece_position = test_piece.placement(self.tile_objects[p], img, scr)

            name = df.loc[df["White-position"] == p, "Piece"].squeeze()

            w["{}".format(name)] = piece_position  # a dictionary of white_pieces
        print(w)
        for p in df.loc[:, "Black-position"]:

            img = df.loc[df["Black-position"] == p, "Black-Image"].squeeze()

            test_piece = pieces.Piece()

            piece_position = test_piece.placement(self.tile_objects[p], img, scr)

            name = df.loc[df["Black-position"] == p, "Piece"].squeeze()

              # a dictionary of black_pieces
            if name[:2] == "Pa":
                b["B{}".format(name)] = piece_position
            else:
                b["{}".format(name)] = piece_position

        print(b)
        return w, b

    @staticmethod
    def reset_pieces(df, scr, w, b):
        for ind, var in w.items():
            img = df.loc[df["Piece"] == ind, "White-Image"].squeeze()

            pi = pieces.Piece()

            pi.placement(pos=var[:2], image=img, s=scr)

        for ind, va in b.items():
            if ind[:2] == "BP":
                data_name = ind[1:]
            else:
                data_name = ind
            img = df.loc[df["Piece"] == data_name, "Black-Image"].squeeze()
            pi = pieces.Piece()
            pi.placement(pos=va[:2], image=img, s=scr)

    @staticmethod
    def draw_board(scr):
        color = 0
        for X in range(0, 640, 80):

            for Y in range(0, 640, 80):
                if Y == 0:

                    color += 1

                square = Square(X, Y)

                c = square.colour_decision(value=color)

                square.instantiate(c, scr)

                b = Board()

                b.add_tile(x=X, y=Y, sqr=square)

                color += 1

class DisposalTray:
    def __init__(self):
        x = self.x
        y = self.y
        w = self.h
        h = self.h


