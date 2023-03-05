class Player():
    def __init__(self, name, char):
        self.char = char,
        self.name = name,

    def __str__(self):
        return f"Player {self.name} has got char: {self.char}"
        # NIE MAM POJECIA CZEMU ZWRACAJA SIE TUPLE, TO JUZ KTORYŚ RAZ ZE TUPLE SIE PRZEKAZUJA

    def get_char(self):
        return self.char[0]
