from battleship import *
import random

def input_coordinate(text):
    while True:
        result = input(text).split(",")
        if len(result) == 2:
            try:
                result = [int(result[0]), int(result[1])]
                if 0 <= result[0] <= 9 and 0 <= result[1] <= 9:
                    return result
            except:
                pass



if __name__ == "__main__":
    board = Board()

    #ship_size = [5, 4, 3, 3, 2]
    ship_size = [5]
    ship_index = 0
    while ship_index < len(ship_size):
        direction = random.choice([Direction.VERTICAL, Direction.HORIZONTAL])
        size = ship_size[ship_index]
        coordinate = (random.randint(0, 9), random.randint(0, 9))
        if board.place_ship(size, coordinate, direction):
            ship_index += 1
            print(f"placed: {coordinate[0]}, {coordinate[1]}")

    while not board.has_won():
        board.draw_board()
        coordinate = input_coordinate("Enter coordinate between 0 and 9 <1,5>: ")
        if not board.shoot(coordinate):
            print("already hit!")

    print("\n\nGame won!")
    print(f"Shots fired: {board.shots_fired}")
