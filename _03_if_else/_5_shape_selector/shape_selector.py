import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    hi = turtle.Turtle()
    hi.hideturtle()
    # Ask the user what shape they want to draw and store it in a variable
    question = simpledialog.askstring(title="", prompt='What type of shape should I draw? Please just say the shape with no other words!')
    # Draw the shape requested by the user using if-elif-else statements
    if question == 'square' :
        for i in range(4):
            hi.forward(50)
            hi.right(90)
            hi.forward(50)
    if question == 'rectangle':
        for i in range(2):
            hi.forward(150)
            hi.right(90)
            hi.forward(30)
            hi.right(90)
    if question == 'diamond':
        for i in range(2):
            hi.right(45)
            hi.forward(80)
            hi.right(135)
            hi.forward(80)
    if question == 'triangle':
            hi.right(55)
            hi.forward(305)
            hi.right(125)
            hi.forward(350)
            hi.right(125)
            hi.forward(305)
    # Call the turtle.done() method

    turtle.done()