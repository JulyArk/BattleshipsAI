from Board.UI.GUI import GUI
from Game.Interface_game import InterfaceGame

if __name__ == '__main__':
    print("1 = Interface  || 2 = GUI \n")
    x = int(input("Choose mode ="))
    if x == 1:
        InterfaceGame.create_game_2_player()
    else:
        GUI.startup_screen()
