from turtle import Turtle
class Food(Turtle):
    def __init__(self, position=None):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#add8e6")
        self.speed("fastest")
        if position is None:
            self.goto((0, 0))
            return
        self.goto(position)

    def collides(self, turtle):
        return self.distance(turtle) < 17.5
