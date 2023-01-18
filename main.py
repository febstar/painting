# import colorgram
#
# # import download.jpg
# colours = colorgram.extract('download.jpg', 16)
# myset = []
# for i in colours:
#     myset.append(i.rgb)
#
# opgl = []
#
#
# def srz(issues):
#     r = issues.r
#     g = issues.g
#     b = issues.b
#
#     set_clr = (r, g, b)
#     return set_clr
#
# for i in myset:
#     opgl.append(srz(i))
#
# print(opgl)
import turtle
from turtle import Turtle, Screen
import random
febe = Turtle()
turtle.colormode(255)

color_list = [(28, 109, 184), (225, 61, 90), (224, 151, 90), (124, 153, 205), (215, 130, 162), (139, 89, 52), (38, 194, 107), (105, 108, 190), (140, 177, 27), (240, 155, 184), (186, 48, 80)]

febe.penup()
febe.setheading(229)
febe.forward(300)
febe.hideturtle()
febe.setheading(0)
def colour():
    for i in range(10):
        febe.dot(20, random.choice(color_list))
        febe.forward(50)

def reset():
    febe.setheading(90)
    febe.forward(50)
    febe.setheading(180)
    febe.forward(500)
    febe.setheading(0)

for i in range(10):
    colour()
    reset()

screen = Screen()
screen.exitonclick()