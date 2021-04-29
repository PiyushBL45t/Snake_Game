# importing the important modules in the program
# the main modules is turtle asit specifically used for making small games

import turtle
import time
import random

delay = 0.1

#score
score=0
high_score=0


#set up the screen
win=turtle.Screen()
win.title("Snake game by Piyush Bhujbal")
win.bgcolor("blue")
win.setup(width=700, height=700)
win.tracer(0) #turns off the screen updates

#snake head
head=turtle.Turtle()   # Turtle head
head.speed(0)          #defining the speed variable
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)         #takes the head to the center point of the screen
head.direction="stop"  

#snake food
food=turtle.Turtle()
food.speed(0)          #defining the speed variable
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,200)         #takes the head to the center point of the screen

  

segments=[]

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,290)
pen.write("Score:0 High score:0", align="center", font=("Courier",24,"normal"))


#functions of the snake

def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"
        

def go_left():
    if head.direction!="right":
        head.direction="left"

def go_right():
    if head.direction!="left":
        head.direction="right"
    
    
def move():
    if head.direction=="up":
        y=head.ycor()    # y co-ordinates of the snake
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()    # x co-ordinates of the snake
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        
#keyboard bindings
win.listen()
win.onkeypress(go_up,"8")
win.onkeypress(go_down,"2")
win.onkeypress(go_left,"4")
win.onkeypress(go_right,"6")
#main game loop
while True:
    win.update()
    # check for a collision with the border
    if head.xcor()>300 or head.xcor()<-300 or head.ycor()>300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        

    #check for a collision with the food
    if head.distance(food)<20:
        #Move the food to the random spot on the screen
        x=random.randint(-300,300)
        y=random.randint(-300,300)
        food.goto(x,y)
        
        # Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay=0.1
        

        # Increase the score
        score+=10

        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {} High Score: {} ".format(score,high_score), align="center", font=("Courier",24,"normal"))


    #Move the end segment  first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)


    #Move segment 0 to where the food is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


        
      
    move()

    # check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"


            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)


            #clear the segments list
            segments.clear()

            # Reset the score
            score=0
            
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score,high_score), align="center", font=("Courier",24,"normal"))
            


            
    time.sleep(delay)

    
win.mainloop()

