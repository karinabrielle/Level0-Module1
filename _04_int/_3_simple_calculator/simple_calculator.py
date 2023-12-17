import turtle
from tkinter import messagebox, simpledialog, Tk

"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
if __name__ == '__main__':

    messagebox.showinfo(message='This is your new calculator for today!')
    messagebox.showinfo(message='type any two numbers and I will add, subtract, multiply, or divide them!')
    messagebox.showinfo(message='for example :')
    messagebox.showinfo(message='1, 1')
    messagebox.showinfo(message='Another example is :')
    messagebox.showinfo(message='53, 7')
    a = simpledialog.askinteger(title="", prompt='Type a random number!')
    b = simpledialog.askinteger(title="", prompt='Type another random number!')
    messagebox.showinfo(message="Now, just tell me if you want to add, subtract, multiply or divide them!")
    messagebox.showinfo(message='for example :')
    messagebox.showinfo(message='Just type in "divide" if you want to divide any two numbers!')
    c = simpledialog.askstring(title="", prompt='type if you want to add, subtract, multiply or divide them!')
    if c == 'divide' :
        messagebox.showinfo(message="The quotient of the two numbers is...")
        messagebox.showinfo(message=str((a / b)) + "!!!")  if c == 'divide' :
     if c == 'multiply':
        messagebox.showinfo(message="The product of the two numbers is...")
        messagebox.showinfo(message=str((a * b)) + "!!!")
    if c == 'add':
        messagebox.showinfo(message="The sum of the two numbers is...")
        messagebox.showinfo(message= str((a + b)) + "!!!")
    if c == 'subtract':
        messagebox.showinfo(message="The difference of the two numbers is...")
        messagebox.showinfo(message= str((a - b)) + "!!!")























































