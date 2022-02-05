from turtle import Turtle

class Rectangle(Turtle):
    def __init__(self, x, y, width, height, color='white'):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.shape('square')
        self.shapesize(stretch_wid=(height / 20), stretch_len=(width / 20))

