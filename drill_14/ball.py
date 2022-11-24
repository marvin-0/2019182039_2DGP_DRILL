import random
from pico2d import *
import server
import game_world

class Ball:
    image = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21X21.png')
        self.x = random.randint(50, server.background.w - 50)
        self.y = random.randint(50, server.background.h - 50)

    def update(self):
        pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)