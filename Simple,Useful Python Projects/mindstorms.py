import turtle  # used to draw
import math


def draw_square(some_turtle):	
	for i in range(1,5):
		some_turtle.forward(100)  # brad moves forward and draws for 100 units
		some_turtle.right(90) #brad makes a 90 degree turn
		
		
def draw_art():
	window=turtle.Screen()
	window.bgcolor("red")  # Create a red colored background
			
	brad=turtle.Turtle() #grabs the turtle and names it brad
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)
	
	angie=turtle.Turtle()
	angie.color("blue")
	angie.shape("arrow")
	angie.circle(100)
	
	joe=turtle.Turtle()
	joe.color("green")
	joe.shape("turtle")
	joe.speed(2)
	joe.forward(100)
	joe.right(135)
	joe.forward(math.sqrt(20000))
	joe.right(135)
	joe.forward(100)
	
	window.exitonclick()
	
	
draw_art()