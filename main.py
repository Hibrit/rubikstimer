# imports
import pygame
import random
from setting import *
import scrambler
from timer import Timer
import cube
from databasemanagement import Database, Time
import sqlite3


class SpeedCubeTimer():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Timer')
        self.clock = pygame.time.Clock()
        self.running = True
        self.t = Timer()
        self.last_time = 0
        self.font_name = pygame.font.match_font('arial')
        self.timer_time = 0
        self.scramble = ''
        self.s = scrambler.Scrambler()
        self.last_scramble = self.s.SCRAMBLE_STR
        self.c = cube.Cube()
        self.c.apply_algorithm(str(self.s))
        self.img = self.c.get().resize((270, 200))
        self.img = pygame.image.fromstring(
            self.img.tobytes(), self.img.size, self.img.mode).convert()
        self.img.set_colorkey(BLACK)
        self.avgo5 = 0
        self.avgo12 = 0
        self.d = Database()
        self.holding_space = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
            pygame.display.flip()
        else:
            pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.holding_space = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.holding_space = False
                    if not self.t.timer_state and not self.t.inspection_timer:
                        self.t.toggle_inspection_timer()
                    elif not self.t.timer_state and self.t.inspection_timer:
                        self.t.toggle_inspection_timer()
                        self.t.toggle_timer()
                    elif self.t.timer_state and not self.t.inspection_timer:
                        self.t.toggle_timer()
                        self.s.generate()
                        self.c.reset()
                        self.c.apply_algorithm(str(self.s))
                        self.img = self.c.get().resize((270, 200))
                        self.img = pygame.image.fromstring(
                            self.img.tobytes(), self.img.size, self.img.mode).convert()
                        self.img.set_colorkey(BLACK)
                    elif self.t.timer_state and self.t.inspection_timer:
                        self.t.toggle_inspection_timer()

                if event.key == pygame.K_r:
                    self.s.generate()

    def draw(self):
        if self.t.inspection_timer:
            self.screen.fill(DARK_GRAY)
            self.write_text(f'{self.timer_time}', 128,
                            WIDTH/2, HEIGHT*.5, GRAY)
        else:
            if self.t.timer_state:
                self.screen.fill(DARK_GRAY)
                self.write_text('{0:.2f}'.format(
                    self.timer_time/1000), 128, WIDTH/2, HEIGHT/2, GRAY)

            else:
                if self.holding_space:
                    self.screen.fill(DARK_GRAY)
                    self.write_text('{0:.2f}'.format(
                        self.timer_time/1000), 64, WIDTH/2, HEIGHT*.25, GRAY)
                    self.write_text(f'{self.s}', 24,
                                    WIDTH/2, HEIGHT*.5, GRAY)
                    # self.write_text()
                    # self.write_text()
                    self.show_cube_image(alpha=True)
                else:
                    self.screen.fill(GRAY)
                    self.write_text('{0:.2f}'.format(
                        self.timer_time/1000), 64, WIDTH/2, HEIGHT*.25, WHITE)
                    self.write_text(f'{self.s}', 24,
                                    WIDTH/2, HEIGHT*.5, WHITE)
                    # self.write_text()
                    # self.write_text()
                    self.show_cube_image()

    def show_cube_image(self, alpha=False):
        # if alpha:
        #     a = 128
        #     self.img.fill((255, 255, 255, a), None, pygame.BLEND_RGBA_MULT)

        rect = self.img.get_rect()
        rect.center = (WIDTH//2, int(HEIGHT*.8))
        self.screen.blit(self.img, rect)

    def write_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (int(x), int(y))
        self.screen.blit(text_surface, text_rect)

    def update(self):
        if not self.t.timer_state and not self.t.active_time == 0:
            self.timer_time = self.t.get_active_time()
        if not self.t.timer_state and not self.t.active_time == 0 and not self.last_time == self.t.active_time:
            self.last_time = self.timer_time
        if self.t.timer_state:
            self.timer_time = self.t.get_active_time()
        if self.t.inspection_timer:
            self.timer_time = self.t.get_inspection_time()
        if self.timer_time == 0 and self.t.inspection_timer:
            self.t.toggle_inspection_timer()
            self.t.toggle_timer()


sct = SpeedCubeTimer()
sct.run()
