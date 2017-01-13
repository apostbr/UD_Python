import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor ("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue", "green")

    z = 0
    while z < 36:
        brad.right(10)     
        i = 0
        while i < 4:
            brad.forward(100)
            brad.right(90)
            i = i + 1
        z = z + 1

#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("yellow")
#    angie.circle(100)

#   cola = turtle.Turtle()
#   cola.shape("arrow")
#    cola.color("brown")
#    cola.backward(100)
#    cola.left(90)
#    cola.backward(100)
#    cola.left(135)
#    cola.backward(142)
#    cola.left(120)

    window.exitonclick()

draw_shapes()
