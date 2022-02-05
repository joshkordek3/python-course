from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x=0, y=0, color="white"):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.shape('circle')
        self.x_vel = 1
        self.y_vel = 1
        self.def_x = x
        self.def_y = y

    def new_round(self):
        self.goto(self.def_x, self.def_y)
        self.x_vel = self.x_vel * -1
        self.y_vel = 1

    def touching(self, paddles):
        dist = 20
        return (abs(paddles[0].xcor() - self.xcor()) <= dist and self.distance(paddles[0]) <= 50) \
                or (abs(paddles[1].xcor() - self.xcor()) <= dist and self.distance(paddles[1]) <= 50)

    def ball_logic(self, screen, paddles):
        self.goto(self.xcor() + self.x_vel, self.ycor() + self.y_vel)
        if abs(self.ycor()) >= 290:
            self.y_vel = self.y_vel * -1
        if self.touching(paddles):
            self.x_vel = self.x_vel * -1
            while self.touching(paddles):
                self.goto(self.xcor() + self.x_vel, self.ycor() + self.y_vel)
                if abs(self.ycor()) >= 290:
                    self.y_vel = self.y_vel * -1
