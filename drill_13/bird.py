from pico2d import *
import game_framework
import random

PIXEL_PER_METER = (10.0 / 0.6)
RUN_SPEED_KMPH = 60.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/ TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(10, 1400), 400
        self.frame = 0
        self.dir = 1
        self.image = load_image('bird_animation.png')
        self.line = 2
        self.frame_count = 5

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if self.frame >= 5 and self.line == 2:
            self.line = 1
            self.frame = 0
        elif self.frame >= 5 and self.line == 1:
            self.line = 0
            self.frame = 0
            self.frame_count = 4
        elif self.frame >= 4 and self.line == 0:
            self.line = 2
            self.frame = 0
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1600 or self.x < 0:
            self.dir *= -1



    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame)*182, self.line * 168, 182, 168, 0.0, '', self.x, self.y, 100, 100)
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*182, self.line * 168, 182, 168, 0.0, 'h', self.x, self.y, 100, 100)


