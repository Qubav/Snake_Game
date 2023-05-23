from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
PATH = "/data.txt"

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.highest_score = None

        self.check_highest_score_data()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Method writes player score after it clears old score."""
        self.clear()
        self.write(f"Score: {self.score}   Highest Score: {self.highest_score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        """Method increases player score and updates score board."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Method checks if score from previous game has has higher value than highest score and updates it if this criteria is met, and resets player score to 0 and updates scoreboard."""

        if self.score > self.highest_score:

            self.highest_score = self.score
            self.update_highest_score_data()
        
        self.score = 0
        self.update_scoreboard()
        
    def check_highest_score_data(self):
        """Reading data from .txt filer and assigning it highest score attribute value."""

        with open("data.txt") as file:
            value = int(file.read())
        
        self.highest_score = value
    
    def update_highest_score_data(self):
        """Updating data file with new highest score value."""

        with open("data.txt", mode = "w") as file:
            file.write(f"{self.highest_score}")

        
    
