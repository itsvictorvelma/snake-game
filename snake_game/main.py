from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game innit")
screen.tracer(0)  # Turn off automatic animation for manual screen updates

# Initialize game objects
snake = Snake()
food = Food()
score = Score()

# Set up controls
screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

game_is_on = True

def game_loop():
    """Main game loop called recursively via ontimer"""
    global game_is_on

    if not game_is_on:
        return

    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()  # Update score
        snake.extend()           # Grow the snake
        food.refresh()           # Move food to new location

    # Detect collision with wall
    if (snake.head.xcor() > 290 or
        snake.head.xcor() < -290 or
        snake.head.ycor() < -290 or
        snake.head.ycor() > 290):
        game_is_on = False
        score.game_over()        # End game if snake hits wall
        return

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()    # End game if snake hits itself
            return

    screen.update()              # Refresh screen after each move
    screen.ontimer(game_loop, 100)  # Call loop again after 100ms

# Start the game
game_loop()
screen.mainloop()

