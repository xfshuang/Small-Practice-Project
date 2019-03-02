#Draw a snowman
#Written by: Shirley Huang
#Date: March 1, 2019

import turtle

def main():
    drawBase(0, -200, 100) #Base
    drawMidSection(0, 0, 75) #Middle Body
    drawHead(0, 150, 50) #Head
    drawHead(-20, 200, 5) #left eye
    drawHead(20, 200, 5) #right eye
    drawArm(-75,70, -200, 90) #left arm
    drawArm(75,70, 200, 70)#right arm
    drawHat(-50,230,100, 'black') #hat
    drawArm(-15, 160, 20, 170) #smile
    
    


def drawBase(x, y, radius=50):
    turtle.penup()             # Raise the pen
    turtle.setposition(x, y) # Position the turtle
    turtle.pendown()           # Lower the pen
    turtle.circle(radius)      # Draw a circle

def drawMidSection(x, y, radius=50):
    turtle.penup()             # Raise the pen
    turtle.setposition(x, y) # Position the turtle
    turtle.pendown()           # Lower the pen
    turtle.circle(radius)      # Draw a circle 

def drawArm(startX, startY, endX, endY):
    turtle.penup()              # Raise the pen
    turtle.goto(startX, startY) # Move to the starting point
    turtle.pendown()            # Lower the pen
    turtle.goto(endX, endY)

def drawHead(x, y, radius=50):
    turtle.penup()             # Raise the pen
    turtle.setposition(x, y) # Position the turtle
    turtle.pendown()           # Lower the pen
    turtle.circle(radius)      # Draw a circle

def drawHat(x, y, width, color):
    turtle.penup()            # Raise the pen
    turtle.goto(x, y)         # Move to the specified location
    turtle.fillcolor(color)   # Set the fill color
    turtle.pendown()          # Lower the pen
    turtle.begin_fill()       # Start filling
    for count in range(4):    # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # End filling
    

main()
