from battleship import *

board = Board()
board.place_ship(4, (1,1), Direction.VERTICAL)


board.shoot((1,1))
board.shoot((1,2))
board.shoot((1,3))




board.draw_board()