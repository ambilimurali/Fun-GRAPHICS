""" Love message """
import time
import random
from turtle import *
from turtle import Screen, Turtle, shapesize

screen = Screen()
screen.title("Stickman and Stick Girl")
screen.bgcolor("pink")

stickman = Turtle()
stickman.speed(1)


def draw_stickman():
    """Function to draw a stickman"""
    stickman.penup()
    stickman.goto(-140, -50)
    stickman.pendown()
    stickman.circle(20)

    stickman.penup()
    stickman.goto(-140, -50)
    stickman.pendown()
    stickman.goto(-140, -100)

    stickman.penup()
    stickman.goto(-140, -70)
    stickman.pendown()
    stickman.goto(-170, -90)
    stickman.penup()
    stickman.goto(-140, -70)
    stickman.pendown()
    stickman.goto(-110, -90)

    stickman.penup()
    stickman.goto(-140, -100) 
    stickman.pendown()
    stickman.goto(-170, -150)  
    stickman.penup()
    stickman.goto(-140, -100)
    stickman.pendown()
    stickman.goto(-110, -150) 


def draw_computer():
    """Function to draw a computer"""

    stickman.penup()
    stickman.goto(-90, -30)
    stickman.pendown()
    stickman.fillcolor("grey")
    stickman.begin_fill()
    stickman.goto(0, -30) 
    stickman.goto(0, -90) 
    stickman.goto(-90, -90) 
    stickman.goto(-90, -30)
    stickman.end_fill()

    stickman.penup()
    stickman.goto(-50, -90)
    stickman.pendown()
    stickman.goto(-50, -100)
    stickman.goto(-50, -105)
    stickman.goto(-40, -105)
    stickman.goto(-40, -100)
    stickman.goto(-40, -90)


def draw_envelope():
    stickman.penup()
    stickman.goto(-60, -40)
    stickman.pendown()
    stickman.fillcolor("white")
    stickman.begin_fill()
    stickman.goto(-20, -40)
    stickman.goto(-20, -60)
    stickman.goto(-60, -60)
    stickman.goto(-60, -40)
    stickman.end_fill()
    
    stickman.penup()
    stickman.goto(-60, -40)
    stickman.pendown()
    stickman.goto(-40, -50)
    stickman.goto(-20, -40)

def draw_office():
    stickman.penup()
    stickman.goto(-190, -105)
    stickman.pendown()
    stickman.fillcolor("brown")
    stickman.begin_fill()
    stickman.goto(0, -105)
    stickman.goto(0, -130)
    stickman.goto(-190, -130)
    stickman.goto(-190, -105)
    stickman.end_fill()
    
    stickman.penup()
    stickman.goto(-150, -130)
    stickman.pendown()
    stickman.fillcolor("brown")
    stickman.begin_fill()
    stickman.goto(-150, -150)
    stickman.goto(-130, -150)
    stickman.goto(-130, -130)
    stickman.goto(-150, -130)
    stickman.end_fill()

def draw_stickgirl():
    stickman.penup()
    stickman.goto(150, -50)
    stickman.pendown()
    stickman.circle(20)
    
    stickman.penup()
    stickman.goto(150, -50)
    stickman.pendown()
    stickman.goto(150, -100)
    
    stickman.penup()
    stickman.goto(150, -70)
    stickman.pendown()
    stickman.goto(180, -90)
    stickman.penup()
    stickman.goto(150, -70)
    stickman.pendown()
    stickman.goto(120, -90)
    
    stickman.penup()
    stickman.goto(150, -100)
    stickman.pendown()
    stickman.goto(180, -150)
    stickman.penup()
    stickman.goto(150, -100)
    stickman.pendown()
    stickman.goto(120, -150)
    stickman.penup()
    stickman.goto(120, -100)
    
    stickman.penup()
    stickman.goto(120, -100)
    stickman.pendown()
    stickman.fillcolor("silver")
    stickman.begin_fill()
    stickman.goto(110, -100)
    stickman.goto(110, -80)
    stickman.goto(120, -80)
    stickman.goto(120, -100)
    stickman.end_fill()

def draw_heart(x, y, fill='pink', size=1):
    stickman.penup()
    stickman.goto(x, y)
    stickman.pendown()

    scale = size
    
    stickman.fillcolor(fill)
    stickman.begin_fill()
    stickman.left(50)
    stickman.forward(30 * scale)
    stickman.circle(10 * scale, 180)
    stickman.left(260)
    stickman.circle(10 * scale, 180)
    stickman.forward(30 * scale)
    stickman.end_fill()



def draw_stickboy():
    stickman.penup()
    stickman.goto(200, 90)
    stickman.pendown()
    stickman.circle(7)
    
    stickman.penup()
    stickman.goto(200, 90)
    stickman.pendown()
    stickman.goto(200, 60)
    
    stickman.penup()
    stickman.goto(200, 85)
    stickman.pendown()
    stickman.goto(190, 70)
    stickman.penup()
    stickman.goto(200, 85)
    stickman.pendown()
    stickman.goto(210, 70)
    
    stickman.penup()
    stickman.goto(200, 65)
    stickman.pendown()
    stickman.goto(190, 50)
    stickman.penup()
    stickman.goto(200, 65)
    stickman.pendown()
    stickman.goto(210, 50)

def draw_thought_bubble():
    stickman.penup()
    stickman.goto(150, 0)
    stickman.pendown()
    stickman.circle(10)
    stickman.penup()
    stickman.goto(170, 20)
    stickman.pendown()
    stickman.circle(20)
    stickman.penup()
    stickman.goto(200, 50)
    stickman.pendown()
    stickman.circle(30)

def animate_love_letter():
    letter = Turtle()
    letter.shape("square")
    letter.shapesize(stretch_wid=0.5, stretch_len=1)
    letter.fillcolor("red")
    letter.penup()
    letter.goto(-60, -40)
    destination_x = 110
    destination_y = -70
    
    while letter.distance(destination_x, destination_y) > 4:
        letter.setheading(letter.towards(destination_x, destination_y))
        letter.forward(4)
        time.sleep(0.05)



draw_stickman()
draw_computer()
draw_office()
draw_stickgirl()

draw_thought_bubble()
draw_stickboy()
draw_envelope()

animate_love_letter()

stickman.speed(0) 
num_hearts = 50

for _ in range(num_hearts):
    x = random.randint(-300, 300)
    y = random.randint(0, 400)
    size = random.uniform(0.5, 1.5)

    draw_heart(x, y, "red", size=size)

stickman.hideturtle()
done()
