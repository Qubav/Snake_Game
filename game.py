from turtle import Screen
import turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

turtle.colormode(255)

class Game():

    def __init__(self) -> None:

        # setting up screen
        self.screen =  Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.screen.update()

        # setting up Snake, Food and ScoreBoard objects
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = ScoreBoard()

        # defining variable that is essential for game going on
        self.game_is_on = True

    def collision_w_food(self) -> None:
        """Function make new food object appear in random place on map, extends snake's body and increases player's score."""

        self.food.refresh()
        self.snake.extend()
        self.scoreboard.increase_score()

    def play(self) -> None:
        """Function lets player to play."""

        # using Screen object methods to assign functions to keys and game to interact with player pressing keys
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

        # main loop where all snake's actions take place
        while self.game_is_on:

            # updating screen and making snake move
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            # detecting snake's collision with food
            if self.snake.head.distance(self.food) < 15:
                self.collision_w_food()
                
            # detecting snake's collision with walls - reason to end game
            if self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280:
                self.scoreboard.reset()
                self.snake.reset()

            # detect collision with tail  - reason to end game
            for segment in self.snake.snake_body[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.scoreboard.reset()
                    self.snake.reset()

        # using Screen method to make window wait for click to end - this is available after game is over
        self.screen.exitonclick()