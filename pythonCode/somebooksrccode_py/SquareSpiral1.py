# SquareSpiral1.py - Draws a square spiral
import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "orange"]

for x in range(100):
    t.pencolor(colors[x%4])
    turtle.bgcolor(colors[3-x%4])
    t.forward(x)
    t.right(91)
    
