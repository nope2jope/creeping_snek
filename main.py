from turtle import Screen
from snek import Snek
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("jope's wicked snek")
screen.tracer(0)

snek = Snek()
nib = Food()
board = Scoreboard()

screen.listen()
screen.onkey(fun=snek.up, key="Up")
screen.onkey(fun=snek.down, key="Down")
screen.onkey(fun=snek.lefty, key="Left")
screen.onkey(fun=snek.righty, key="Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snek.move()

    # detect collision w/ food
    if snek.head.distance(nib) < 15:
        nib.new_fud()
        snek.lengthen()
        board.plus_one()

    # detect collision w/ wall
    if snek.head.xcor() > 300 or snek.head.xcor() < -300 or snek.head.ycor() > 300 or snek.head.ycor() < -300:
        board.reset_board()
        snek.reset_snek()

    # detect collision with tail
    for seg in snek.segments[1:]:
        if snek.head.position() == seg.position():
            board.reset_board()
            snek.reset_snek()

screen.exitonclick()
