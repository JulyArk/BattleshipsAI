import sys
import pygame, copy
from Board.Board_Creation import *
from Game.AI import Padoru

pygame.init()
pygame.display.set_caption("Battleships")

screen_size = width, height = 1100, 500
speed = [2, 2]
black = 0, 0, 0
old_background = 0, 105, 148
background = 135, 206, 235
boat_color = 169, 169, 169
hit_color = 255, 0, 0
miss_color = 255, 255, 255
player_miss_color = 255, 255, 255
player_hit_color = 255, 0, 0
build_x = 0
build_y = 0
screen = pygame.display.set_mode(screen_size)



class Player:
    def __init__(self, x, y, player_board):
        self.x_pos = x
        self.y_pos = y
        self.board = player_board


class GUI:
    @staticmethod
    def player_win():
        pygame.draw.rect(screen, black, (10, 5, 290, 81))
        pygame.draw.rect(screen, boat_color, (11, 6, 288, 79))
        pygame.draw.rect(screen, black, (20, 15, 270, 60))

        startup_font = pygame.font.SysFont('Times New Roman', 35)
        again_text = startup_font.render("You won!", True, (255, 255, 255))
        screen.blit(again_text, (80, 25))
        pygame.display.update()

    @staticmethod
    def padoru_win():
        pygame.draw.rect(screen, black, (710, 5, 290, 81))
        pygame.draw.rect(screen, boat_color, (711, 6, 288, 79))
        pygame.draw.rect(screen, black, (720, 15, 270, 60))

        startup_font = pygame.font.SysFont('Times New Roman', 35)
        again_text = startup_font.render("Computer won", True, (255, 255, 255))
        screen.blit(again_text, (750, 25))
        pygame.display.update()

    @staticmethod
    def player_vs_pai_end():
        while 1:
            for main_event in pygame.event.get():
                if main_event.type == pygame.QUIT:
                    sys.exit()
                elif main_event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    if 400 < x < 700:
                        if 100 < y < 200:
                            return True
                        elif 250 < y < 350:
                            Padoru.Store.boat = 0
                            Padoru.Store.Hit = False
                            Padoru.Store.probability_map = []
                            Padoru.Store.hit_probability_map = []
                            Padoru.Store.initial = True
                            Padoru.Store.last_hit = []
                            Padoru.Store.counter = 1
                            Padoru.Store.multiple_boats = False
                            Padoru.Store.alive = 5
                            GUI.startup_screen()
                            return False

            pygame.draw.rect(screen, black, (400, 80, 300, 100))
            pygame.draw.rect(screen, black, (400, 230, 300, 100))
            pygame.draw.rect(screen, boat_color, (401, 81, 298, 98))
            pygame.draw.rect(screen, boat_color, (401, 231, 298, 98))
            pygame.draw.rect(screen, black, (410, 90, 280, 80))
            pygame.draw.rect(screen, black, (410, 240, 280, 80))
            startup_font = pygame.font.SysFont('Times New Roman', 35)
            quit_text = startup_font.render('Exit game', True, (255, 255, 255))
            again_text = startup_font.render("Play again", True, (255, 255, 255))
            screen.blit(quit_text, (480, 105))
            screen.blit(again_text, (480, 255))
            pygame.display.update()

    @staticmethod
    def game_over_menu():
        while 1:
            for main_event in pygame.event.get():
                if main_event.type == pygame.QUIT:
                    sys.exit()
                elif main_event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    if 400 < x < 700:
                        if 100 < y < 200:
                            return True
                        elif 250 < y < 350:
                            Padoru.Store.boat = 0
                            Padoru.Store.Hit = False
                            Padoru.Store.probability_map = []
                            Padoru.Store.hit_probability_map = []
                            Padoru.Store.initial = True
                            Padoru.Store.last_hit = []
                            Padoru.Store.counter = 1
                            Padoru.Store.multiple_boats = False
                            Padoru.Store.alive = 5
                            GUI.startup_screen()
                            return False

            pygame.draw.rect(screen, black, (400, 80, 300, 100))
            pygame.draw.rect(screen, black, (400, 230, 300, 100))
            pygame.draw.rect(screen, boat_color, (401, 81, 298, 98))
            pygame.draw.rect(screen, boat_color, (401, 231, 298, 98))
            pygame.draw.rect(screen, black, (410, 90, 280, 80))
            pygame.draw.rect(screen, black, (410, 240, 280, 80))
            startup_font = pygame.font.SysFont('Times New Roman', 35)
            quit_text = startup_font.render('Exit game', True, (255, 255, 255))
            again_text = startup_font.render("Play again", True, (255, 255, 255))
            screen.blit(quit_text, (480, 105))
            screen.blit(again_text, (480, 255))
            pygame.display.update()
            Padoru.Store.boat = 0
            Padoru.Store.Hit = False
            Padoru.Store.probability_map = []
            Padoru.Store.hit_probability_map = []
            Padoru.Store.initial = True
            Padoru.Store.last_hit = []
            Padoru.Store.counter = 1
            Padoru.Store.multiple_boats = False
            Padoru.Store.alive = 5
            Engine.impossible_ai_game()

    @staticmethod
    def coordinate_display(coord_x, coord_y):
        # UI
        startup_font = pygame.font.SysFont('Times New Roman', 22)
        if coord_x > 9:
            coord_x = coord_x - 11
        coord_x += 1
        coord_x = str(coord_x)
        coord_y = chr(ord('A') + coord_y)
        coords = coord_x + coord_y
        display_coord = startup_font.render(coords, True, (0, 0, 0))
        pygame.draw.rect(screen, black, (1052, 12, 43, 43))
        pygame.draw.rect(screen, (255, 255, 255), (1056, 16, 35, 35))
        screen.blit(display_coord, (1060, 20))
        pygame.display.update()

    @staticmethod
    def draw_in_game_frame():
        # UI
        pygame.draw.rect(screen, boat_color, (500, 0, 48, 500))
        pygame.draw.rect(screen, boat_color, (1050, 0, 48, 500))
        pygame.display.update()

    @staticmethod
    def display_enemy(enemy):
        # UI
        for i in range(0, 10):
            for j in range(0, 10):
                if enemy.board.board[i][j] == 'hit':
                    pygame.draw.rect(screen, hit_color, ((j + enemy.x_pos) * 50, (i + enemy.y_pos) * 50, 48, 48))
                    pygame.display.update()
                elif enemy.board.board[i][j] == 'miss':
                    pygame.draw.rect(screen, miss_color, ((j + enemy.x_pos) * 50, (i + enemy.y_pos) * 50, 48, 48))
                    pygame.display.update()
                else:
                    pygame.draw.rect(screen, background, ((j + enemy.x_pos) * 50, (i + enemy.y_pos) * 50, 48, 48))
                    pygame.display.update()

    @staticmethod
    def display_attack_game(player, enemy):
        # UI
        GUI.draw_in_game_frame()
        ships = [2, 3, 4, 5]
        for i in range(0, 10):
            for j in range(0, 10):

                if player.board.board[i][j] == 0:  # o_in_lst, nr_o_list
                    pygame.draw.rect(screen, background, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()

                elif player.board.board[i][j] in ships:
                    pygame.draw.rect(screen, boat_color, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()

                elif player.board.board[i][j] == 'hit':
                    pygame.draw.rect(screen, player_hit_color,
                                     ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()
                elif player.board.board[i][j] == 'miss':
                    pygame.draw.rect(screen, player_miss_color,
                                     ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()
        GUI.display_enemy(enemy)

    @staticmethod
    def display_game(player, enemy):
        # UI
        GUI.draw_in_game_frame()
        ships = [2, 3, 4, 5]
        for i in range(0, 10):
            for j in range(0, 10):

                if player.board.board[i][j] == 0:  # o_in_lst, nr_o_list
                    pygame.draw.rect(screen, background, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()

                elif player.board.board[i][j] in ships:
                    pygame.draw.rect(screen, boat_color, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()

                elif player.board.board[i][j] == 'hit':
                    pygame.draw.rect(screen, hit_color, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()
                elif player.board.board[i][j] == 'miss':
                    pygame.draw.rect(screen, miss_color, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()
        GUI.display_current_board(enemy)

    @staticmethod
    def display_current_board(player):
        # UI
        GUI.draw_in_game_frame()
        ships = [2, 3, 4, 5]
        for i in range(0, 10):
            for j in range(0, 10):

                if player.board.board[i][j] == 0:  # o_in_lst, nr_o_list
                    pygame.draw.rect(screen, background, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()

                elif player.board.board[i][j] in ships:
                    pygame.draw.rect(screen, boat_color, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()

                elif player.board.board[i][j] == 'hit':
                    pygame.draw.rect(screen, hit_color, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()
                elif player.board.board[i][j] == 'miss':
                    pygame.draw.rect(screen, miss_color, ((j + player.x_pos) * 50, (i + player.y_pos) * 50, 48, 48))
                    pygame.display.update()

    @staticmethod
    def ai_menu_shadowing(x, normal_color, impossible_color):
        # UI
        """
        Creates the shadowing effect for the options
        :param x: left = 0 | right = 1
        :param normal_color: = not hovered color for normal option
        :param impossible_color: not hovered color for impossible option
        :return:
        """
        # Done
        normal_shadow = [200, 0, 0]
        impossible_shadow = [186, 209, 215]
        if x == 1:
            GUI.draw_ai_menu(normal_color, impossible_shadow)
        else:
            GUI.draw_ai_menu(normal_shadow, impossible_color)

    @staticmethod
    def draw_ai_menu(normal_color, impossible_color):
        # UI
        """
        Draws onto the screen the AI menu
        :param normal_color: Color for normal option
        :param impossible_color: Color for Impossible option
        :return:
        """
        # Done

        startup_font = pygame.font.SysFont('Times New Roman', 35)
        normal_text = startup_font.render('Normal Mode', True, (0, 0, 0))
        impossible_text = startup_font.render("AI visual", True, (0, 0, 0))

        screen.fill(black)
        pygame.draw.rect(screen, normal_color, (0, 0, 550, 500))  # draw padoru outer color
        pygame.draw.rect(screen, impossible_color, (550, 0, 550, 500))  # draw human outer color
        GUI.startup_frame_draw()

        screen.blit(normal_text, (175, 375))

        screen.blit(impossible_text, (770, 375))
        pygame.display.update()

    @staticmethod
    def ai_setting():
        # UI
        """
        This is where the difficulty option against AI is chosen
        :return:
        """
        # Done
        click = True
        current_pos_x, current_pos_y = 5, 5
        normal_color = [150, 0, 0]
        impossible_color = [82, 96, 109]
        GUI.draw_ai_menu(normal_color, impossible_color)
        while click:
            for main_event in pygame.event.get():
                if main_event.type == pygame.QUIT:
                    sys.exit()
                elif main_event.type == pygame.MOUSEBUTTONUP:
                    click = False
                    x, y = pygame.mouse.get_pos()
                    if x < 550:
                        Engine.normal_ai_game()
                    elif x > 551:
                        Engine.impossible_ai_game()

            new_pos_x, new_pos_y = pygame.mouse.get_pos()
            if new_pos_x < 550:
                new_pos_x = 0
            elif new_pos_x >= 550:
                new_pos_x = 1
            if new_pos_x != current_pos_x:
                current_pos_x = new_pos_x
                GUI.ai_menu_shadowing(current_pos_x, normal_color, impossible_color)

    @staticmethod
    def startup_frame_draw():
        # UI
        """
        Draws a "frame" around the menu, made by 5 rectangles
        :return:
        """
        frame_color = (0, 0, 0)
        pygame.draw.rect(screen, frame_color, (0, 0, 1101, 20))
        pygame.draw.rect(screen, frame_color, (0, 480, 1101, 20))
        pygame.draw.rect(screen, frame_color, (540, 0, 20, 501))
        pygame.draw.rect(screen, frame_color, (0, 0, 20, 501))
        pygame.draw.rect(screen, frame_color, (1080, 0, 20, 501))

    @staticmethod
    def startup_base_draw(padoru, padoru_text, human_text, padoru_color, human_color):
        # UI
        """
        Does the actual drawing of the menu for startup
        :param padoru: img used for AI option
        :param padoru_text: Text for AI option
        :param human_text: Text for 2 player option
        :param padoru_color: Color for left side current
        :param human_color: Color for right side current
        :return:
        """
        # Done
        screen.fill(black)
        pygame.draw.rect(screen, padoru_color, (0, 0, 550, 500))  # draw padoru outer color
        pygame.draw.rect(screen, human_color, (550, 0, 550, 500))  # draw human outer color
        GUI.startup_frame_draw()
        screen.blit(padoru, (150, 87))
        screen.blit(padoru_text, (230, 345))
        screen.blit(human_text, (750, 345))
        pygame.display.update()

    @staticmethod
    def startup_shadow(x, padoru, padoru_text, human_text, padoru_color, human_color):
        # UI
        """
        creates a "shadowing" effect over the hovered option
        :param x: left = 0 / right = 1
        :param padoru: img used for AI option
        :param padoru_text: Text for AI option
        :param human_text: Text for 2 player option
        :param padoru_color: Color for not hovered AI option
        :param human_color: Color for not hovered 2 player option
        :return:
        """
        # Done
        shadow_color_padoru = [200, 0, 0]
        shadow_color_human = [186, 209, 215]
        if x == 1:
            GUI.startup_base_draw(padoru, padoru_text, human_text, padoru_color, shadow_color_human)
        elif x == 0:
            GUI.startup_base_draw(padoru, padoru_text, human_text, shadow_color_padoru, human_color)

    @staticmethod
    def startup_screen():
        """
        Declares the data for the start-up screen, and chooses the type of game : AI  or 2 player
        :return:
        """
        # Done UI
        pygame.font.init()
        padoru = pygame.image.load("padoru.png")
        startup_font = pygame.font.SysFont('Times New Roman', 35)
        padoru_text = startup_font.render('VS AI', True, (0, 0, 0))
        human_text = startup_font.render("VS Human", True, (0, 0, 0))
        current_pos_x, current_pos_y = 5, 5
        padoru_color = [150, 0, 0]
        human_color = [82, 96, 109]
        click = True
        GUI.startup_base_draw(padoru, padoru_text, human_text, padoru_color, human_color)
        while click:
            for main_event in pygame.event.get():
                if main_event.type == pygame.QUIT:
                    sys.exit()
                elif main_event.type == pygame.MOUSEBUTTONUP:
                    click = False
                    x, y = pygame.mouse.get_pos()
                    if x > 551:
                        Engine.human_game()
                    elif x < 550:
                        GUI.ai_setting()

            new_pos_x, new_pos_y = pygame.mouse.get_pos()
            if new_pos_x < 550:
                new_pos_x = 0
            elif new_pos_x >= 550:
                new_pos_x = 1
            if new_pos_x != current_pos_x:
                current_pos_x = new_pos_x
                GUI.startup_shadow(current_pos_x, padoru, padoru_text, human_text, padoru_color, human_color)


class Engine:
    screen_size = width, height = 1100, 500
    speed = [2, 2]
    black = 0, 0, 0
    old_background = 0, 105, 148
    background = 135, 206, 235
    boat_color = 169, 169, 169
    hit_color = 34, 139, 34
    miss_color = 255, 0, 0
    player_miss_color = 255, 255, 255
    player_hit_color = 255, 0, 0
    build_x = 0
    build_y = 0

    @staticmethod
    def check_add_boat_system(orientation, all_boats, player):
        """
        Checks if the player has placed the boat in a valid place and adds it if yes
        :param orientation: "v" or "h"
        :param all_boats: a list containing the current unplaced boats, sorted from big to small
        :param player: the player for which you check
        :return:
        """
        if orientation == 'v':
            o_in_l, lis_nr = pygame.mouse.get_pos()
            pos_x = [int(o_in_l / 50) - player.x_pos, int(lis_nr / 50) - player.y_pos]
            pos_y = [int(o_in_l / 50) - player.x_pos,
                     int(lis_nr / 50) + all_boats[0] - player.y_pos]  # [2,1 + 4] [2, 5]
            boat = Boat(all_boats[0], orientation, pos_x, pos_y)
            if not player.board.outside_board(pos_x, pos_y):
                if not player.board.check_for_boat(boat):
                    player.board.add_boat(boat)
                    all_boats.pop(0)

        elif orientation == 'h':
            o_in_l, lis_nr = pygame.mouse.get_pos()
            pos_x = [int(o_in_l / 50) - player.x_pos, int(lis_nr / 50) - player.y_pos]
            pos_y = [int(o_in_l / 50) + all_boats[0] - player.x_pos, int(lis_nr / 50) - player.y_pos]
            boat = Boat(all_boats[0], orientation, pos_x, pos_y)
            if not player.board.outside_board(pos_x, pos_y):
                if not player.board.check_for_boat(boat):
                    player.board.add_boat(boat)
                    all_boats.pop(0)

    @staticmethod
    def hit_system(or_in_lst, lst_nr, player):
        """
        Checks if the position has a boat
        :param or_in_lst: x coordinate
        :param lst_nr: y coordinate
        :param player: player
        :return: True / False
        """
        x = int(or_in_lst / 50) - player.x_pos
        y = int(lst_nr / 50) - player.y_pos
        if 10 > x > -1 and 10 > y > -1:
            state = player.board.hit_or_miss(x, y)
            if state:
                player.board.board[y][x] = 'hit'
            else:
                player.board.board[y][x] = 'miss'

            x, y = pygame.mouse.get_pos()
            x = int(x / 50) * 50
            y = int(y / 50) * 50
            pygame.draw.rect(screen, (255, 223, 0), (x, y, 48, 48))
            return True
        else:
            return False

    @staticmethod
    def player_position_boats(player, enemy):
        """
        Engine that positions the human player boats
        :param player:
        :param enemy:
        :return:
        """
        carrier = 5
        battleship = 4
        cruiser = 3
        submarine = 3
        destroyer = 2
        orientation = 'v'
        all_boats = [carrier, battleship, cruiser, submarine, destroyer]
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        mouse_position_x = int(mouse_position_x / 50)
        mouse_position_y = int(mouse_position_y / 50)
        orientation_change = False

        while len(all_boats) != 0:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    Engine.check_add_boat_system(orientation, all_boats, player)
            # orientation system
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if orientation == 'v':
                    orientation = 'h'
                    orientation_change = True
                    pygame.time.delay(55)
                elif orientation == 'h':
                    orientation = 'v'
                    orientation_change = True
                    pygame.time.delay(55)
            # ghosting system
            o_in_l, lis_nr = pygame.mouse.get_pos()
            o_in_l = int(o_in_l / 50)
            lis_nr = int(lis_nr / 50)
            GUI.coordinate_display(o_in_l, lis_nr)
            if o_in_l != mouse_position_x or lis_nr != mouse_position_y or orientation_change:
                GUI.display_attack_game(player, enemy)
                mouse_position_x = o_in_l
                mouse_position_y = lis_nr
                orientation_change = False
                try:
                    if orientation == 'v':
                        o_in_l = o_in_l * 50
                        lis_nr = lis_nr * 50
                        for ln in range(0, all_boats[0]):
                            pygame.draw.rect(screen, (153, 50, 204), (o_in_l, lis_nr, 48, 48))
                            lis_nr = lis_nr + 50
                            pygame.display.update()
                    elif orientation == 'h':
                        o_in_l = o_in_l * 50
                        lis_nr = lis_nr * 50
                        for ln in range(0, all_boats[0]):
                            pygame.draw.rect(screen, (153, 50, 204), (o_in_l, lis_nr, 48, 48))
                            o_in_l = o_in_l + 50
                            pygame.display.update()
                except IndexError:
                    pass

    @staticmethod
    def player_check_add_boat_system(orientation, all_boats, player):
        """
        Checks if the player has placed the boat in a valid place and adds it if yes
        :param orientation: "v" or "h"
        :param all_boats: a list containing the current unplaced boats, sorted from big to small
        :param player: the player for which you check
        :return:
        """
        if orientation == 'v':
            o_in_l, lis_nr = pygame.mouse.get_pos()
            pos_x = [int(o_in_l / 50) - player.x_pos, int(lis_nr / 50) - player.y_pos]
            pos_y = [int(o_in_l / 50) - player.x_pos,
                     int(lis_nr / 50) + all_boats[0] - player.y_pos]  # [2,1 + 4] [2, 5]
            boat = Boat(all_boats[0], orientation, pos_x, pos_y)
            if not player.board.outside_board(pos_x, pos_y):
                if not player.board.check_for_boat(boat):
                    player.board.add_boat(boat)
                    all_boats.pop(0)

        elif orientation == 'h':
            o_in_l, lis_nr = pygame.mouse.get_pos()
            pos_x = [int(o_in_l / 50) - player.x_pos, int(lis_nr / 50) - player.y_pos]
            pos_y = [int(o_in_l / 50) + all_boats[0] - player.x_pos, int(lis_nr / 50) - player.y_pos]
            boat = Boat(all_boats[0], orientation, pos_x, pos_y)
            if not player.board.outside_board(pos_x, pos_y):
                if not player.board.check_for_boat(boat):
                    player.board.add_boat(boat)
                    all_boats.pop(0)

    @staticmethod
    def ai_attack_sys(player_1, player_2):
        """
        HIT Engine for the attack system for player vs AI
        :param player_1: player
        :param player_2: AI
        :return:
        """
        attack_mouse_pos_x, attack_mouse_pos_y = pygame.mouse.get_pos()
        attack_mouse_pos_x = int(attack_mouse_pos_x / 50)
        attack_mouse_pos_y = int(attack_mouse_pos_y / 50)
        took_action = False
        while not took_action:

            for main_event in pygame.event.get():
                if main_event.type == pygame.QUIT:
                    sys.exit()
                elif main_event.type == pygame.MOUSEBUTTONUP:
                    or_in_l, lst_nr = pygame.mouse.get_pos()
                    if Engine.hit_system(or_in_l, lst_nr, player_2):
                        took_action = True

            curr_mouse_x, curr_mouse_y = pygame.mouse.get_pos()
            curr_mouse_x = int(curr_mouse_x / 50)
            curr_mouse_y = int(curr_mouse_y / 50)
            if curr_mouse_x != attack_mouse_pos_x or curr_mouse_y != attack_mouse_pos_y:
                GUI.display_attack_game(player_1, player_2)
                attack_mouse_pos_x = curr_mouse_x
                attack_mouse_pos_y = curr_mouse_y

                or_in_l, lst_nr = pygame.mouse.get_pos()
                or_in_l = int(or_in_l / 50) * 50
                lst_nr = int(lst_nr / 50) * 50
                GUI.display_attack_game(player_1, player_2)
                pygame.draw.rect(screen, (255, 223, 0), (or_in_l, lst_nr, 48, 48))
                GUI.coordinate_display(curr_mouse_x, curr_mouse_y)
                pygame.display.update()

        GUI.display_attack_game(player_1, player_2)

    @staticmethod
    def attack_sys(player_1, player_2):
        """
        HIT Engine for the attack system for 2 players
        :param player_1: player
        :param player_2: enemy
        :return:
        """
        attack_mouse_pos_x, attack_mouse_pos_y = pygame.mouse.get_pos()
        attack_mouse_pos_x = int(attack_mouse_pos_x / 50)
        attack_mouse_pos_y = int(attack_mouse_pos_y / 50)
        took_action = False
        while not took_action:

            for main_event in pygame.event.get():
                if main_event.type == pygame.QUIT:
                    sys.exit()
                elif main_event.type == pygame.MOUSEBUTTONUP:
                    or_in_l, lst_nr = pygame.mouse.get_pos()
                    if Engine.hit_system(or_in_l, lst_nr, player_2):
                        took_action = True

            curr_mouse_x, curr_mouse_y = pygame.mouse.get_pos()
            curr_mouse_x = int(curr_mouse_x / 50)
            curr_mouse_y = int(curr_mouse_y / 50)
            if curr_mouse_x != attack_mouse_pos_x or curr_mouse_y != attack_mouse_pos_y:
                GUI.display_attack_game(player_1, player_2)
                attack_mouse_pos_x = curr_mouse_x
                attack_mouse_pos_y = curr_mouse_y

                or_in_l, lst_nr = pygame.mouse.get_pos()
                or_in_l = int(or_in_l / 50) * 50
                lst_nr = int(lst_nr / 50) * 50
                GUI.display_attack_game(player_1, player_2)
                pygame.draw.rect(screen, (255, 223, 0), (or_in_l, lst_nr, 48, 48))
                GUI.coordinate_display(curr_mouse_x, curr_mouse_y)
                pygame.display.update()

        GUI.display_attack_game(player_1, player_2)
        pygame.time.delay(200)
        screen.fill(black)
        pygame.display.update()
        pygame.time.delay(200)

    @staticmethod
    def normal_ai_game():
        """
        Normal AI vs player game
        :return:
        """
        screen.fill(black)
        # create Human
        human_player_board = Board()
        human_player_board.create_empty_board()
        human_player = Player(0, 0, human_player_board)
        # create padoru
        padoru_ai_board = Padoru.ai_placing_boats()
        padoru_ai = Player(11, 0, padoru_ai_board)
        # put player boards
        Engine.player_position_boats(human_player, padoru_ai)
        while 1:
            for main_event in pygame.event.get():
                if main_event.type == pygame.QUIT:
                    sys.exit()
            Engine.ai_attack_sys(human_player, padoru_ai)
            if Engine.check_player_win(padoru_ai_board.board):
                GUI.player_win()
                if GUI.player_vs_pai_end():
                    break
            pygame.time.delay(150)
            Padoru.ai_attack(human_player_board)
            if Padoru.win_condition():
                GUI.padoru_win()
                if GUI.player_vs_pai_end():
                    break
            elif Engine.check_player_win(human_player_board.board):
                GUI.padoru_win()
                if GUI.player_vs_pai_end():
                    break

    @staticmethod
    def impossible_ai_game():
        # ENGINE
        """
        The AI knows where the player boats are, so the player has to play a perfect game in order to win.
        :return:
        """
        screen.fill(black)
        # create Human
        antipadoru = copy.deepcopy(Padoru())
        human_player_board = antipadoru.ai_placing_boats()
        human_player = Player(0, 0, human_player_board)
        # create padoru
        padoru = copy.deepcopy(Padoru())
        padoru_ai_board = padoru.ai_placing_boats()
        padoru_ai = Player(11, 0, padoru_ai_board)
        # put player boards
        while 1:
            for main_event in pygame.event.get():
                if main_event.type == pygame.QUIT:
                    sys.exit()

            padoru.ai_attack(human_player_board)

            GUI.display_game(human_player, padoru_ai)
            pygame.display.update()

            if padoru.win_condition():
                GUI.padoru_win()
                if GUI.game_over_menu():
                    break
            elif Engine.check_player_win(human_player_board.board):
                GUI.padoru_win()
                if GUI.game_over_menu():
                    break

    @staticmethod
    def human_game():
        # ENGINE
        """
        Creates a game for 2 player, runs it, etc.
        :return:
        """

        screen.fill((0, 0, 0))
        player_board1 = Board()
        player_board1.create_empty_board()

        player1 = Player(0, 0, player_board1)

        player_board2 = Board()
        player_board2.create_empty_board()

        player2 = Player(11, 0, player_board2)

        Engine.player_position_boats(player1, player2)
        screen.fill(black)
        pygame.display.update()
        pygame.time.delay(500)
        Engine.player_position_boats(player2, player1)

        screen.fill(black)
        pygame.display.update()
        pygame.time.delay(500)

        GUI.display_game(player2, player1)
        while 1:
            Engine.attack_sys(player1, player2)
            Engine.attack_sys(player2, player1)

    @staticmethod
    def check_player_win(board):
        """
        checks if a player won the game in a current state
        :param board: enemy board
        :return: True = win, False = keep going
        """
        win = True
        for i in range(0, 10):
            for j in range(0, 10):
                if board[i][j] != "miss" and board[i][j] != "hit":
                    if 0 < board[i][j] < 5:
                        win = False

        return win


if __name__ == '__main__':
    GUI.startup_screen()
