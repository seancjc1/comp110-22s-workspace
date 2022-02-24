"""Exercise 04 for COMP110 - Turtle Scene: The scene depicts a car driving down a road on a sunny summer day."""

__author__ = "730358979"

from turtle import Turtle, colormode, done, tracer, update

MAX_SPEED: int = 0
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    bob_ross: Turtle = Turtle()
    bob_ross.color(236, 0, 14)
    bob_ross.ht()
    bob_ross.speed(MAX_SPEED)
    bob_ross.begin_fill()
    draw_car(bob_ross, -141.0, 60.0)
    bob_ross.end_fill()
    update()
    done()


def draw_car(turtle: Turtle, x: float, y: float) -> None:
    """Draws the car at the center of the scene."""
    go_to(turtle, x, y)
    draw_rectangle(turtle, -141.0, 60.0, 300.0, 150.0)
    draw_rectangle(turtle, -105.0, 90.0, 150.0, 75.0)
    

def draw_rectangle(turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws a rectangle of a given width and length whose top-left corner is at x, y."""
    go_to(turtle, x, y)
    i: int = 0
    while i < 2:
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        i += 1


def draw_square(turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draws a square of a given width whose bottom-left corner is at x, y."""
    go_to(turtle, x, y)
    i: int = 0
    while i < 4:
        turtle.forward(width)
        turtle.right(90)
        i += 1


def draw_squiggly(turtle: Turtle, x: float, y: float, segments: int, segment_length: float) -> None:
    """Draws a squiggly line with given segments of specified length."""
    go_to(turtle, x, y)
    i: int = 0
    while i < segments:
        turtle.forward(segment_length)
        turtle.right(70)
        turtle.forward(segment_length / 10)
        i += 1


def go_to(turtle: Turtle, x: float, y: float) -> None:
    """Moves turtle to desired x, y coordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown


if __name__ == "__main__":
    main()