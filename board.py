
class Board():
    def __init__(self):
        self.list_of_char = [" ", " ", "X", " ", " ", " ", " ", " ", " "]
        # self.create_board()
        self.move_char_on_board()
        self.current_char = "X"

    def create_board(self):
        print("CLICK ARROW to START")
        print("  |   |  ")
        print("__|___|__")
        print("  |   |  ")
        print("__|___|__")
        print("  |   |  ")

    def move_char_on_board(self):
        print("%s | %s | %s" % (self.list_of_char[0], self.list_of_char[3], self.list_of_char[2]))
        print("__|___|__")
        print("%s | %s | %s" % (self.list_of_char[0], self.list_of_char[3], self.list_of_char[2]))
        print("__|___|__")
        print("%s | %s | %s" % (self.list_of_char[0], self.list_of_char[3], self.list_of_char[2]))
        print("*********")





