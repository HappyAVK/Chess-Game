import pygame
from pieces import Piece



class Turn:
    def start_move(self, piece, mousepos, selecting_):
        piece_options = []
        piece_object = 1
        if not selecting_:

            if piece.collidepoint(mousepos):

                selected_piece = Piece()
                x = selected_piece.get_move_and_attack_tiles(piece.topleft)[0]

                piece_object = piece
                for pos in x:

                    piece_options.append(pos)







            return piece_options, piece_object
        else:
            pass



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