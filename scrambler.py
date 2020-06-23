class Scrambler():
    MOVES = ['U', 'D', 'L', 'R', 'F', 'B']
    SCRAMBLE = []
    SCRAMBLE_STR = ''

    def __init__(self, length=15):
        self.generate(length)
        self.__str__()

    def generate(self, length=15):
        from random import randint, choice
        self.SCRAMBLE = []
        utilities = ["'", "2"]
        last_move = ''
        for _ in range(length):
            to_do = randint(1, 3)

            move = choice(self.MOVES)

            while move == last_move:
                move = choice(self.MOVES)

            if to_do == 1 or to_do == 2:
                self.SCRAMBLE.append(''.join([move, utilities[to_do-1]]))

            elif to_do == 3:
                self.SCRAMBLE.append(move)
            last_move = move
        self.__str__()

    def __str__(self):
        self.SCRAMBLE_STR = ''
        for c in self.SCRAMBLE:
            self.SCRAMBLE_STR += c
            self.SCRAMBLE_STR += ' '
        return self.SCRAMBLE_STR[:-1]
