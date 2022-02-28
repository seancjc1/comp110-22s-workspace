"""Exercise 04 for COMP110 - Turtle Scene: The scene depicts a car driving down a road on a sunny summer day."""

__author__ = "730358979"

from turtle import Turtle, colormode, done, tracer, update

MAX_SPEED: int = 0
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    bob_ross: Turtle = Turtle()
    bob_ross.ht()
    bob_ross.speed(MAX_SPEED)
    draw_car(bob_ross, -141.0, 60.0)
    draw_tree(bob_ross, -250, 150.0)
    draw_tree(bob_ross, 250, -100.0)
    draw_sun(bob_ross, 300, 300, 25)
    update()
    done()


def draw_car(turtle: Turtle, x: float, y: float) -> None:
    """Draws the car at the center of the scene."""
    go_to(turtle, x, y)
    draw_rectangle_car(turtle, -141.0, 60.0, 300.0, 140.0)
    draw_rectangle_car(turtle, -80.0, 120.0, 200.0, 100.0)
    draw_square_window(turtle, 30.0, 80.0, 50.0)
    draw_square_window(turtle, -50.0, 80.0, 50.0)
    draw_square_wheel(turtle, -90, -50, 60)
    draw_square_wheel(turtle, 70, -50, 60)


def draw_tree(turtle: Turtle, x: float, y: float) -> None:
    """Draws a tree for use in the scene."""
    go_to(turtle, x, y)
    turtle.begin_fill()
    draw_rectangle_tree(turtle, x, y, 50, 200)
    draw_square_tree(turtle, -275, 200, 100)
    draw_square_tree(turtle, 205, -100, 100)
    turtle.end_fill()


def draw_sun(turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws the sun at the top right of the scene."""
    go_to(turtle, x, y)
    turtle.color(248, 242, 80)
    draw_square_sun(turtle, 200, 220, 80)


def draw_rectangle_car(turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws a rectangle of a given width and length whose top-left corner is at x, y."""
    go_to(turtle, x, y)
    i: int = 0
    turtle.color(236, 0, 14)
    turtle.begin_fill()
    while i < 2:
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def draw_rectangle_tree(turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws a rectangle of a given width and length whose top-left corner is at x, y."""
    go_to(turtle, x, y)
    i: int = 0
    turtle.color(123, 91, 3)
    turtle.begin_fill()
    while i < 2:
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def draw_square_window(turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draws a square of a given width whose bottom-left corner is at x, y."""
    go_to(turtle, x, y)
    i: int = 0
    turtle.color(92, 213, 228)
    turtle.begin_fill()
    while i < 4:
        turtle.forward(width)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def draw_square_sun(turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draws a square of a given width whose bottom-left corner is at x, y."""
    go_to(turtle, x, y)
    i: int = 0
    turtle.color(248, 242, 80)
    turtle.begin_fill()
    while i < 4:
        turtle.forward(width)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def draw_square_wheel(turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draws a square of a given width whose bottom-left corner is at x, y."""
    go_to(turtle, x, y)
    i: int = 0
    turtle.color(0, 0, 0)
    turtle.begin_fill()
    while i < 4:
        turtle.forward(width)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def draw_square_tree(turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draws a square of a given width whose bottom-left corner is at x, y."""
    go_to(turtle, x, y)
    i: int = 0
    turtle.color(46, 123, 3)
    turtle.begin_fill()
    while i < 4:
        turtle.forward(width)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def go_to(turtle: Turtle, x: float, y: float) -> None:
    """Moves turtle to desired x, y coordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


if __name__ == "__main__":
    main()