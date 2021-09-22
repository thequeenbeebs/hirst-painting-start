import turtle

import colorgram
import random
from turtle import Turtle, Screen

rgb_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

tim = Turtle()
tim.hideturtle()
tim.speed('fastest')
turtle.colormode(255)
tim.penup()
tim.setx(-200)
tim.sety(-200)


def make_dot():
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)


def make_row():
    for _ in range(10):
        make_dot()


def turn_left():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50)


def turn_right():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    tim.forward(50)


for _ in range(5):
    make_row()
    turn_left()
    make_row()
    turn_right()



# 10 x 10 rows of spots
# dots are 20 in size
# spaces apart by 50 paces
# delete first three color in rgb colors


screen = Screen()
screen.exitonclick()