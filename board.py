from colorama import Fore, Back, Style

class Colors:
    red = '\033[31m'

class Board():
    def __init__(self):
        self.current_char = "X"
        self.confirm_char = {"X": [], "O": []}
        self.temp_position = -1
        self.list_of_char = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.set_chars = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.display_board(self.list_of_char)

    def display_board(self, list_chars):
        print("%s | %s | %s" % (list_chars[0], list_chars[1], list_chars[2]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[3], list_chars[4], list_chars[5]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[6], list_chars[7], list_chars[8]))
        print(Colors.red+'*********')

    def move(self, step, limit, next_step):
        self.list_of_char = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.list_of_char = self.set_chars[:]
        self.temp_position = self.temp_position + step
        print("temp_pos", self.temp_position)
        if self.temp_position == limit:
            self.temp_position = next_step
            self.check_free_place(step, next_step, limit)
            self.list_of_char[self.temp_position] = self.current_char
        else:
            self.check_free_place(step, next_step, limit)
            self.list_of_char[self.temp_position] = self.current_char
        self.display_board(self.list_of_char)

    def save_char(self):
        if self.temp_position >= 0:
            self.set_chars[self.temp_position] = self.current_char
            print([number for number, position in enumerate(self.set_chars) if position in ["X", "O"]])

    def check_free_place(self, step, next_step, limit):
        if " " not in self.set_chars:
            print("End Game, pat")
            exit()
        while self.set_chars[self.temp_position] in ["X", "O"]:
            self.temp_position = self.temp_position + step
            if self.temp_position == limit:
                self.temp_position = next_step

