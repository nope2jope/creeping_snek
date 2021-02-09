from turtle import Turtle

STARTING_X = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
NORTH = 90
WEST = 180
SOUTH = 270
EAST = 0


class Snek(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snek()
        self.head = self.segments[0]

    def create_snek(self):
        for x in STARTING_X:
            self.add_segment(x)

    def reset_snek(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snek()
        self.head = self.segments[0]

    def add_segment(self, pos):
        snek = Turtle(shape="square")
        snek.penup()
        snek.color("white")
        snek.goto(pos)
        self.segments.append(snek)

    def lengthen(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto([new_x, new_y])
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.seth(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.seth(SOUTH)

    def lefty(self):
        if self.head.heading() != EAST:
            self.head.seth(WEST)

    def righty(self):
        if self.head.heading() != WEST:
            self.head.seth(EAST)


