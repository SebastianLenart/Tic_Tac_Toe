from board import Board
from pynput import keyboard
from pynput.keyboard import Key

class Game():
    def __init__(self):
        self.board = Board()


    def on_key_release(key):
        if key == Key.right:
            print("Right key clicked")
        elif key == Key.left:
            print("Left key clicked")
        elif key == Key.up:
            print("Up key clicked")
        elif key == Key.down:
            print("Down key clicked")
        elif key == Key.esc:
            exit()

    with keyboard.Listener(on_release=on_key_release) as listener:
            listener.join()

if __name__ == "__main__":
    game = Game()
