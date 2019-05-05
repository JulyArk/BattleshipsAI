class Boat:
    """
    Boat.
    """

    def __init__(self, size, orientation, coordinate_start, coordinate_end):
        self.type = size
        self.orientation = orientation
        self.coordinate_start = coordinate_start
        self.coordinate_end = coordinate_end

    def return_type(self):
        return self.type


class BoatPart:
    def __init__(self):
        self.part = int  # I want a visual representation for this
        self.x_location = int  # coordinate x
        self.y_location = int  # coordinate y

    def use_part(self):
        pass


class Board:
    """
    The player board
    """
    def __init__(self):
        self.board = []
        self.object = []

    def add_boat(self, boat):
        """
        adds a boat on the map
        :param boat: boat class
        :return: None
        """
        if boat.orientation == "v":  # [2,1] [2,4] o_in_lst, nr_o_list

            for length in range(boat.coordinate_start[1], boat.coordinate_end[1]):
                self.board[length][boat.coordinate_end[0]] = boat.return_type()
        elif boat.orientation == "h":  # [1, 5], [4, 5]
            for length in range(boat.coordinate_start[0], boat.coordinate_end[0]):
                self.board[boat.coordinate_end[1]][length] = boat.return_type()

    def create_empty_board(self):
        """
        initializes the board
        :return:
        """
        for i in range(0, 10):
            self.board.append([])
        for i in range(0, 10):
            for j in range(0, 10):
                self.board[i].append(0)

    def print_board(self):
        """
        debugging tool, prints the boat in the console
        :return:
        """
        print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                         for row in self.board])
              )

    def check_for_boat(self, boat):  # [o_in_lst, nr_o_list]
        """
         Checks if there is a boat at the coordinates you want to place a boat
        :param boat: boat class
        :return: True if there is a boat / False if not
        """
        boat_there = False  # ----------0 1   0 1

        if boat.orientation == "v":  # [2,1] [2,4]
            for length in range(boat.coordinate_start[1], boat.coordinate_end[1]):  # ( 1=y , 4=x)
                if self.board[length][boat.coordinate_end[0]] != 0:  # [  ,  ]
                    boat_there = True
        elif boat.orientation == "h":  # [1, 5], [4, 5]
            for length in range(boat.coordinate_start[0], boat.coordinate_end[0]):
                if self.board[boat.coordinate_end[1]][length] != 0:
                    boat_there = True

        return boat_there

    def hit_or_miss(self, coordinate_x, coordinate_y):
        """
        Checks if there is a boat at the coordinates
        "I guess they never miss huh"
        :return: True - hit a boat / False - hit water / False - hit a miss
        """
        print(coordinate_x, coordinate_y)
        if self.board[coordinate_y][coordinate_x] == 0:
            return False
        elif self.board[coordinate_y][coordinate_x] == "miss":
            return False
        else:
            return True

    @staticmethod
    def outside_board(x, y):
        """
        Checks if the boat you want to place is outside the board
        :param x: list with starting coordinates
        :param y: list with ending coordinates
        :return: True if outside / False if inside
        """
        if (x[0] > 10 or x[0] < 0) or (x[1] > 10 or x[1] < 0) or (y[0] > 10 or y[0] < 0) or (y[1] > 10 or y[1] < 0):

            return True
        else:

            return False


if __name__ == '__main__':
    Game = Board()
    Game.create_empty_board()
    Game.board[3][1] = 8
    Game.print_board()
