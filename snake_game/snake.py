from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    """Represents the snake in the game, handles movement and growth"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # First segment is the head

    def create_snake(self):
        """Initialize snake with starting positions"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment at the given position"""
        segment = Turtle("square")
        segment.speed(0)        # Instant movement
        segment.color("white")
        segment.penup()         # No drawing lines
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Add a segment to the end of the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by shifting each segment"""
        for s_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s_num - 1].xcor()
            new_y = self.segments[s_num - 1].ycor()
            self.segments[s_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Direction controls with prevention of 180-degree turns
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



