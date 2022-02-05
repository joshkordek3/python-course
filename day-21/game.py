# import os
import tkinter
from food import Food
from time import sleep
from circleSnake import Snake
from random_place import random
from extra_modules import Writer
from turtle import Screen, done as donotexit

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

def xy(x, y):
    return {"x": x, "y": y}

def is_on_screen(ascreen, position, borders=False):
    half = {
        "width": ascreen.window_width() * 0.5,
        "height": ascreen.window_height() * 0.5
    }
    cond = borders * 20
    return abs(position["x"]) < (half["width"] - cond) and abs(position["y"]) < (half["height"] - cond)

def random_on_screen(ascreen):
    half = {
        "width": round(ascreen.window_width() * 0.5),
        "height": round(ascreen.window_height() * 0.5)
    }
    rand = random(
        xy(
            (half["width"] - 20) * -1,
            (half["height"] - 20) * -1
        ),
        xy(
            half["width"] - 20,
            half["height"] - 20
        ),
        xy(
            snake.head.xcor(),
            snake.head.ycor()
        ),
        False
    )
    return rand["x"], rand["y"]

screen = Screen()
screenDetails = tkinter.Tk()

screen.setup(width=screenDetails.winfo_screenwidth() - 6, height=screenDetails.winfo_screenheight() - 64)
screenDetails.withdraw()

screen.title("Python snake game")
screen.bgcolor("black")
screen.tracer(0)

food = Food()
writer = Writer(0, screen.window_height() * 0.5 - 40)

snake = Snake(10, ["blue", "purple"], "#aaa")  # Snake(3, ["white"], "#ddd")
snake.SG = True
food.goto(random_on_screen(screen))

screen.listen()
screen.onkey(snake.headUp, "w")
screen.onkey(snake.headLeft, "a")
screen.onkey(snake.headDown, "s")
screen.onkey(snake.headRight, "d")
screen.onkey(snake.headUp, "W")
screen.onkey(snake.headLeft, "A")
screen.onkey(snake.headDown, "S")
screen.onkey(snake.headRight, "D")

score = 0
while True:
    if not food.isvisible():
        food.reset()
        food.hideturtle()
        food = Food(random_on_screen(screen))
    if not is_on_screen(screen, {"x": food.xcor(), "y": food.ycor()}, True):
        food.goto(random_on_screen(screen))
    sleep(0.05)
    snake.move(snake.direction, 10)
    if food.collides(snake.head):
        snake.extend()  # clear=(screen, [food, writer])
        score += 1
        food.goto(random_on_screen(screen))
    writer.clear()
    writer.writetext(f"Score: {score}", "Calibri", 24, "bold", "white", 0, screen.window_height() * 0.5 - 40)
    if snake.collideswith(snake.segments):
        snake.gameover()
        break
    try:
        if abs(snake.head.xcor()) > screen.window_width() / 2 or abs(snake.head.ycor()) > screen.window_height() / 2:
            snake.gameover()
            break
        screen.update()
    except:
        break
    snake.can_turn = True
print(f"\n\nGAME OVER, final score: {score}\n\n")
try:
    donotexit()
except:
    pass
