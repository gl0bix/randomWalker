import pygame as pg
import random
import numpy as np

WINDOW_SIZE = 1000
BG_COLOR = pg.Color("black")
STEP = 50
LINE_W = 5
POSSIBLE_STEPS = [(STEP, 0), (-STEP, 0), (0, STEP), (0, -STEP)]

SOME_COLORS = []
for c in ["yellow", "purple", "pink", "orange"]: SOME_COLORS.append(pg.Color(c))

clock = pg.time.Clock()
fps = 10

pg.init()

SCREEN = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

class Stepper:
    RADIUS = 10
    

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def show(self):
        global SCREEN
        pg.draw.circle(SCREEN, self.color, (self.x, self.y), self.RADIUS)

    def step(self):
        global SCREEN

        old_pos = (self.x, self.y)
        new_pos = tuple(np.add(old_pos, (random.choice(POSSIBLE_STEPS))))

        self.x = new_pos[0]
        self.y = new_pos[1]

        pg.draw.line(SCREEN, self.color, old_pos, new_pos, LINE_W)

        self.show()

def randomWalk():

    t1 = Stepper(WINDOW_SIZE // 2, WINDOW_SIZE // 2, random.choice(SOME_COLORS))
    t1.show()


    game_runs = True
    while game_runs:

        e = pg.event.poll()
        if e.type == pg.QUIT:
            game_runs = False
        pg.display.flip()

        # stepping

        t1.step()

        clock.tick(fps)        



def main():
    randomWalk()

if __name__ == "__main__":
    main()