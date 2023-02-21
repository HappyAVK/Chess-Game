import pygame
from pieces import DynamicPiece
import pandas as pd
from pieces import Piece
from game_board import Board
p_places = []
df = pd.read_csv("Chess_piece_info.csv")


class Turn:
    @staticmethod
    def start_move(piece, piece_list, enemy_list):
        piece_check = []
        block_check = []
        name = list(piece_list.keys())[list(piece_list.values()).index(piece)][:-2]

        selected_piece = DynamicPiece()

        m, a = selected_piece.identify(name)

        m_, _a = selected_piece.get_move_and_attack_tiles(piece.topleft, m, a, enemy_list)
        m_and_a = m_ + _a

        for k, s in piece_list.items():
            piece_check.append(list(s.topleft))  # first pass to remove blocked spaces
        tu = Turn()

        block_check = piece_check + _a

        more_blocked_spaces = tu.check_blocked_piece(piece_type=name, original_piece_pos=piece.topleft,
                                                     blocked_spaces=block_check)  # second pass to remove blocked spaces

        piece_check = piece_check + more_blocked_spaces

        m_and_a = [p for p in m_and_a if p not in piece_check]  # Appending move list to blocked spaces

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
    def instantiate_options(pieces, chosen_piece, scr, opponents):
        p_places.clear()
        image_ = pygame.image.load("graphics/Pawn_Black.png").convert_alpha()

        t = Turn()
        selections_, selected_piece = t.start_move(piece=chosen_piece, piece_list=pieces, enemy_list=opponents)

        p_name = list(pieces.keys())[list(pieces.values()).index(selected_piece)]

        for index, i in enumerate(selections_):

            pos_option_rect = image_.get_rect(topleft=i)

            scr.blit(image_, pos_option_rect)

            p_places.append(pos_option_rect)

        return p_places, p_name

    @staticmethod
    def make_final_move(_name, turn_type, p, old_list, scr):
        if _name[:2] == "BP":
            data_name = _name[1:]
        else:
            data_name = _name

        replace_img = df.loc[df["Piece"] == data_name, "White-Image"].squeeze()

        new_board = Board()

        new_board.draw_board(scr)

        new_pos = turn_type.get_new_place(p, replace_img, scr)

        old_list[_name] = new_pos

        return old_list

    def check_blocked_piece(self, piece_type, original_piece_pos, blocked_spaces):
        unreachable_spaces = []
        blocked_spaces = [i for i in blocked_spaces if not isinstance(i, int)]
        match piece_type:
            case "Castle":

                for x in blocked_spaces:
                    if x[1] == original_piece_pos[1]:  # x value
                        if x[0] > original_piece_pos[0]:
                            for z in range(x[0]+80, 741, 80):

                                unreachable_spaces.append([z, original_piece_pos[1]])

                        elif x[0] < original_piece_pos[0]:
                            for z in range(0, x[0], 80):  # change to 100 if broken

                                unreachable_spaces.append([z, original_piece_pos[1]])
                    for y in blocked_spaces:

                        if y[0] == original_piece_pos[0]:  # y value
                            if y[1] > original_piece_pos[1]:
                                for z in range(y[1]+80, 721, 80):
                                    unreachable_spaces.append([original_piece_pos[0], z])
                            elif y[1] < original_piece_pos[1]:
                                for z in range(0, y[1], 80):
                                    unreachable_spaces.append([original_piece_pos[0], z])

                return unreachable_spaces

            case "Rook":

                for x in blocked_spaces:
                    if x[0] > original_piece_pos[0] and x[1] > original_piece_pos[1]:
                        for z in range(x[0] + 80, 741, 80):
                            for w in range(x[1]+80, 721, 80):
                                unreachable_spaces.append([z, w])
                    if x[0] < original_piece_pos[0] and x[1] < original_piece_pos[1]:
                        for z in range (100, x[0], 80):
                            for w in range(0, x[1], 80):
                                unreachable_spaces.append([z, w])
                    if x[0] > original_piece_pos[0] and x[1] < original_piece_pos[1]:
                        for z in range(x[0] + 80, 741, 80):
                            for w in range(0, x[1], 80):
                                unreachable_spaces.append([z, w])
                    if x[0] < original_piece_pos[0] and x[1] > original_piece_pos[1]:
                        for z in range(100, x[0], 80):
                            for w in range(x[1]+80, 721, 80):
                                unreachable_spaces.append([z, w])
                return unreachable_spaces
            case "Queen":
                for x in blocked_spaces:
                    if x[0] > original_piece_pos[0] and x[1] > original_piece_pos[1]:
                        for z in range(x[0] + 80, 741, 80):
                            for w in range(x[1] + 80, 721, 80):
                                unreachable_spaces.append([z, w])
                    if x[0] < original_piece_pos[0] and x[1] < original_piece_pos[1]:
                        for z in range(100, x[0], 80):
                            for w in range(0, x[1], 80):
                                unreachable_spaces.append([z, w])
                    if x[0] > original_piece_pos[0] and x[1] < original_piece_pos[1]:
                        for z in range(x[0] + 80, 741, 80):
                            for w in range(0, x[1], 80):
                                unreachable_spaces.append([z, w])
                    if x[0] < original_piece_pos[0] and x[1] > original_piece_pos[1]:
                        for z in range(100, x[0], 80):
                            for w in range(x[1] + 80, 721, 80):
                                unreachable_spaces.append([z, w])
                for x in blocked_spaces:
                    if x[1] == original_piece_pos[1]:  # x value
                        if x[0] > original_piece_pos[0]:
                            for z in range(x[0] + 80, 741, 80):
                                unreachable_spaces.append([z, original_piece_pos[1]])

                        elif x[0] < original_piece_pos[0]:
                            for z in range(0, x[0], 80):  # change to 100 if broken

                                unreachable_spaces.append([z, original_piece_pos[1]])
                    for y in blocked_spaces:

                        if y[0] == original_piece_pos[0]:  # y value
                            if y[1] > original_piece_pos[1]:
                                for z in range(y[1] + 80, 721, 80):
                                    unreachable_spaces.append([original_piece_pos[0], z])
                            elif y[1] < original_piece_pos[1]:
                                for z in range(0, y[1], 80):
                                    unreachable_spaces.append([original_piece_pos[0], z])

                return unreachable_spaces

        return [-1000, -1000]


# if __name__ == "__main__":
        # pygame.init()
    # screen = pygame.display.set_mode((1000, 1000))
    # pygame.display.set_caption("Chess")
    # clock = pygame.time.Clock()
    # playa = pygame.image.load('graphics/Salt.png').convert_alpha()
    # player_rect = playa.get_rect(mid=(500, 600))
    # while True:
    #     screen.blit(playa, player_rect)
    #     print(player_rect.right, player_rect.top)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             exit()
