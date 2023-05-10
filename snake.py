import turtle
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

turtle.colormode(255)

class Snake():

    def __init__(self) -> None:
        
        self.snake_body: list [Turtle] = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self) -> None:
        """Function creates snake body"""

        for i in range(3):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x = i * (-20), y = 0)
            self.snake_body.append(new_segment)

    def move(self) -> None:
        """Function makes snake body move by defined move distance. Each snake body segment moves into position of previous one,
         expect of 1st segment, which goes forward into set direction."""

        # loop that goes through each snake body segment, expect 1st one
        for segm_num in range(len(self.snake_body) - 1,  0, -1):

            # getting new x and y coordinates by reading previous segment coordinates
            new_x = self.snake_body[segm_num  - 1].xcor()
            new_y = self.snake_body[segm_num  - 1].ycor()
            # setting new coordinates
            self.snake_body[segm_num].goto(new_x, new_y)

        # moving 1st segment of snake body forward in set direction 
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        """Function sets snakes head direction to up. If snake is heading """

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """Function sets snakes head direction to down."""

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """Function sets snakes head direction to left."""

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """Function sets snakes head direction to right."""

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)