import turtle
from tkinter import messagebox, simpledialog, Tk, Canvas
import math
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# Iif they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
if __name__ == '__main__':
    hi = Tk()
    c = Canvas()
    hi.withdraw()
    k = simpledialog.askstring(title="", prompt="What is a random radius of a circle?...")
    question = simpledialog.askstring(title="", prompt="What would you like to calculate more, area, or circumference of a circle?")
    if question == "area" :
        c.create_oval(50, 50, int(k), int(k))
        a = math.pi * int(k) * int(k)
       # hi.write(arg = a, align= "left", font= "arial")
        messagebox.showinfo(title="", message="Area = " + str(a))
    if question == "circumference" :
        c.create_oval(50, 50, int(k), int(k))
        v = math.pi * int(k) * 2
        messagebox.showinfo(title="", message="Circumference = " + str(v))
# Area = πr^2
# Circumference = 2πr

































































































































