import numpy as np
from enum import Enum

class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1

class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

    def hit(self):
        self.hits += 1

    def is_sunk(self):
        return self.hits >= self.size

class Board:
    def __init__(self):
        self.ship_matrix = np.empty((10, 10), dtype=object)
        self.is_hit_matrix = np.zeros((10, 10), dtype=int)
        self.shots_fired = 0
        self.ship = []

    def is_position_legal(self, size: int, coordinate: tuple, direction: Direction):

        #check if ship is out of bounds
        if coordinate[0] < 0 or coordinate[0] >= 10 or coordinate[1] < 0 or coordinate[1] >= 10:
            return False
        if direction == Direction.HORIZONTAL and coordinate[0] + (size-1) >= 10:
            return False
        if direction == Direction.VERTICAL and coordinate[1] + (size-1) >= 10:
            return False

       #check if ship already exists
        if direction == direction.HORIZONTAL:
            for i in range(size):
                print(self.ship_matrix[coordinate[1], coordinate[0] + i])
                if self.ship_matrix[coordinate[1], coordinate[0] + i] is not None:
                    return False

        if direction == direction.VERTICAL:
            for i in range(size):
                print(self.ship_matrix[coordinate[1], coordinate[0] + i])
                if self.ship_matrix[coordinate[1] + i, coordinate[0]] is not None:
                    return False
        return True

    def place_ship(self, size: int, coordinate: tuple, direction: Direction):
        if self.is_position_legal(size, coordinate, direction):
            ship = Ship(size)
            self.ship.append(ship)
            for i in range(size):
                if direction == Direction.HORIZONTAL:
                    self.ship_matrix[coordinate[1], coordinate[0] + i] = ship
                else:
                    self.ship_matrix[coordinate[1] + i, coordinate[0]] = ship
            return True
        else:
            return False

    def shoot(self, coordinate):
        if self.is_hit_matrix[coordinate[1], coordinate[0]] == 1:
            return False

        self.is_hit_matrix[coordinate[1], coordinate[0]] = 1

        ship = self.ship_matrix[coordinate[1], coordinate[0]]
        if ship is not None:
            ship.hit()


    def draw_board(self):

        board = []

        for y in range(10):
            for x in range(10):
                value = self.is_hit_matrix[y, x]
                if value == 0:
                    board.append("˜")
                else:
                    current_ship = self.ship_matrix[y, x]
                    if current_ship is not None:
                        if current_ship.is_sunk():
                            board.append("Ø")
                        else:
                            board.append("S")
                    else:
                        board.append("O")

        for x in range(10):
            print("\t".join(element for element in board[x*10:x*10 + 10]))


        #print(board[90:])

        #for row in self.is_hit_matrix:
        #    print("\t".join(str(location) for location in row))



    def has_won(self):
        pass