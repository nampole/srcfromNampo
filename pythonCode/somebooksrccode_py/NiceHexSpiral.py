'''
Created on 2022. 2. 24.

@author: isaiah
'''
import turtle
colors=['red','purple','blue','green','yellow','orange']
t=turtle.Pen()
#===============================================================================
turtle.bgcolor('black')
#===============================================================================
for x in range (360):
    t.pencolor(colors[x%6])
    t.width(x/100+3)
    t.forward(x)
    t.left(30)
