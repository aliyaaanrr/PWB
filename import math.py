import math
import turtle

def heart_x(t):
    return 16 * math.sin(t)**3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

screen = turtle.Screen()  
screen.bgcolor("black")
screen.title("Red Heart") 

t = turtle.Turtle()  
t.speed(2)  
t.pencolor("red")

scale_factor = 18 

for i in range(0, 628, 2):  
    t.goto(heart_x(i * 0.1) * scale_factor, heart_y(i * 0.1) * scale_factor)  
turtle.done()
