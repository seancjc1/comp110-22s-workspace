"""Demonstration of the turtle."""

__author__ = "730358979"

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(163, 17, 26)
leo.speed(50)
leo.hideturtle()
# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
leo.penup()
leo.goto(-150, -100)
leo.pendown()
i: int = 0
leo.begin_fill()
side_length: float = 300.0
while (i < 3): 
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()
bob: Turtle = Turtle()
bob.color(51, 10, 12)
bob.ht()
bob.penup()
bob.goto(-150, -100)
bob.pendown()
bob.speed(50)
idx: int = 0
while (idx < 100): 
    bob.forward(side_length)
    bob.left(121)
    side_length = side_length * 0.97
    idx += 1
done()
