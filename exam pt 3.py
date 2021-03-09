import turtle #import the turtle library
 
turtle.Screen() # opens the turtle display terminal
drawTurtle = turtle.Turtle() # assigns turtle function to variable
 
for i in range(5): # loop for the 5 lines making the star design
        drawTurtle.forward(400) #draws a straight line
        drawTurtle.right(144) # rotates right to the correct angle needed for this design
        