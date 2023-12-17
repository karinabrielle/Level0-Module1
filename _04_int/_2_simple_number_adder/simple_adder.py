import turtle
from tkinter import messagebox, simpledialog, Tk

"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

if __name__ == '__main__':

    messagebox.showinfo(message='This is your new calculator for today!')
    messagebox.showinfo(message='type any two numbers and I will add them!')
    messagebox.showinfo(message='for example :')
    messagebox.showinfo(message='1, 1')
    messagebox.showinfo(message='Another example is :')
    messagebox.showinfo(message='53, 7')
    messagebox.showinfo(message="Now it's your turn!")
    a = simpledialog.askinteger(title="", prompt='type a random number!')
    b = simpledialog.askinteger(title="",prompt='type another random number!')
    messagebox.showinfo(message="The sum of the two numbers is...")
    messagebox.showinfo(message= str((a + b)) + "!!!")















































































