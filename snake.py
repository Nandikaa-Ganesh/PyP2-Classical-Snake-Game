from turtle import Turtle

STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.heads = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        length = len(self.segments)
        turtle_i = Turtle()
        turtle_i.penup()
        turtle_i.shape("square")
        if length % 2 == 0:
            turtle_i.color("yellow")
        else:
            turtle_i.color("lawngreen")
        turtle_i.goto(position)

        self.segments.append(turtle_i)

    def reset(self):
        for i in self.segments:
            i.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.heads = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.heads.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.heads.heading() != DOWN:
            self.heads.setheading(UP)

    def move_down(self):
        if self.heads.heading() != UP:
            self.heads.setheading(DOWN)

    def move_left(self):
        if self.heads.heading() != RIGHT:
            self.heads.setheading(LEFT)

    def move_right(self):
        if self.heads.heading() != LEFT:
            self.heads.setheading(RIGHT)
