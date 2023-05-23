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
        
        # defining snake body as list with Turtle class objects, creating snake's body and defining 1st object in snake's body as head
        self.snake_body: list [Turtle] = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self) -> None:
        """Method creates snake's body"""

        # creating 3 turtle objects, that will be segments of snake body
        # turtle objects shape is set to square, color to white and pen is up so there is no track left
        # their coordinates are set that they together create one body
        for i in range(3):
            position = (i * (-20), 0)
            self.add_segment(position)

    def move(self) -> None:
        """Method makes snake's body move by defined move distance. Each snake's body segment moves into position of previous one,
         expect the head of the snake, which goes forward into set direction."""

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
        """Method sets the head of the snake direction to up. Direction is not changed if current direction is down."""

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """Method sets the head of the snake direction to down. Direction is not changed if current direction is up."""

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """Method sets the head of the snake direction to left.  Direction is not changed if current direction is right."""

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """Method sets the head of the snake direction to right.  Direction is not changed if current direction is left."""

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def add_segment(self, position: tuple) -> None:
        """Method creates new segment and adds it to snake's."""

        # creating new Tutrle object that will be used as segment in snake's body, appending it to snake's body
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position[0], position[1])
        self.snake_body.append(new_segment)

    def extend(self):
        """Method creates new snake's body segment that will be at the end of snake's body."""
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        """Method creates new snake body."""

        for segment in self.snake_body:
            segment.goto(1000, 1000)
        
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]