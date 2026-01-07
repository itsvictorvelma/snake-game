from turtle import Turtle
import random


class Food(Turtle):
    """Represents the food the snake eats, handles random repositioning"""

    def __init__(self):
        super().__init__()
        self.penup()  # Don’t draw lines
        self.shape("circle")
        self.color("gold")
        self.shapesize(stretch_len=1, stretch_wid=1)  # Make it smaller than default
        self.speed("fastest")  # Instant movement

    def refresh(self):
        """Move food to a random position on screen"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
