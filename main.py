from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SPEED = 0.2
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    time.sleep(SPEED)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.generate_food()
        scoreboard.add_score()
        snake.extend_snake()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with the snake body
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
