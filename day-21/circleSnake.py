from turtle import Turtle

class Snake:
    def __init__(self, starting_length=3, display=["#000"], headColor="black"):
        self.head = Turtle("circle")
        self.head.color(headColor)
        self.head.penup()
        self.direction = 0
        self.display = display
        self.SG = False
        self.can_turn = True
        self.headColor = headColor
        self.segments = [self.head]
        self.extend(starting_length)

    def collideswith(self, other_segments):
        for segment in other_segments:
            if segment == self.head:
                continue
            if self.head.distance(segment) <= 5:
                return True
        return False

    def gameover(self):
        if not self.SG:
            return
        self.head.goto(0, 0)
        self.head.color("white")
        self.head.write("GAME OVER", False, "center", ("Calibri", 24, "bold"))
        self.head.color(self.headColor)

    def clear_idle_segments(self, screen, other_segments=[]):
        for turtle in screen.turtles():
            if self.segments.count(turtle) == 0 and other_segments.count(turtle) == 0:
                turtle.reset()
                turtle.hideturtle()

    def headRight(self):
        if self.SG and (self.direction == 180 or (not self.can_turn)):
            return
        self.head.setheading(0)
        self.direction = self.head.heading()
        self.can_turn = False

    def headLeft(self):
        if self.SG and (self.direction == 0 or (not self.can_turn)):
            return
        self.head.setheading(180)
        self.direction = self.head.heading()
        self.can_turn = False

    def headUp(self):
        if self.SG and (self.direction == 270 or (not self.can_turn)):
            return
        self.head.setheading(90)
        self.direction = self.head.heading()
        self.can_turn = False

    def headDown(self):
        if self.SG and (self.direction == 90 or (not self.can_turn)):
            return
        self.head.setheading(270)
        self.direction = self.head.heading()
        self.can_turn = False

    def extend(self, number=1, clear=None):
        for i in range(number):
            self.segments.append(Turtle("circle"))
            newSegment = self.segments[len(self.segments) - 1]
            newSegment.penup()
            last = self.segments[len(self.segments) - 2]
            newSegment.goto(last.pos())
            if last == self.head:
                newSegment.setheading((self.head.heading() + 180) % 360)
            else:
                newSegment.setheading(self.segments[len(self.segments) - 3].towards(last))
            newSegment.forward(10)
            newSegment.color(self.display[(len(self.segments) - 1) % len(self.display)])
        if clear is None:
            return
        clear = list(clear)
        segments = self.segments
        segments.reverse()
        self.head = None
        self.segments = []
        for segment in segments:
            self.segments.append(segment.clone())
        self.segments.reverse()
        self.head = self.segments[0]
        self.clear_idle_segments(clear[0], clear[1])

    def turn(self, degrees):
        self.direction = (self.direction + degrees) % 360
        self.head.setheading(self.direction)

    def move(self, direction, speed):
        self.head.setheading(direction)
        self.direction = direction
        for i in range(len(self.segments) - 1, 0, -1):
            other = self.segments[i - 1]
            self.segments[i].goto(other.pos())
            self.segments[i].color(self.display[i % len(self.display)])
        self.head.forward(speed)
