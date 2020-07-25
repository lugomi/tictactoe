class PlayingField:
    def __init__(self):
        self.field = field

    @classmethod
    def field_status(cls):
        print(' '.join(field[0]))
        print(' '.join(field[1]))
        print(' '.join(field[2]))

field = [['-' for x in range(3)] for y in range(3)]

grids = {
    1: field[0][0], 2: field[0][1], 3: field[0][2],
    4: field[1][0], 5: field[1][1], 6: field[1][2],
    7: field[2][0], 8: field[2][1], 9: field[2][2]
}

def grid_to_square(grids, shape):
    x = int(input('Enter number here: '))
    choice = grids[x]
    choice = shape
    print(field)

grid_to_square(grids[1], 'x')

game_board = PlayingField

# game_board.field_status()

class Player:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def info(self):
        print(self.name)
        print(self.shape)

    def your_turn(self):
        pass



# miggy = Player("Miguel", "OO")

# miggy.info()