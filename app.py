from board import Board
from pynput import keyboard
from pynput.keyboard import Key
from player import Player


class Game():
    MENU = """Options:
1.) PLAYER 1 VS PLAYER 2,    
2.) PLAYER VS COMPUTER
choose: """

    def __init__(self):
        self.mode = None
        self.list_of_players = []
        self.start()
        self.board = Board()
        self.turn = 0
        with keyboard.Listener(on_release=self.on_key_release) as listener:
            listener.join()

    def on_key_release(self, key):
        if key == Key.right:
            print("Right key clicked")
            self.board.move(1, 9, 0)
        elif key == Key.left:
            print("Left key clicked")
            self.board.move(-1, -1, 8)
        elif key == Key.enter:
            print("enter clicked")
            self.board.save_char()
            self.next_turn()
            self.auto_mode()
        elif key == Key.esc:
            exit()

    def start(self):
        selection = input(self.MENU)
        while selection not in ['1', '2']:
            print("Enter correct value!")
        print(self.mode, type(self.mode))
        if self.mode == "1":
            name1 = input("Enter name of player 1")
            name2 = input("Enter name of player 2")
            self.list_of_players.append(Player(name1, "X", 1))
            self.list_of_players.append(Player(name2, "O", 1))
        else:
            name1 = input("Enter name of player")
            self.list_of_players.append(Player(name1, "X", 2))
            self.list_of_players.append(Player("Computer", "O", 2))

    def next_turn(self):
        self.board.current_char = self.list_of_players[self.turn].get_char()
        self.turn += 1
        if self.turn == 2:
            self.turn = 0

    def auto_mode(self):
        if self.mode == "2":
            pass

if __name__ == "__main__":
    game = Game()

















