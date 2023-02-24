import pygame
from pieces import DynamicPiece
import pandas as pd
from pieces import Piece
from game_board import Board
p_places = []
df = pd.read_csv("Chess_piece_info.csv")


class Turn:
    @staticmethod
    def start_move(piece, piece_list, enemy_list, check_tiles, srcs):
        piece_check = []
        block_check = []
        move_state = False
        name = list(piece_list.keys())[list(piece_list.values()).index(piece)][:-2]

        selected_piece = DynamicPiece()

        m, a = selected_piece.identify(name)

        m_, _a = selected_piece.get_move_and_attack_tiles(piece.topleft, m, a, enemy_list)

        for k, s in piece_list.items():
            piece_check.append(list(s.topleft))  # first pass to remove blocked spaces
        tu = Turn()
        if name == "Pawn" or name == "BPawn":
            move_state = selected_piece.pawn_check(piece, check_tiles)

            # Check if pawn has attacked
        if move_state:
            m_ = m_[:1]

        m_and_a = m_ + _a


        block_check = piece_check + _a
        # line 32 to 37 are to facilitate special pawn conditions

        more_blocked_spaces = tu.check_blocked_piece(piece_type=name, original_piece_pos=piece.topleft,
                                                     blocked_spaces=block_check, movecheck=m_, scrn=srcs, enemy_list=enemy_list)  # second pass to remove blocked spaces

       # print(m_and_a)
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
    def instantiate_options(pieces, chosen_piece, scr, opponents, tiles):
        p_places.clear()
        image_ = pygame.image.load("graphics/Pawn_Black.png").convert_alpha()

        t = Turn()
        selections_, selected_piece = t.start_move(piece=chosen_piece, piece_list=pieces, enemy_list=opponents,
                                                   check_tiles=tiles, srcs=scr)

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

    def check_blocked_piece(self, piece_type, original_piece_pos, blocked_spaces, movecheck, scrn, enemy_list):
        unreachable_spaces = []
        blocked_spaces = [i for i in blocked_spaces if not isinstance(i, int)]
        block_image_ = pygame.image.load("graphics/asmrvegeta.png").convert_alpha()
        match piece_type:
            case "Castle":

                for x in blocked_spaces:
                    if x[1] == original_piece_pos[1]:  # x value
                        if x[0] > original_piece_pos[0]:
                            for z in range(x[0]+80, 740, 80):

                                unreachable_spaces.append([z, original_piece_pos[1]])

                        elif x[0] < original_piece_pos[0]:
                            for z in range(20, x[0]-79, 80):  # change to 100 if broken

                                unreachable_spaces.append([z, original_piece_pos[1]])
                    for y in blocked_spaces:

                        if y[0] == original_piece_pos[0]:  # y value
                            if y[1] > original_piece_pos[1]:
                                for z in range(y[1]+80, 720, 80):
                                    unreachable_spaces.append([original_piece_pos[0], z])
                            elif y[1] < original_piece_pos[1]:
                                for z in range(0, y[1]-79, 80):
                                    unreachable_spaces.append([original_piece_pos[0], z])

                return unreachable_spaces

            case "Rook":

                for x in blocked_spaces:
                    if x[0] > original_piece_pos[0] and x[1] > original_piece_pos[1]:
                        for z in zip(range(x[0]+80, 741, 80), range(x[1]+80, 721, 80)):

                            unreachable_spaces.append(list(z))

                    if x[0] < original_piece_pos[0] and x[1] < original_piece_pos[1]:
                        for z in zip(reversed(range(20, x[0]-79, 80)), reversed(range(0, x[1]-79, 80))):
                            unreachable_spaces.append(list(z))

                    if x[0] > original_piece_pos[0] and x[1] < original_piece_pos[1]:
                        for z in zip(range(x[0]+80, 740, 80), reversed(range(0, x[1]-79, 80))):

                            unreachable_spaces.append(list(z))

                    if x[0] < original_piece_pos[0] and x[1] > original_piece_pos[1]:
                        for z in zip(reversed(range(20, x[0]-79, 80)),range(x[1]+80, 720, 80)):

                            unreachable_spaces.append(list(z))
                    for y in unreachable_spaces:
                        rect = block_image_.get_rect(topleft=y)
                        scrn.blit(block_image_, rect)
                return unreachable_spaces
            case "Queen":
                for x in blocked_spaces:
                    if x[1] == original_piece_pos[1]:  # x value
                        if x[0] > original_piece_pos[0]:
                            for z in range(x[0] + 80, 740, 80):
                                unreachable_spaces.append([z, original_piece_pos[1]])

                        elif x[0] < original_piece_pos[0]:
                            for z in range(20, x[0] - 79, 80):  # change to 100 if broken

                                unreachable_spaces.append([z, original_piece_pos[1]])
                    for y in blocked_spaces:

                        if y[0] == original_piece_pos[0]:  # y value
                            if y[1] > original_piece_pos[1]:
                                for z in range(y[1] + 80, 720, 80):
                                    unreachable_spaces.append([original_piece_pos[0], z])
                            elif y[1] < original_piece_pos[1]:
                                for z in range(0, y[1] - 79, 80):
                                    unreachable_spaces.append([original_piece_pos[0], z])
                    for x in blocked_spaces:
                        if x[0] > original_piece_pos[0] and x[1] > original_piece_pos[1]:
                            for z in zip(range(x[0] + 80, 741, 80), range(x[1] + 80, 721, 80)):
                                unreachable_spaces.append(list(z))

                        if x[0] < original_piece_pos[0] and x[1] < original_piece_pos[1]:
                            for z in zip(reversed(range(20, x[0] - 79, 80)), reversed(range(0, x[1] - 79, 80))):
                                unreachable_spaces.append(list(z))

                        if x[0] > original_piece_pos[0] and x[1] < original_piece_pos[1]:
                            for z in zip(range(x[0] + 80, 740, 80), reversed(range(0, x[1] - 79, 80))):
                                unreachable_spaces.append(list(z))

                        if x[0] < original_piece_pos[0] and x[1] > original_piece_pos[1]:
                            for z in zip(reversed(range(20, x[0] - 79, 80)), range(x[1] + 80, 720, 80)):
                                unreachable_spaces.append(list(z))


                    return unreachable_spaces
            case "Pawn":
                e_list = []
                for i, v in enemy_list.items():
                    e_list.append(list(v.topleft))

                pawn_range = [y for y in blocked_spaces if y in movecheck] + [e for e in e_list if e in movecheck]

                for n in pawn_range:
                    if n[1] < original_piece_pos[1] and n[1] > original_piece_pos[1]-81:
                        unreachable_spaces = movecheck
                    else:
                        unreachable_spaces = movecheck[1:2]


                return unreachable_spaces

            case "BPawn":
                e_list = []
                for i, v in enemy_list.items():
                    e_list.append(list(v.topleft))

                pawn_range = [y for y in blocked_spaces if y in movecheck] + [e for e in e_list if e in movecheck]

                for n in pawn_range:
                    if n[1] > original_piece_pos[1] and n[1] < original_piece_pos[1] + 81:
                        unreachable_spaces = movecheck
                    else:
                        unreachable_spaces = movecheck[1:2]

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
