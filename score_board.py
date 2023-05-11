from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_score_board()
    
    def update_score_board(self):
        """Function writes player score after it clears old score."""
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        """Function increases player score and updates score board."""
        self.score += 1
        self.update_score_board()
    
    def game_over(self):
        """Function writes \"GAME OVER\" in center of game window to let player know game has ended."""
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
        

        
    
