from ball import Ball
from time import sleep
from turtle import Screen
from shapes import Rectangle
from extra_modules import Writer, Button, move, KeyHandler, bool_to_num

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=600)
def start(players):
    def func(_arg1=None, _arg2=None, _arg3=None):
        paddles = [Rectangle(-350, 0, 20, 100), Rectangle(350, 0, 20, 100)]
        screen.tracer(False)
        handler = KeyHandler(screen)
        if players is 2:
            handler.addkey('W', move(paddles[0], 0, 1, y_min=-250, y_max=250))
            handler.addkey('w', move(paddles[0], 0, 1, y_min=-250, y_max=250))
            handler.addkey('S', move(paddles[0], 0, -1, y_min=-250, y_max=250))
            handler.addkey('s', move(paddles[0], 0, -1, y_min=-250, y_max=250))
        handler.addkey('Up', move(paddles[1], 0, 1, y_min=-250, y_max=250))
        handler.addkey('Down', move(paddles[1], 0, -1, y_min=-250, y_max=250))
        scores = [0, 0]
        ball = Ball()
        writer = Writer()
        for y in range(280, -280, -16):
            writer.writetext('l', x=0, y=y, size=8, color="white")
        writer.writetext('l', x=0, y=-280, size=8, color="white")
        writer = Writer()
        writer.writetext(scores[0], x=-50, y=200, size=50, color="white")
        writer.writetext(scores[1], x=50, y=200, size=50, color="white")
        while True:
            ball.ball_logic(screen, paddles)
            if abs(ball.xcor()) >= 390:
                result = bool_to_num(ball.xcor() >= 390) - bool_to_num(ball.xcor() <= -390)
                result = result + bool_to_num(result is -1)
                scores[abs(result - 1)] += 1
                ball.reset()
                writer.clear()
                writer.writetext(scores[0], x=-50, y=200, size=50, color="white")
                writer.writetext(scores[1], x=50, y=200, size=50, color="white")

            if players is 1:
                move(paddles[0], 0, ball.ycor() - paddles[0].ycor(), y_min=-250, y_max=250)()
            handler.run()
            screen.update()
            sleep(0.0005)
    return func

# Button((-100, 0), 50, 20, '1 player', start(1))
# Button((100, 0), 50, 20, '2 players', start(2))
start(2)()
