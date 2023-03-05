class Board():
    LINES = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]

    def __init__(self):
        self.current_char = "X"
        self.confirm_char = {"X": set(), "O": set()}
        self.temp_position = -1
        self.list_of_char = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.set_chars = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.display_board(self.list_of_char)

    def get_set_numbers(self):
        return [number for number, position in enumerate(self.set_chars) if position in ["X", "O"]]

    def display_board(self, list_chars):
        print("%s | %s | %s" % (list_chars[0], list_chars[1], list_chars[2]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[3], list_chars[4], list_chars[5]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[6], list_chars[7], list_chars[8]))
        print('*********')

    def move(self, step, limit, next_step):
        self.list_of_char = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.list_of_char = self.set_chars[:]
        self.temp_position = self.temp_position + step
        self.check_free_place(step, next_step, limit)
        self.list_of_char[self.temp_position] = self.current_char
        self.display_board(self.list_of_char)

    def save_char(self):
        self.set_chars[self.temp_position] = self.current_char
        self.confirm_char[self.current_char].add(self.temp_position)
        print(self.confirm_char)
        self.display_board(self.set_chars)

    def check_win(self, players):
        for line in self.LINES:
            if set(line).issubset(self.confirm_char[self.current_char]):
                for player in players:
                    if player.get_char() == self.current_char:
                        print("GAME OVER, THE WINNER IS", player)
                        exit()
        if " " not in self.set_chars:
            print("End Game, pat")
            exit()

    def check_free_place(self, step, next_step, limit):
        if self.temp_position == limit:
            self.temp_position = next_step
        while self.set_chars[self.temp_position] in ["X", "O"]:
            self.temp_position = self.temp_position + step
            if self.temp_position == limit:
                self.temp_position = next_step
