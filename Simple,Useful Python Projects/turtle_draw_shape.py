import turtle  # used to draw
import math

class Draw():
	def __init__(self,height,width):
		print "Called __init__"
		self.height=height
		self.width=width
		
	def draw_square(self):
		print "Called draw square"
		#Parent.__init__(self,height)
		window=turtle.Screen()
		window.bgcolor("red")  # Create a red colored background
			
		brad=turtle.Turtle() #grabs the turtle and names it brad
		brad.shape("turtle")
		brad.color("yellow")
		brad.speed(2)
	
		for i in range(1,5):
			brad.forward(self.height)  # brad moves forward and draws for 100 units
			brad.right(90) #brad makes a 90 degree turn

square = Draw(100,50).draw_square()

		

#def draw_art():
#	window=turtle.Screen()
#	window.bgcolor("red")  # Create a red colored background
			
#	brad=turtle.Turtle() #grabs the turtle and names it brad
#	brad.shape("turtle")
#	brad.color("yellow")
#	brad.speed(2)
#	for i in range(1,37):
#		draw_square(brad)
#		brad.right(10)
	
#	angie=turtle.Turtle()
#	angie.color("blue")
#	angie.shape("arrow")
#	angie.circle(100)
	
#	joe=turtle.Turtle()
#	joe.color("green")
#	joe.shape("turtle")
#	joe.speed(2)
#	joe.forward(100)
#	joe.right(135)
#	joe.forward(math.sqrt(20000))
#	joe.right(135)
#	joe.forward(100)
	
#	window.exitonclick()
	
#draw_art()