from Board.Board_Creation import Board, Boat
import random


class BoatFavor:
    def __init__(self, boat, score):
        self.boat = boat
        self.score = score


class Padoru:
    @staticmethod
    def random_padoru_ai_placing_boats():
        pass

    @staticmethod
    def adjust_favor(board, boat):
        """
        Adjust the probability map according to the rules after placing a boat
        :param board: probability map
        :param boat: Boat that was placed (object)
        :return:
        """
        orientation = boat.orientation
        if orientation == "h":
            if not boat.coordinate_start[0] < 0:
                if not board.board[boat.coordinate_start[1]][boat.coordinate_start[0] - 1] == 0:
                    board.board[boat.coordinate_start[1]][boat.coordinate_start[0] - 1] -= 5
            try:
                if not board.board[boat.coordinate_start[1] + 1][boat.coordinate_start[0] - 1] == 0:
                    board.board[boat.coordinate_start[1] + 1][boat.coordinate_start[0] - 1] -= 5
            except IndexError:
                pass
            try:
                if not board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0] - 1] == 0:
                    board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0] - 1] -= 5
            except IndexError:
                pass

            if not boat.coordinate_end[0] > 9:
                if not board.board[boat.coordinate_end[1]][boat.coordinate_end[0]] == 0:
                    board.board[boat.coordinate_end[1]][boat.coordinate_end[0]] -= 5
            try:
                if not board.board[boat.coordinate_end[1] + 1][boat.coordinate_end[0]] == 0:
                    board.board[boat.coordinate_end[1] + 1][boat.coordinate_end[0]] -= 5
            except IndexError:
                pass
            try:
                if not board.board[boat.coordinate_end[1] - 1][boat.coordinate_end[0]] == 0:
                    board.board[boat.coordinate_end[1] - 1][boat.coordinate_end[0]] -= 5
            except IndexError:
                pass

            for i in range(0, boat.type):
                if not boat.coordinate_start[1] - 1 < 0:
                    if not board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0] + i] == 0:
                        board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0] + i] -= 5
                if not boat.coordinate_start[1] + 1 > 9:
                    if not board.board[boat.coordinate_start[1] + 1][boat.coordinate_start[0] + i] == 0:
                        board.board[boat.coordinate_start[1] + 1][boat.coordinate_start[0] + i] -= 5

        elif orientation == "v":
            if not boat.coordinate_start[1] < 0:
                if not board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0]] == 0:
                    board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0]] -= 5
            try:
                if not boat.coordinate_start[1] < 0:
                    if not board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0] + 1] == 0:
                        board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0] + 1] -= 5
            except IndexError:
                pass
            try:
                if not boat.coordinate_start[1] < 0:
                    if not board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0] - 1] == 0:
                        board.board[boat.coordinate_start[1] - 1][boat.coordinate_start[0] - 1] -= 5
            except IndexError:
                pass

            if not boat.coordinate_end[1] > 9:
                if not board.board[boat.coordinate_end[1]][boat.coordinate_end[0]] == 0:
                    board.board[boat.coordinate_end[1]][boat.coordinate_end[0]] -= 5
            try:
                if not boat.coordinate_end[1] > 9:
                    if not board.board[boat.coordinate_end[1]][boat.coordinate_end[0] + 1] == 0:
                        board.board[boat.coordinate_end[1]][boat.coordinate_end[0] + 1] -= 5
            except IndexError:
                pass
            try:
                if not boat.coordinate_end[1] > 9:
                    if not board.board[boat.coordinate_end[1]][boat.coordinate_end[0] - 1] == 0:
                        board.board[boat.coordinate_end[1]][boat.coordinate_end[0] - 1] -= 5
            except IndexError:
                pass

            for i in range(0, boat.type):
                if not boat.coordinate_start[0] - 1 < 0:
                    if not board.board[boat.coordinate_start[1] + i][boat.coordinate_start[0] - 1] == 0:
                        board.board[boat.coordinate_start[1] + i][boat.coordinate_start[0] - 1] -= 5
                if not boat.coordinate_start[0] + 1 > 9:
                    if not board.board[boat.coordinate_start[1] + i][boat.coordinate_start[0] + 1] == 0:
                        board.board[boat.coordinate_start[1] + i][boat.coordinate_start[0] + 1] -= 5

    @staticmethod
    def best_positions(all_positions):
        maximum = 0
        for x in all_positions:
            if x.score > maximum:
                maximum = x.score

        best_positions = []
        for x in all_positions:
            if x.score == maximum:
                best_positions.append(x)
        return best_positions

    @staticmethod
    def placement_calculator(length, board):
        """
        Calculates the best options to place the boat
        :param length: the length of the boat
        :param board: the probability map
        :return: a list of MAX (best places to place the boat)
        """
        available_positions = []
        # horizontal calculator
        for y_axis in range(0, 10):  # y_axis = Y axis
            for x_axis in range(0, 10):  # X axis (due to list of list)
                if 10 - x_axis >= length:
                    suma = 0
                    for k in range(0, length):
                        suma = suma + board[y_axis][x_axis + k]
                        if board[y_axis][x_axis + k] == 0:
                            suma = 0
                            break
                    boat = Boat(length, "h", [x_axis, y_axis], [x_axis + length, y_axis])
                    available_positions.append(BoatFavor(boat, suma))
                else:
                    break
        # vertical calculator
        for y_axis in range(0, 10):  # y_axis = Y axis
            for x_axis in range(0, 10):  # X axis (due to list of list)
                if 10 - y_axis >= length:
                    suma = 0
                    for k in range(0, length):
                        suma = suma + board[y_axis + k][x_axis]
                        if board[y_axis + k][x_axis] == 0:
                            suma = 0
                            break
                    boat = Boat(length, "v", [x_axis, y_axis], [x_axis, y_axis + length])
                    available_positions.append(BoatFavor(boat, suma))
                else:
                    break
        return available_positions

    @staticmethod
    def ai_placing_boats():
        # create AI board
        ai_board = Board()
        ai_board.create_empty_board()
        # create probability map
        probability_map = Board()
        probability_map.create_empty_board()
        # all points are 10 at the start
        for i in range(0, 10):
            for j in range(0, 10):
                probability_map.board[i][j] = 9
        # creating the boat
        boat_length = [5, 4, 3, 3, 2]
        for length in boat_length:
            possible_positions = Padoru.placement_calculator(length, probability_map.board)
            best_position = random.choice(Padoru.best_positions(possible_positions))
            if not ai_board.check_for_boat(best_position.boat):
                ai_board.add_boat(best_position.boat)
                best_position.boat.type = 0

                probability_map.add_boat(best_position.boat)
                best_position.boat.type = length
                Padoru.adjust_favor(probability_map, best_position.boat)

        return ai_board

    @staticmethod
    class Store:
        boat = 0
        Hit = False
        probability_map = []
        hit_probability_map = []
        initial = True
        last_hit = []
        counter = 1
        multiple_boats = False
        alive = 5

    @staticmethod
    def initial_probability_map(board):
        for i in range(0, 10):
            for j in range(0, 10):
                if i == 0 or j == 0 or i == 9 or j == 9:
                    board[i][j] = 6
                elif 2 < i < 7 and 2 < j < 7:
                    board[i][j] = 9
                elif i == 1 or j == 1 or i == 8 or j == 8:
                    board[i][j] = 7
                else:
                    board[i][j] = 8
        return board

    @staticmethod
    def maximum_positions(all_board):
        maxm = -9999
        for i in range(0, 10):
            for j in range(0, 10):
                if all_board[i][j] > maxm:
                    if all_board[i][j] != 0:
                        maxm = all_board[i][j]

        list_of_max = []
        for i in range(0, 10):
            for j in range(0, 10):
                if all_board[i][j] == maxm:
                    list_of_max.append([i, j])
        return list_of_max

    @staticmethod
    def create_hit_map(coord, board):
        hit_map = Board()
        hit_map.create_empty_board()
        # 1 square
        if coord[1] + 1 < 10:
            hit_map.board[coord[0]][coord[1] + 1] = 10
        if coord[1] - 1 >= 0:
            hit_map.board[coord[0]][coord[1] - 1] = 10
        if coord[0] + 1 < 10:
            hit_map.board[coord[0] + 1][coord[1]] = 10
        if coord[0] - 1 >= 0:
            hit_map.board[coord[0] - 1][coord[1]] = 10
        # 2 squares

        for i in range(0, 10):
            for j in range(0, 10):
                if hit_map.board[i][j] == 0:
                    hit_map.board[i][j] = -1

        for i in range(0, 10):
            for j in range(0, 10):
                if board.board[i][j] == "hit" or board.board[i][j] == "miss":
                    hit_map.board[i][j] = 0

        return hit_map.board

    @staticmethod
    def on_hit_probability_adjustment(prob_board, chosen_position):

        if chosen_position[0] == Padoru.Store.last_hit[0]:
            if chosen_position[1] > Padoru.Store.last_hit[1]:
                counter = chosen_position[1] - Padoru.Store.last_hit[1]
                bonus = 10
                for i in range(0, 3 + counter):
                    if chosen_position[1] + i < 10:
                        if prob_board[chosen_position[0]][chosen_position[1] + i] != 0:
                            prob_board[chosen_position[0]][chosen_position[1] + i] += bonus
                        bonus -= 2
                bonus = 10
                for i in range(0, 3):
                    if chosen_position[1] + i >= 0:
                        if prob_board[chosen_position[0]][chosen_position[1] - i] != 0:
                            prob_board[chosen_position[0]][chosen_position[1] - i] += bonus
                        bonus -= 2
            else:
                counter = Padoru.Store.last_hit[1] - chosen_position[1]
                bonus = 10
                for i in range(0, 3 + counter):
                    if chosen_position[1] - i >= 0:
                        if prob_board[chosen_position[0]][chosen_position[1] - i] != 0:
                            prob_board[chosen_position[0]][chosen_position[1] - i] += bonus
                        bonus -= 2
                bonus = 10
                for i in range(0, 3):
                    if chosen_position[1] + i < 10:
                        if prob_board[chosen_position[0]][chosen_position[1] + i] != 0:
                            prob_board[chosen_position[0]][chosen_position[1] + i] += bonus
                        bonus -= 2
            if Padoru.Store.last_hit[0] + 1 < 10:
                prob_board[Padoru.Store.last_hit[0] + 1][Padoru.Store.last_hit[1]] = -1
            if Padoru.Store.last_hit[0] - 1 >= 10:
                prob_board[Padoru.Store.last_hit[0] - 1][Padoru.Store.last_hit[1]] = -1

        elif chosen_position[1] == Padoru.Store.last_hit[1]:
            if chosen_position[0] > Padoru.Store.last_hit[0]:
                counter = chosen_position[0] - Padoru.Store.last_hit[0]
                bonus = 10
                for i in range(0, 3 + counter):
                    if chosen_position[0] + i < 10:
                        if prob_board[chosen_position[0] + i][chosen_position[1]] != 0:
                            prob_board[chosen_position[0] + i][chosen_position[1]] += bonus
                        bonus -= 2
                bonus = 10
                for i in range(0, 3):
                    if chosen_position[0] - i >= 0:
                        if prob_board[chosen_position[0] - i][chosen_position[1]] != 0:
                            prob_board[chosen_position[0] - i][chosen_position[1]] += bonus
                        bonus -= 2
            else:
                counter = Padoru.Store.last_hit[0] - chosen_position[0]
                bonus = 10
                for i in range(0, 3 + counter):
                    if chosen_position[0] - i >= 0:
                        if prob_board[chosen_position[0] - i][chosen_position[1]] != 0:
                            prob_board[chosen_position[0] - i][chosen_position[1]] += bonus
                        bonus -= 2
                bonus = 10
                for i in range(0, 3):
                    if chosen_position[0] + i < 10:
                        if prob_board[chosen_position[0] + i][chosen_position[1]] != 0:
                            prob_board[chosen_position[0] + i][chosen_position[1]] += bonus
                        bonus -= 2
            if Padoru.Store.last_hit[1] - 1 >= 0:
                prob_board[Padoru.Store.last_hit[0]][Padoru.Store.last_hit[1] - 1] = -1
            if Padoru.Store.last_hit[1] + 1 < 10:
                prob_board[Padoru.Store.last_hit[0]][Padoru.Store.last_hit[1] + 1] = -1
        return prob_board

    @staticmethod
    def on_miss_probability_adjustment(prob_board, chosen_position):
        if chosen_position[0] == Padoru.Store.last_hit[0]:
            if chosen_position[1] > Padoru.Store.last_hit[1]:
                counter = chosen_position[1] - Padoru.Store.last_hit[1]
                bonus = -13
                for i in range(0, 3 + counter):
                    if chosen_position[1] + i < 10:
                        if prob_board[chosen_position[0]][chosen_position[1] + i] != 0:
                            prob_board[chosen_position[0]][chosen_position[1] + i] += bonus
                        bonus += 2
                bonus = -13
                for i in range(0, 3):
                    if chosen_position[1] + i >= 0:
                        if prob_board[chosen_position[0]][chosen_position[1] - i] != 0:
                            prob_board[chosen_position[0]][chosen_position[1] - i] += bonus
                        bonus += 2
            else:
                counter = Padoru.Store.last_hit[1] - chosen_position[1]
                bonus = -13
                for i in range(0, 3 + counter):
                    if chosen_position[1] - i >= 0:
                        if prob_board[chosen_position[0]][chosen_position[1] - i] != 0:
                            prob_board[chosen_position[0]][chosen_position[1] - i] += bonus
                        bonus += 2
                bonus = -13
                for i in range(0, 3):
                    if chosen_position[1] + i < 10:
                        if prob_board[chosen_position[0]][chosen_position[1] + i] != 0:
                            prob_board[chosen_position[0]][chosen_position[1] + i] += bonus
                        bonus += 2

        elif chosen_position[1] == Padoru.Store.last_hit[1]:
            if chosen_position[0] > Padoru.Store.last_hit[0]:
                counter = chosen_position[0] - Padoru.Store.last_hit[0]
                bonus = -13
                for i in range(0, 3 + counter):
                    if chosen_position[0] + i < 10:
                        if prob_board[chosen_position[0] + i][chosen_position[1]] != 0:
                            prob_board[chosen_position[0] + i][chosen_position[1]] += bonus
                        bonus += 2
                bonus = -13
                for i in range(0, 3):
                    if chosen_position[0] - i >= 0:
                        if prob_board[chosen_position[0] - i][chosen_position[1]] != 0:
                            prob_board[chosen_position[0] - i][chosen_position[1]] += bonus
                        bonus += 2
            else:
                counter = Padoru.Store.last_hit[0] - chosen_position[0]
                bonus = -13
                for i in range(0, 3 + counter):
                    if chosen_position[0] - i >= 0:
                        if prob_board[chosen_position[0] - i][chosen_position[1]] != 0:
                            prob_board[chosen_position[0] - i][chosen_position[1]] += bonus
                        bonus += 2
                bonus = -13
                for i in range(0, 3):
                    if chosen_position[0] + i < 10:
                        if prob_board[chosen_position[0] + i][chosen_position[1]] != 0:
                            prob_board[chosen_position[0] + i][chosen_position[1]] += bonus
                        bonus += 2
        return prob_board

    @staticmethod
    def check_sunk():
        if Padoru.Store.boat == Padoru.Store.counter:
            Padoru.Store.alive -= 1
            Padoru.Store.counter = 1
            Padoru.Store.boat = 0
            Padoru.Store.Hit = False
            Padoru.Store.probability_map = Padoru.merge_maps(Padoru.Store.hit_probability_map,
                                                             Padoru.Store.probability_map)

        elif Padoru.Store.boat == "hit":
            Padoru.Store.counter = 1
            Padoru.Store.boat = 0
            Padoru.Store.Hit = False
            Padoru.Store.probability_map = Padoru.merge_maps(Padoru.Store.hit_probability_map,
                                                             Padoru.Store.probability_map)

    @staticmethod
    def merge_maps(hit_map, prob_map):
        Padoru.Store.Hit = False

        generator_map = Board()
        generator_map.create_empty_board()
        merged_map = generator_map.board
        for i in range(0, 10):
            for j in range(0, 10):
                merged_map[i][j] = "x"

        for i in range(0, 10):
            for j in range(0, 10):
                if hit_map[i][j] == 0:
                    merged_map[i][j] = 0

        for i in range(0, 10):
            for j in range(0, 10):
                if merged_map[i][j] == 0:
                    if j > 0:
                        if merged_map[i][j - 1] != 0:
                            merged_map[i][j - 1] = 2
                    if j < 9:
                        if merged_map[i][j + 1] != 0:
                            merged_map[i][j + 1] = 2
                    if i < 9:
                        if merged_map[i + 1][j] != 0:
                            merged_map[i + 1][j] = 2
                    if i > 0:
                        if merged_map[i - 1][j] != 0:
                            merged_map[i - 1][j] = 2

        for i in range(0, 10):
            for j in range(0, 10):
                if merged_map[i][j] == "x":
                    merged_map[i][j] = prob_map[i][j]

        return merged_map

    @staticmethod
    def hit_is_miss_adjust(probability_board, coord):
        # 1 square
        if coord[1] + 1 < 10:
            probability_board[coord[0]][coord[1] + 1] -= 4
        if coord[1] - 1 > 0:
            probability_board[coord[0]][coord[1] - 1] -= 4
        if coord[0] + 1 < 10:
            probability_board[coord[0] + 1][coord[1]] -= 4
        if coord[0] - 1 > 0:
            probability_board[coord[0] - 1][coord[1]] -= 4
        # 2 squares
        if coord[1] + 2 < 10:
            probability_board[coord[0]][coord[1] + 2] -= 2
        if coord[1] - 2 > 0:
            probability_board[coord[0]][coord[1] - 2] -= 2
        if coord[0] + 2 < 10:
            probability_board[coord[0] + 2][coord[1]] -= 2
        if coord[0] - 2 > 0:
            probability_board[coord[0] - 2][coord[1]] -= 2
        return probability_board

    @staticmethod
    def win_condition():
        if Padoru.Store.alive < 1:
            return True
        else:
            return False

    @staticmethod
    def ai_attack(board_z):
        x = Board()
        x.create_empty_board()
        probability_board = x.board
        chosen_position = "OVER"
        if Padoru.Store.Hit:
            probability_board = Padoru.Store.hit_probability_map
            best_pos = Padoru.maximum_positions(probability_board)
            try:
                chosen_position = random.choice(best_pos)
                not_right = True
                while not_right:
                    if board_z.board[chosen_position[0]][chosen_position[1]] == "miss" or \
                            board_z.board[chosen_position[0]][chosen_position[1]] == "hit":
                        chosen_position = random.choice(best_pos)
                        Padoru.Store.hit_probability_map[chosen_position[0]][chosen_position[1]] = 0
                        best_pos = Padoru.maximum_positions(probability_board)
                    else:
                        not_right = False
            except IndexError:
                pass
            if chosen_position == "OVER":
                Padoru.Store.alive = 0
                chosen_position = [0, 0]

            if board_z.hit_or_miss(chosen_position[1], chosen_position[0]):
                if Padoru.Store.boat == board_z.board[chosen_position[0]][chosen_position[1]]:
                    Padoru.Store.counter += 1
                else:
                    Padoru.Store.multiple_boats = True
                probability_board = Padoru.on_hit_probability_adjustment(probability_board, chosen_position)
                probability_board[chosen_position[0]][chosen_position[1]] = 0
                board_z.board[chosen_position[0]][chosen_position[1]] = "hit"
                Padoru.Store.hit_probability_map = probability_board
                Padoru.check_sunk()

            else:
                probability_board = Padoru.on_miss_probability_adjustment(probability_board, chosen_position)
                probability_board[chosen_position[0]][chosen_position[1]] = 0
                board_z.board[chosen_position[0]][chosen_position[1]] = "miss"
                Padoru.Store.hit_probability_map = probability_board

        else:
            if Padoru.Store.initial:
                probability_board = Padoru.initial_probability_map(probability_board)
                Padoru.Store.initial = False
            else:
                probability_board = Padoru.Store.probability_map
            # max function
            best_positions = Padoru.maximum_positions(probability_board)
            chosen_position = random.choice(best_positions)
            if board_z.hit_or_miss(chosen_position[1], chosen_position[0]):
                Padoru.Store.Hit = True
                Padoru.Store.boat = board_z.board[chosen_position[0]][chosen_position[1]]
                # function that creates a hit board separate from the board
                # you'll need to make a case for when it hits 2 boats next to eachother
                Padoru.Store.hit_probability_map = Padoru.create_hit_map(chosen_position, board_z)
                Padoru.Store.hit_probability_map[chosen_position[0]][chosen_position[1]] = 0
                probability_board[chosen_position[0]][chosen_position[1]] = 0
                board_z.board[chosen_position[0]][chosen_position[1]] = "hit"
                # update the board
                Padoru.Store.probability_map = probability_board
                Padoru.Store.last_hit = chosen_position + [board_z.board[chosen_position[0]][chosen_position[1]]]

            else:
                probability_board = Padoru.hit_is_miss_adjust(probability_board, chosen_position)
                probability_board[chosen_position[0]][chosen_position[1]] = 0
                board_z.board[chosen_position[0]][chosen_position[1]] = "miss"
                Padoru.Store.probability_map = probability_board
            Padoru.check_sunk()
