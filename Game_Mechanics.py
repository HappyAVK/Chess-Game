import pygame
from pieces import DynamicPiece
import pandas as pd
from pieces import Piece
from game_board import Board
p_places = []
df = pd.read_csv("Chess_piece_info.csv")


class Turn:
    @staticmethod
    def start_move(piece, piece_list):

        name = list(piece_list.keys())[list(piece_list.values()).index(piece)][:-2]

        selected_piece = DynamicPiece()

        m, a = selected_piece.identify(name)

        m_, _a = selected_piece.get_move_and_attack_tiles(piece.topleft, m, a)
        m_and_a = m_ + _a
        piece_check = []
        for k, s in piece_list.items():
            piece_check.append(list(s.topleft))

        m_and_a = [p for p in m_and_a if p not in piece_check]
        piece_object = piece

        return m_and_a, piece_object

    @staticmethod
    def get_new_place(obj, _img, s):

        r = obj.topleft

        t = tuple(r)

        rect_pos = pygame.Rect(t, (80, 80))

        moved_piece = Piece()

        moved_piece.placement(t, _img, s)

        return rect_pos

    @staticmethod
    def instantiate_options(pieces, chosen_piece, scr):
        p_places.clear()
        image_ = pygame.image.load("graphics/Pawn_Black.png").convert_alpha()

        t = Turn()
        selections_, selected_piece = t.start_move(piece=chosen_piece, piece_list=pieces)

        p_name = list(pieces.keys())[list(pieces.values()).index(selected_piece)]

        for index, i in enumerate(selections_):

            pos_option_rect = image_.get_rect(topleft=i)

            scr.blit(image_, pos_option_rect)

            p_places.append(pos_option_rect)
        print(p_places)
        return p_places, p_name

    @staticmethod
    def make_final_move(_name, turn_type, p, old_list, scr):

        replace_img = df.loc[df["Piece"] == _name, "White-Image"].squeeze()

        new_board = Board()

        new_board.draw_board(scr)

        new_pos = turn_type.get_new_place(p, replace_img, scr)

        old_list[_name] = new_pos

        return old_list


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()
    playa = pygame.image.load('graphics/SaltzPog.png').convert_alpha()
    player_rect = playa.get_rect(midbottom=(500, 600))
    while True:
        screen.blit(playa, player_rect)
        print(player_rect.right, player_rect.top)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
