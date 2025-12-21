from turtle import Turtle

# Constants for score display
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"

class Score(Turtle):
    """Handles the game score display and game over message"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")  # Avoid animation delay
        self.hideturtle()
        self.goto(0, 260)      # Position at top of screen
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.update_score()    # Initial display

    def update_score(self):
        """Refresh the score on screen"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment score and update display"""
        self.score += 1
        self.clear()           # Clear previous score
        self.update_score()    # Draw new score

    def game_over(self):
        """Display game over message at center"""
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

