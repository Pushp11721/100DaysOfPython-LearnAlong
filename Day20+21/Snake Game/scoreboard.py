from turtle import Turtle
ALIGNMENT="center"
FONT=('Courier',20,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore=0
        with open("data.txt",mode="r") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.write(arg=f"Score={self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score={self.score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.clear()
        self.write(arg=f"Score={self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)