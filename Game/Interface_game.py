from Board.Board_Creation import Board, Boat
import copy


class InterfaceUI:
    @staticmethod
    def get_orientation():
        good = True
        while good:
            orientation = input("orientation (h/v) =")
            if orientation == "h" or orientation == "v":
                good = False
            else:
                print("Invalid orientation!")
        return orientation

    @staticmethod
    def print_1stmsg(x):
        print("Player {} place boats:".format(x))

    @staticmethod
    def ui_attack_game(player1, player2):
        while 1:
            InterfaceUI.print_1()
            x, y = InterfaceUI.get_attack_coords()
            InterfaceGame.attack_player(player2, x, y)
            InterfaceUI.print_attack_game(player1, player2)
            if InterfaceGame.check_winner(player2):
                InterfaceUI.win_msg(1)
                break

            InterfaceUI.print_2()
            x, y = InterfaceUI.get_attack_coords()
            InterfaceGame.attack_player(player1, x, y)
            InterfaceUI.print_attack_game(player2, player1)
            if InterfaceGame.check_winner(player1):
                InterfaceUI.win_msg(2)
                break

    @staticmethod
    def win_msg(x):
        print("Player {} wins!".format(x))

    @staticmethod
    def print_attack_game(player1, player2):
        print("Player board")
        InterfaceUI.display_player_board(player1)
        print("\n", "Enemy board", )
        InterfaceUI.display_enemy_board(player2)

    @staticmethod
    def print_1():
        print("Player 1 turn", "\n")

    @staticmethod
    def print_2():
        print("Player 2 turn", "\n")

    @staticmethod
    def two_player_game():
        pass

    @staticmethod
    def get_attack_coords():
        good = True
        while good:
            x_coord = int(input("x coord =")) - 1
            if 0 <= x_coord < 10:
                good = False
            else:
                print("Invalid x coord!")

        good = True
        while good:
            y_coord = int(input("y coord =")) - 1
            if 0 <= y_coord < 10:
                good = False
            else:
                print("Invalid y coord!")
        return x_coord, y_coord

    @staticmethod
    def display_enemy_board(player):
        visual_board = copy.deepcopy(player.board)
        boats = [5, 4, 3, 2]
        for i in range(0, 10):
            for j in range(0, 10):
                if visual_board[i][j] == 0:
                    visual_board[i][j] = "-"
                elif visual_board[i][j] == "hit":
                    visual_board[i][j] = "x"
                elif visual_board[i][j] == "miss":
                    visual_board[i][j] = "0"
                elif visual_board[i][j] in boats:
                    visual_board[i][j] = "-"

        print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                         for row in visual_board])
              )

    @staticmethod
    def display_player_board(player):
        visual_board = copy.deepcopy(player.board)
        boats = [5, 4, 3, 2]
        for i in range(0, 10):
            for j in range(0, 10):
                if visual_board[i][j] == 0:
                    visual_board[i][j] = "-"
                elif visual_board[i][j] == "hit":
                    visual_board[i][j] = "x"
                elif visual_board[i][j] == "miss":
                    visual_board[i][j] = "0"
                elif visual_board[i][j] in boats:
                    visual_board[i][j] = "b"

        print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                         for row in visual_board])
              )


class InterfaceGame:
    @staticmethod
    def check_winner(player):
        win = True
        for i in range(0, 10):
            for j in range(0, 10):
                if player.board[i][j] != "miss" and player.board[i][j] != "hit":
                    if 0 < player.board[i][j] < 5:
                        win = False
        return win

    @staticmethod
    def create_game_2_player():
        player1 = Board()
        player2 = Board()
        player1.create_empty_board()
        player2.create_empty_board()
        InterfaceUI.print_1stmsg(1)
        InterfaceGame.place_player_boats(player1)

        InterfaceUI.print_1stmsg(2)
        InterfaceGame.place_player_boats(player2)
        print("\n", "Starting the game:")
        InterfaceUI.ui_attack_game(player1, player2)

    @staticmethod
    def place_player_boats(player):
        aboats = [5, 4, 3, 3, 2]
        for size in aboats:
            placed_boat = True
            x, y = InterfaceUI.get_attack_coords()
            h = InterfaceUI.get_orientation()
            boat = InterfaceGame.place_boat(size, x, y, h)
            while placed_boat:
                if player.outside_board(boat.coordinate_start, boat.coordinate_end):
                    print("Outside the map!")
                    boat = InterfaceGame.place_boat(size, x, y, h)
                elif player.check_for_boat(boat):
                    print("Boat There")
                    boat = InterfaceGame.place_boat(size, x, y, h)
                else:
                    player.add_boat(boat)
                    placed_boat = False
                    InterfaceUI.display_player_board(player)

    @staticmethod
    def attack_player(player, x, y):
        if player.hit_or_miss(x, y):
            player.board[y][x] = "hit"
            print("hit!")
        else:
            player.board[y][x] = "miss"
            print("miss!")

    @staticmethod
    def place_boat(size, x, y, orientation):
        if orientation == "h":
            return Boat(size, orientation, [x, y], [x + size, y])
        else:
            return Boat(size, orientation, [x, y], [x, y + size])

