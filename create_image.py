from setting import *
class CubeImage():
    SCHEME = None
    TOP = None
    LEFT = None
    FRONT = None
    RIGHT = None
    BACK = None
    DOWN = None
    RGB_VALUES = {'W': (255, 255, 255), 'O': (255, 125, 0), 'G': (
        0, 255, 0), 'R': (255, 0, 0), 'B': (0, 0, 255), 'Y': (255, 255, 0)}
    IMG = None

    def __init__(self, scheme='WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY'):
        self.SCHEME = scheme
        self.slice_sheme()
        self.draw_cube()

    def slice_sheme(self):
        import numpy as np
        cube_scheme = np.array([i for i in self.SCHEME])
        sides = []
        for i in range(6):
            sides.append(cube_scheme[i*9:(i+1)*9].reshape((3, 3)))
        self.TOP = sides[0]
        self.LEFT = sides[1]
        self.FRONT = sides[2]
        self.RIGHT = sides[3]
        self.BACK = sides[4]
        self.DOWN = sides[5]

    def draw_cube(self):
        from PIL import Image, ImageDraw
        self.IMG = Image.new('RGBA', (136, 101), (51, 51, 51, 0))

        def draw_lines(draw: ImageDraw.Draw, x, y):
            line_col = DARKEST_GRAY
            a = (x, y)
            b = (x+30, y)
            c = (x, y+30)
            d = (x+30, y+30)
            e = (x+10, y)
            f = (x+20, y)
            g = (x, y+10)
            h = (x+30, y+10)
            i = (x, y+20)
            j = (x+30, y+20)
            k = (x+10, y+30)
            l = (x+20, y+30)
            draw.line((*a, *b), line_col, width=1)
            draw.line((*a, *c), line_col, width=1)
            draw.line((*b, *d), line_col, width=1)
            draw.line((*c, *d), line_col, width=1)
            draw.line((*e, *k), line_col, width=1)
            draw.line((*f, *l), line_col, width=1)
            draw.line((*g, *h), line_col, width=1)
            draw.line((*i, *j), line_col, width=1)

        draw = ImageDraw.Draw(self.IMG)
        tile_length = 10
        # * Draw the TOP
        start_pos = (35, 0)
        for i in range(3):
            for j in range(3):
                x1, y1 = start_pos[0]+j*10, start_pos[1]+i*10
                x2, y2 = x1+10, y1+10
                col = self.RGB_VALUES[self.TOP[i][j]]
                draw.rectangle((x1, y1, x2, y2), fill=col)
        draw_lines(draw, *start_pos)
        # * Draw the LEFT
        start_pos = (0, 35)
        for i in range(3):
            for j in range(3):
                x1, y1 = start_pos[0]+j*10, start_pos[1]+i*10
                x2, y2 = x1+10, y1+10
                col = self.RGB_VALUES[self.LEFT[i][j]]
                draw.rectangle((x1, y1, x2, y2), fill=col)
        draw_lines(draw, *start_pos)

        # * Draw the FRONT
        start_pos = (35, 35)
        for i in range(3):
            for j in range(3):
                x1, y1 = start_pos[0]+j*10, start_pos[1]+i*10
                x2, y2 = x1+10, y1+10
                col = self.RGB_VALUES[self.FRONT[i][j]]
                draw.rectangle((x1, y1, x2, y2), fill=col)
        draw_lines(draw, *start_pos)

        # * Draw the RIGHT
        start_pos = (70, 35)
        for i in range(3):
            for j in range(3):
                x1, y1 = start_pos[0]+j*10, start_pos[1]+i*10
                x2, y2 = x1+10, y1+10
                col = self.RGB_VALUES[self.RIGHT[i][j]]
                draw.rectangle((x1, y1, x2, y2), fill=col)
        draw_lines(draw, *start_pos)

        # * Draw the BACK
        start_pos = (105, 35)
        for i in range(3):
            for j in range(3):
                x1, y1 = start_pos[0]+j*10, start_pos[1]+i*10
                x2, y2 = x1+10, y1+10
                col = self.RGB_VALUES[self.BACK[i][j]]
                draw.rectangle((x1, y1, x2, y2), fill=col)
        draw_lines(draw, *start_pos)

        # * Draw the DOWN
        start_pos = (35, 70)
        for i in range(3):
            for j in range(3):
                x1, y1 = start_pos[0]+j*10, start_pos[1]+i*10
                x2, y2 = x1+10, y1+10
                col = self.RGB_VALUES[self.DOWN[i][j]]
                draw.rectangle((x1, y1, x2, y2), fill=col)
        draw_lines(draw, *start_pos)

    def show_img(self):
        self.IMG.show()
