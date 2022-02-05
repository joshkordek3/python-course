from turtle import Turtle
class Writer(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x, y)

    def writetext(self, text, font="Arial", size=8, textType="normal", color="black", x=None, y=None):
        if x is None:
            x = self.xcor()
        if y is None:
            y = self.ycor()
        self.goto(x, y)
        self.color(color)
        self.write(text, move=False, align="center", font=(font, size, textType))

class Button(Turtle):
    def __init__(self, position, onclick, shape=(20, 30)):
        self.speed('fastest')
        self.goto(position)
        shapesize = list(shape)
        self.shapesize(stretch_wid=shapesize[0]/20, stretch_len=shapesize[1]/20)
        self.onclick(onclick)

def typeof(value):
    return list(str(type(value)).split('\''))[1]