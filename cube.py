from create_image import CubeImage
from scrambler import Scrambler


class Cube():
    UP = None
    LEFT = None
    FRONT = None
    RIGHT = None
    BACK = None
    DOWN = None

    def __init__(self):
        import numpy as np
        self.UP = np.array([i for i in 'W'*9]).reshape((3, 3))
        self.LEFT = np.array([i for i in 'O'*9]).reshape((3, 3))
        self.FRONT = np.array([i for i in 'G'*9]).reshape((3, 3))
        self.RIGHT = np.array([i for i in 'R'*9]).reshape((3, 3))
        self.BACK = np.array([i for i in 'B'*9]).reshape((3, 3))
        self.DOWN = np.array([i for i in 'Y'*9]).reshape((3, 3))

    def reset(self):
        self.__init__()

    def get_scheme(self):
        scheme = ''
        for i in self.UP.flatten():
            scheme += i
        for i in self.LEFT.flatten():
            scheme += i
        for i in self.FRONT.flatten():
            scheme += i
        for i in self.RIGHT.flatten():
            scheme += i
        for i in self.BACK.flatten():
            scheme += i
        for i in self.DOWN.flatten():
            scheme += i
        return scheme

    def __str__(self):
        return self.get_scheme()

    def apply_move(self, move):
        import numpy as np

        def U():
            self.FRONT[0], self.LEFT[0], self.BACK[0], self.RIGHT[0] = self.RIGHT[0].copy(
            ), self.FRONT[0].copy(), self.LEFT[0].copy(), self.BACK[0].copy()
            self.UP = np.rot90(self.UP, 3)

        def D():
            self.FRONT[2], self.LEFT[2], self.BACK[2], self.RIGHT[2] = self.LEFT[2].copy(
            ), self.BACK[2].copy(), self.RIGHT[2].copy(), self.FRONT[2].copy()
            self.DOWN = np.rot90(self.DOWN, 3)

        def L():
            self.UP[:, :1], self.FRONT[:, :1], self.DOWN[:, :1], self.BACK[:, 2:] = self.BACK[:, 2:][::-1].copy(
            ), self.UP[:, :1].copy(), self.FRONT[:, :1].copy(), self.DOWN[:, :1][::-1].copy()
            self.LEFT = np.rot90(self.LEFT, 3)

        def R():
            self.UP[:, 2:], self.FRONT[:, 2:], self.DOWN[:, 2:], self.BACK[:, :1] = self.FRONT[:, 2:].copy(
            ), self.DOWN[:, 2:].copy(), self.BACK[:, :1][::-1].copy(), self.UP[:, 2:][::-1].copy()
            self.RIGHT = np.rot90(self.RIGHT, 3)

        def F():
            self.UP[2], self.LEFT[:, 2:], self.DOWN[0], self.RIGHT[:, :1] = self.LEFT[:, 2:].flatten(
            )[::-1].copy(), self.DOWN[0].reshape((3, 1)).copy(), self.RIGHT[:, :1].flatten()[::-1].copy(), self.UP[2].reshape((3, 1)).copy()
            self.FRONT = np.rot90(self.FRONT, 3)

        def B():
            self.UP[0], self.LEFT[:, :1], self.DOWN[2], self.RIGHT[:, 2:] = self.RIGHT[:, 2:].flatten(
            ).copy(), self.UP[0][::-1].reshape((3, 1)).copy(), self.LEFT[:, :1].flatten().copy(), self.DOWN[2][::-1].reshape((3, 1)).copy()
            self.BACK = np.rot90(self.BACK, 3)

        utilitie = None

        if len(move) == 2:
            utilitie = move[1]
            move = move[0]

        fnc = None
        if move == 'U':
            fnc = U
        elif move == 'D':
            fnc = D
        elif move == 'L':
            fnc = L
        elif move == 'R':
            fnc = R
        elif move == 'F':
            fnc = F
        elif move == 'B':
            fnc = B

        if utilitie == '2':
            fnc()
            fnc()
        elif utilitie == "'":
            fnc()
            fnc()
            fnc()
        else:
            fnc()

    def apply_algorithm(self, alg):
        for move in alg.split(' '):
            self.apply_move(move)

    def show(self):
        im = CubeImage(self.get_scheme())
        im.show_img()

    def get(self):
        im = CubeImage(self.get_scheme())
        return im.IMG
