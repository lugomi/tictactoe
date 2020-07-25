field = [['-' for x in range(3)] for y in range(3)]



class PlayingField:
    global field

    
    def __init__(self):
        self.field = field

    @classmethod
    def field_status(cls):
        print(' '.join(field[0]))
        print(' '.join(field[1]))
        print(' '.join(field[2]))


def replace_func(x, y, shape):
    field[x][y] = shape
    return field


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