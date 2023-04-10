from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.segments = []
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        last_segment_position = self.segments[-1].position()
        self.add_segment(last_segment_position)

    def move(self):
        for seg_num in reversed(range(1, len(self.segments))):
            new_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_position)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def has_collided_with_walls(self):
        return (
            self.head.xcor() > 300
            or self.head.xcor() < -300
            or self.head.ycor() > 300
            or self.head.ycor() < -300
        )

    def has_collided_with_segment(self, segment):
        return self.head.distance(segment) < 5

    def has_collided_with_itself(self):
        return any(
            self.has_collided_with_segment(segment) for segment in self.segments[1:]
        )

    def game_over(self):
        if self.has_collided_with_walls():
            return True

        return self.has_collided_with_itself()

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.create_snake()
        self.head = self.segments[0]
