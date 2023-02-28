
class Board():
    def __init__(self):
        self.current_char = "X"
        self.temp_position = 0
        self.list_of_char = [self.current_char, " ", " ", " ", " ", " ", " ", " ", " "]
        self.create_board()
        # self.move_char_on_board(self.list_of_char)


    def create_board(self):
        print("CLICK ARROW to START")
        print("  |   |  ")
        print("__|___|__")
        print("  |   |  ")
        print("__|___|__")
        print("  |   |  ")

    def display_board(self, list_chars):
        print("%s | %s | %s" % (list_chars[0], list_chars[1], list_chars[2]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[3], list_chars[4], list_chars[5]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[6], list_chars[7], list_chars[8]))
        print("*********")

    def move_right(self):
        self.list_of_char = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.temp_position = self.temp_position + 1
        if 4 > self.temp_position > 2:
            self.temp_position = 0
            self.list_of_char[self.temp_position] = self.current_char
        elif 7 > self.temp_position > 5:
            self.temp_position = 3
            self.list_of_char[self.temp_position] = self.current_char
        elif 10 > self.temp_position > 8:
            self.temp_position = 6
            self.list_of_char[self.temp_position] = self.current_char
        else:
            self.list_of_char[self.temp_position] = self.current_char
        print(self.temp_position)
        self.display_board(self.list_of_char)

    def move_left(self):
        self.list_of_char = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.temp_position = self.temp_position - 1
        if 0 > self.temp_position:
            self.temp_position = 2
            self.list_of_char[self.temp_position] = self.current_char
        elif 3 > self.temp_position > 1:
            self.temp_position = 5
            self.list_of_char[self.temp_position] = self.current_char
        elif 6 > self.temp_position > 4:
            self.temp_position = 8
            self.list_of_char[self.temp_position] = self.current_char
        else:
            self.list_of_char[self.temp_position] = self.current_char
        print(self.temp_position)
        self.display_board(self.list_of_char)






