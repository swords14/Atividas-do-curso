import turtle

def draw_sun():
    window = turtle.Screen()
    window.bgcolor("yellow")

    sun = turtle.turtle()
    sun.shape("circle")
    sun.color("red")
    sun.speed(10)

    for i in range(36):
        sun.stamp()
        sun.right(10)

        window.exitonclick()

        draw_sun
