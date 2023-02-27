from board import Board
from pynput import keyboard
from pynput.keyboard import Key


class Game():
    MENU = """Options:
1.) PLAYER 1 VS PLAYER 2,    
2.) PLAYER VS COMPUTER
choose: """

    def __init__(self):
        self.mode = None
        self.start()
        self.board = Board()
        self.current_player = None
        with keyboard.Listener(on_release=self.on_key_release) as listener:
            listener.join()

    def on_key_release(self, key):
        if key == Key.right:
            print("Right key clicked")
            self.board.create_board()
        elif key == Key.left:
            print("Left key clicked")
            self.board.create_board()
        elif key == Key.up:
            print("Up key clicked")
            self.board.create_board()
        elif key == Key.down:
            print("Down key clicked")
            self.board.create_board()
        elif key == Key.enter:
            print("enter clicked")
        elif key == Key.esc:
            exit()

    def start(self):
        # print(self.MENU)
        while (selection := input(self.MENU) not in ["1", "2"]):
            print("Enter correct value!")
        self.mode = selection



if __name__ == "__main__":
    game = Game()
