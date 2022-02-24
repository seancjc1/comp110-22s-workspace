from turtle import Turtle, colormode, done
colormode(255)
bob_ross: Turtle = Turtle()
bob_ross.color(236, 0, 14)
bob_ross.ht()
bob_ross.speed(1)


# bob_ross.penup()
# bob_ross.goto(10.0, 20.0)
# bob_ross.pendown()
# i: int = 0
# while i < 2:
#     bob_ross.forward(100)
#     bob_ross.right(90)
#     bob_ross.forward(50)
#     bob_ross.right(90)

bob_ross.penup()
bob_ross.goto(10.0, 20.0)
bob_ross.pendown()
i: int = 0
while i < 5:
    bob_ross.forward(50)
    bob_ross.right(70)
    bob_ross.forward(50 / 10)
    bob_ross.left(70)
    i += 1
done()