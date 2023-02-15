import pygame
from pieces import Piece, DynamicPiece



class Turn:
    def start_move(self, piece, piece_list):

        name = list(piece_list.keys())[list(piece_list.values()).index(piece)][:-2]

        selected_piece = DynamicPiece()

        m, a = selected_piece.identify(name)
        print(m, a)
        m_, _a = selected_piece.get_move_and_attack_tiles(piece.topleft, m, a)
        m_and_a = m_ + _a

        piece_object = piece

        return m_and_a, piece_object




    def get_new_place(self, mouse, obj, _img, s):



        if obj.collidepoint(mouse):
            r = obj.topleft

            t = tuple(r)

            rect_pos = pygame.Rect(t, (80, 80))
            moved_piece = Piece()
            moved_piece.placement(t, _img, s)
            return rect_pos


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