class Board():
    def __init__(self):
        self.current_char = "X"
        self.confirm_char = {"X": [], "O": []}
        self.temp_position = 0
        self.list_of_char = [self.current_char, " ", " ", " ", " ", " ", " ", " ", " "]
        self.create_board()
        self.sets_save_chars = set()
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

    def move(self, step, limit, return_step, vertical=1, constant_left=1):
        self.list_of_char = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.temp_position = self.temp_position + step
        self.check_free_place(step)
        if self.temp_position == limit:
            self.temp_position = self.temp_position - vertical * return_step
            self.check_free_place(step)
            self.list_of_char[self.temp_position] = self.current_char
        elif self.temp_position == limit + constant_left * return_step:
            self.temp_position = self.temp_position - vertical * return_step
            self.check_free_place(step)
            self.list_of_char[self.temp_position] = self.current_char
        elif self.temp_position == limit + 2 * return_step * constant_left:
            self.temp_position = self.temp_position - vertical * return_step
            self.check_free_place(step)
            self.list_of_char[self.temp_position] = self.current_char
        else:
            self.list_of_char[self.temp_position] = self.current_char
        self.display_board(self.list_of_char)

    def save_char(self):
        self.sets_save_chars.add(self.temp_position)
        print("savechar", self.sets_save_chars)

    def check_free_place(self, step):
        if self.temp_position in list(self.sets_save_chars):
            self.current_char = "w" # unneccesary
