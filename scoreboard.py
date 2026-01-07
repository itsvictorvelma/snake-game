from turtle import Turtle
import os

# -----------------------------
# Filesystem / persistence
# -----------------------------
# Get absolute path to *this* file.
# This avoids VS Code / terminal CWD weirdness and keeps the score file
# living next to the game code where it belongs.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCORE_FILE = os.path.join(BASE_DIR, "score_storage.txt")

# -----------------------------
# UI constants
# -----------------------------
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    """
    Handles score rendering + high score storage.
    No game-over screen anymore, death just hard resets the run.
    """

    def __init__(self):
        super().__init__()

        # Score for the current run
        self.score = 0

        # Pull high score from disk
        # File is expected to exist at this point
        with open(SCORE_FILE, mode="r") as score_storage:
            contents = score_storage.read()
            self.highscore = contents  # kept as str, cast when comparing

        # Turtle setup for HUD text
        self.color("white")
        self.penup()
        self.speed("fastest")  # skip animation frames
        self.hideturtle()
        self.goto(0, 260)  # top of the screen

        # First draw
        self.write(
            f"Score: {self.score} | High Score: {self.highscore}",
            align=ALIGNMENT,
            font=FONT,
        )

        # Centralized redraw path
        self.update_score()

    def update_score(self):
        """Clear HUD and redraw score state."""
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.highscore}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        """Increment score by one and refresh HUD."""
        self.score += 1
        self.update_score()

    # -----------------------------
    # High score persistence
    # -----------------------------

    def add_new_highscore(self):
        """Write the new high score to disk (overwrite)."""
        with open(SCORE_FILE, mode="w") as score_storage:
            score_storage.write(str(self.score))

    def update_highscore(self):
        """Re-sync in-memory high score with file."""
        with open(SCORE_FILE, mode="r") as score_storage:
            contents = score_storage.read()
            self.highscore = contents

    def reset(self):
        """
        Called on collision / death.
        If this run beats the stored high score, persist it.
        Then zero the score and redraw.
        """
        if self.score > int(self.highscore):
            self.add_new_highscore()
            self.update_highscore()

        self.score = 0
        self.update_score()
