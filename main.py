import pygame
from sys import exit
import pandas as pd
import Game_Mechanics
from game_board import Square, Board
pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
color = 0
Game_Start = False
White_Turn = True
white_pieces = {}
black_pieces = {}
selecting = False
df = pd.read_csv("Chess_piece_info.csv")
position_options = []
moving_name = ""
def main_turn_loop(piece_list, sel, current_turn, poz_places, name):
    w_turn = Game_Mechanics.Turn()

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not sel:

        for key, value in piece_list.items():

            if value.collidepoint(mouse):

                poz_places, name = w_turn.instantiate_options(piece_list, value, screen)

                sel = True

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and sel:

        for v in poz_places:

            if v.collidepoint(mouse):

                piece_list = w_turn.make_final_move(name, w_turn, v, piece_list, screen)

                board.draw_board(screen)

                board.reset_pieces(df=df, scr=screen, w=white_pieces, b=black_pieces)

                current_turn = not current_turn

                name = ""
                poz_places = []
                sel = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and sel:  # Rclick to undo piece sel

        board.draw_board(screen)

        board.reset_pieces(df=df, scr=screen, w=white_pieces, b=black_pieces)

        name = ""
        poz_places = []
        sel = False

    return piece_list, sel, current_turn, poz_places, name


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

                square.instantiate(colour=c, scr=screen)
                board.add_tile(x=X, y=Y, sqr=square)
                color += 1

        white_pieces, black_pieces = board.set_pieces(df=df, scr=screen, w=white_pieces, b=black_pieces)

        Game_Start = True
    else:

        for event in pygame.event.get():

            if White_Turn:

                white_pieces, selecting, White_Turn, position_options, moving_name = main_turn_loop(white_pieces, selecting, White_Turn, position_options, moving_name)

            else:
                black_pieces, selecting, White_Turn, position_options, moving_name = main_turn_loop(black_pieces, selecting, White_Turn, position_options, moving_name)
                print(position_options, selecting)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(60)
