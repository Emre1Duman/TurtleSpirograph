from turtle import Turtle, Screen
import random


screen = Screen()
nina = Turtle()
nina.shape("turtle")
nina.speed(0)
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        nina.color(random_color())
        nina.circle(100)
        nina.setheading(nina.heading() + size_of_gap)

draw_spirograph(5)






    

screen.exitonclick()