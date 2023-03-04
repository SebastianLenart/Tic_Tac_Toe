from board import Board
from pynput import keyboard
from pynput.keyboard import Key
from player import Player
import random


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
        self.turn = 1
        self.numbers_on_board = {0, 1, 2, 3, 4, 5, 6, 7, 8}
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
            if self.board.temp_position >= 0 and self.board.temp_position not in self.board.get_set_numbers():
                self.board.save_char()
                self.next_turn()
                self.auto_mode()
        elif key == Key.esc:
            exit()

    def start(self):
        selection = input(self.MENU)
        while selection not in ['1', '2']:
            print("Enter correct value!")
        self.mode = selection
        if self.mode == "1":
            name1 = input("Enter name of player 1: ")
            name2 = input("Enter name of player 2: ")
            self.list_of_players.append(Player(name1, "X"))
            self.list_of_players.append(Player(name2, "O"))
        else:
            name1 = input("Enter name of player: ")
            self.list_of_players.append(Player(name1, "X"))
            self.list_of_players.append(Player("Computer", "O"))

    def next_turn(self):
        self.board.current_char = self.list_of_players[self.turn].get_char()
        self.turn += 1
        if self.turn == 2:
            self.turn = 0

    def auto_mode(self):
        if self.mode == "2":
            try:
                number = random.choice(list(self.numbers_on_board - set(self.board.get_set_numbers())))
                print("random:", number)
                self.board.temp_position = number
            except IndexError:
                print("PAT")
                exit()

            self.board.save_char()
            self.next_turn()


if __name__ == "__main__":
    game = Game()
