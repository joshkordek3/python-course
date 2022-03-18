from turtle import Turtle
from shapes import Rectangle


class Writer(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.hideturtle()

    def writetext(self, text, font="Arial", size=8, textType="normal", color="black", x=None, y=None):
        if x is None:
            x = self.xcor()
        if y is None:
            y = self.ycor()
        self.goto(x, y)
        self.color(color)
        self.write(text, move=False, align="center", font=(font, size, textType))

class KeyHandler:
    def __init__(self, screen):
        self.screen = screen
        self._keys = []
        self._run = []
        screen.listen()

    def addkey(self, key, bind):
        self._run.append([key, bind])

        def modify(operation):
            def func():
                if operation is 'add':
                    if self._keys.count(key) is 0:
                        self._keys.append(key)
                if operation is 'remove':
                    if self._keys.count(key) > 0:
                        self._keys.remove(key)
            return func
        self.screen.onkeypress(modify("add"), key)
        self.screen.onkeyrelease(modify("remove"), key)

    def run(self):
        for run in self._run:
            if self._keys.count(run[0]) > 0:
                run[1]()

class Button(Rectangle):
    def __init__(self, position, width, height, text, onclick, color="gray"):
        position = list(position)
        super().__init__(position[0], position[1], width, height, color)
        writer = Writer(position[0], position[1])
        writer.writetext(text, color="white")
        self.goto(position[0], position[1])
        self.onclick(onclick)

def move(thing, x_change, y_change, x_min=float('-inf'), x_max=float('inf'), y_min=float('-inf'), y_max=float('inf')):
    def func():
        thing.goto(thing.xcor() + x_change, thing.ycor() + y_change)
        if thing.xcor() < x_min:
            thing.setx(x_min)
        if thing.ycor() < y_min:
            thing.sety(y_min)
        if thing.xcor() > x_max:
            thing.setx(x_max)
        if thing.ycor() > y_max:
            thing.sety(y_max)
    return func

def bool_to_num(boolean):
    if boolean:
        return 1
    return 0

def typeof(value):
    return list(str(type(value)).split('\''))[1]
