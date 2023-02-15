import pygame


class Piece:
    def __init__(self):
        self.movement = [0, -80, 0, -160]  # x and y var for pygame
        self.attack = [80, -80, -80, -80]

        # self.alignment = alignment May a var for piece placement

    def get_move_and_attack_tiles(self, pos):
        # there is potentially a better way to do this, but this method locates adjacent tiles to either move of attack
        #  by converting the data to a list of a list, these values should correspond with the board dictionary
        move_list = []
        move_options = []
        attack_list = []
        attack_options = []
        for i, m in enumerate(self.movement):
            if (i % 2) == 0:

                i = pos[0] + m

                move_list.append(i)
            else:

                n = pos[1] + m

                move_list.append(n)
            if len(move_list) >= 2:
                move_options.append(move_list)
                move_list = []

        for i, m in enumerate(self.attack):
            if (i % 2) == 0:
                i = pos[0] + m

                attack_list.append(i)
            else:

                n = pos[1] + m

                attack_list.append(n)
            if len(attack_list) >= 2:

                attack_options.append(attack_list)
                attack_list = []

                # After attack tiles are selected, we need to confirm if there is a piece there to attack (for pawns),
                # for other pieces, if there is a piece to attack the position it
                # needs to be removed from the regular move list to avoid overlap
        move_options = [r for r in move_options if r not in attack_options]
        return move_options, attack_options

    def placement(self, pos, image, s):
        l_img = pygame.image.load(image).convert_alpha()
        piece_rectangle = l_img.get_rect(topleft=pos)
        s.blit(l_img, piece_rectangle)
        return piece_rectangle
        # Somewhere we should store data for each piece's starting positions

    def move_piece(self):
        pass  # for this we need to make the code more fitting for pygame, and understand a way we can move the chess
# pieces through pygame



class DynamicPiece(Piece):
    def identify(self, ident):
        move = []
        atk = []

        match ident:
            case "Pawn":

                move = [0, -80, 0, -160]  # x and y var for pygame
                atk = [80, -80, -80, -80]

            case "Rook":
                for x_ in range(-640, 0, 80):
                    move.append(x_)
                    move.append(x_)
                    move.append(-x_)
                    move.append(-x_)
                    move.append(x_)
                    move.append(-x_)
                    move.append(-x_)
                    move.append(x_)
                atk = move
            case "Knight":
                move = [160, 80, 160, -80, -160, 80, -160, -80, 80, 160, 80, -160, -80, 160, -80, -160]
                atk = move
            case "Castle":

                for x_ in range(-640, 0, 80):
                    move.append(0)
                    move.append(x_)
                    move.append(x_)
                    move.append(0)
                    move.append(0)
                    move.append(-x_)
                    move.append(-x_)
                    move.append(0)



                atk = move
            case "King":
                move = [80, 80, 80, 0, 0, 80, -80, -80, -80, 0, 0, -80]
                atk = move
            case "Queen":
                for x_ in range(-640, 0, 80):
                    move.append(0)
                    move.append(x_)
                    move.append(x_)
                    move.append(0)
                    move.append(0)
                    move.append(-x_)
                    move.append(-x_)
                    move.append(0)
                    move.append(x_)
                    move.append(x_)
                    move.append(-x_)
                    move.append(-x_)
                    move.append(x_)
                    move.append(-x_)
                    move.append(-x_)
                    move.append(x_)
                atk = move

            case "BPawn":
                move = [80, 80, 0, 160, 0, 240]
                atk = [80, 80, 80, 80]
        return move, atk

    def get_move_and_attack_tiles(self, pos, move_data, attack_data):
        # there is potentially a better way to do this, but this method locates adjacent tiles to either move of attack
        #  by converting the data to a list of a list, these values should correspond with the board dictionary
        move_list = []
        move_options = []
        attack_list = []
        attack_options = []

        for i, m in enumerate(move_data):
            if (i % 2) == 0:

                i = pos[0] + m

                move_list.append(i)
            else:
                n = pos[1] + m

                move_list.append(n)
            if len(move_list) >= 2:
                for check in move_list:
                    if check > 660 or check < 80:
                        move_list = []
                    else:
                        continue


                move_options.append(move_list)
                move_list = []

        for i, m in enumerate(attack_data):
            if (i % 2) == 0:
                i = pos[0] + m

                attack_list.append(i)
            else:
                n = pos[1] + m

                attack_list.append(n)
            if len(attack_list) >= 2:
                for check in attack_list:
                    if check > 660 or check < 80:
                        attack_list = []
                    else:
                        continue

                attack_options.append(attack_list)
                attack_list = []

                # After attack tiles are selected, we need to confirm if there is a piece there to attack (for pawns),
                # for other pieces, if there is a piece to attack the position it
                # needs to be removed from the regular move list to avoid overlap
        attack_options = [v for v in attack_options if v != []]
        move_options = [r for r in move_options if r != [] and r not in attack_options]

        return move_options, attack_options


if __name__ == "__main__":
    # p = Piece()
    # x, y = p.get_move_and_attack_tiles(pos=[4, 2])
    # print(x, y)
    tes = DynamicPiece()
    t, x = tes.identify(ident="Castle")
    print(tes.get_move_and_attack_tiles([4, 2], t, x))
    #print(t)
