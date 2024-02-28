from turtle import *

# The Cantor set
def cantor(x , y , length):
    speed(13)
    if length >= 5:
        penup()
        pensize(2)
        pencolor("blue")
        setpos(x , y)
        pendown()
        fd(length)
        y -= 80
        cantor(x , y , length / 5)
        cantor(x + 2 * length / 5 , y , length / 5)
        cantor(x + 4 * length / 5, y, length / 5)
        penup()
        setpos(x , y + 80)

#cantor(-400 , 200 , 500)


# The Koch Snowflake.
pensize(1)
penup()
setpos(-250 , 200)
pendown()

def KochSnowflake(length, level):
    speed(13) # Fastest speed.
    for i in range(4):
        plot_side(length, level)
        rt(90)
    
def plot_side(length, level):
    if level==0:
        fd(length)
        return
    plot_side(length/3, level-1)
    lt(90)
    plot_side(length/3, level-1)
    rt(90)
    plot_side(length/3, level-1)
    rt(90)
    plot_side(length/3, level-1)
    lt(90)
    plot_side(length/3, level-1)
    
#KochSnowflake(300 , 3)



# A bifurcating tree.
speed(13)
setheading(90)
penup()
setpos(-200 , -120)
pendown()

def FractalTreeColor(length, level):
    pensize(length /10) # Thickness of lines.
    if length < 20:
        pencolor("green")
    else:
        pencolor("brown")
    if level > 0:
        fd(length) # Forward
        rt(60) # Right turn 60 degrees
        FractalTreeColor(length*0.6, level-1)
        lt(90) # Left turn 90 degrees
        FractalTreeColor(length*0.4, level-1)
        rt(30) # Right turn 30 degrees
        FractalTreeColor(length*0.2, level-1)
        penup()
        bk(length) # Backward
        pendown()

#FractalTreeColor(200,8)


# Sierpinski Triangle.
speed(13)
penup()
setpos(-300 , -100)
pendown()
def SierpinskiTriangle(length, level):
    if level==0:
        return
    begin_fill() # Fill shape
    color("red")
    for i in range(3):
        SierpinskiTriangle(length/2, level-1)
        fd(length)
        lt(90) # Left turn 120 degrees
        end_fill()
SierpinskiTriangle(300 , 5)
