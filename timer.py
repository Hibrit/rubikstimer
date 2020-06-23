import pygame
from setting import *


class Timer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.start_time = 0
        self.timer_state = False
        self.active_time = 0
        self.inspection_timer = False

    def toggle_timer(self):
        self.timer_state = not self.timer_state
        if self.timer_state:
            self.start_time = pygame.time.get_ticks()
        else:
            self.active_time = pygame.time.get_ticks()-self.start_time
            return self.active_time

    def get_active_time(self):
        if self.timer_state:
            return pygame.time.get_ticks()-self.start_time
        else:
            return self.active_time

    def get_inspection_time(self):
        return int(INSPECTION_TIME-(pygame.time.get_ticks() - self.start_time)/1000)

    def toggle_inspection_timer(self):
        self.inspection_timer = not self.inspection_timer
        if self.inspection_timer:
            self.start_time = pygame.time.get_ticks()
