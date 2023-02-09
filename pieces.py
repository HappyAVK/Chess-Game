import pygame


class Piece:
    def __init__(self, image):
        self.movement = [0, -1, 0, -2]  # x and y var for pygame
        self.attack = [1, -1, -1, -1]
        self.image = image
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

    def placement(self, pos):
        piece_rectangle = self.image.get_rect(topleft=pos)
        return piece_rectangle
        # Somewhere we should store data for each piece's starting positions

    def move_piece(self):
        pass  # for this we need to make the code more fitting for pygame, and understand a way we can move the chess
# pieces through pygame


if __name__ == "__main__":
    p = Piece(image="graphics/SaltzPog.png")
    x, y = p.get_move_and_attack_tiles(pos=[4, 2])
    print(x, y)
