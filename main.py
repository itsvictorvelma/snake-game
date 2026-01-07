from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

# -----------------------------
# Screen setup
# -----------------------------
# Basic turtle screen config.
# tracer(0) disables auto redraw so we control frames manually.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game innit")
screen.tracer(0)

# -----------------------------
# Game objects
# -----------------------------
# Core game entities.
snake = Snake()
food = Food()
score = Score()

# -----------------------------
# Input bindings
# -----------------------------
# Arrow keys mapped directly to snake direction methods.
# No key buffering, turtle just fires callbacks.
screen.listen()
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


# -----------------------------
# Main game loop
# -----------------------------
# Using ontimer instead of while-loop to keep turtle responsive.
def game_loop():
    # Advance snake one step
    snake.move()

    # -------------------------
    # Food collision
    # -------------------------
    # Distance threshold tuned for segment size.
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()  # add new segment to tail
        food.refresh()  # respawn food somewhere else

    # -------------------------
    # Wall collision
    # -------------------------
    # Screen bounds are 300x300, padding for snake head size.
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        snake.reset()
        score.reset()

    # -------------------------
    # Tail collision
    # -------------------------
    # Skip head (index 0), check rest of the body.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            break  # no need to keep checking once we hit

    # Manual redraw for this frame
    screen.update()

    # Schedule next tick (~10 FPS)
    screen.ontimer(game_loop, 100)


# -----------------------------
# Boot
# -----------------------------
game_loop()
screen.exitonclick()
