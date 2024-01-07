import turtle
from tkinter import messagebox, simpledialog, Tk
from tkinter import *

window_width = 800
window_height = 800
root = Tk()

if __name__ == '__main__':



    canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#000050")
    canvas.grid()

    canvas.create_rectangle(0, 0, window_width, window_height, fill="black")

    """
     * Write a python program that prints the word 'banana' one thousand (1,000) times
    """


    hi = turtle.Turtle

    messagebox.showinfo(title="" , message='This program will print the word "banana" one thousand times. Can you believe it?')
    messagebox.showinfo(title='', message="Don't worry, it's not actually going to print on actuall paper, it's going to print on the screen, the python way.")
    messagebox.showinfo(title='', message="GET READY, because it's going to print in... 10, 9, 8, 7, 6, 5, 4, 3, 2, 1!!!")

    hi.color("white")
    hi.write(arg="BANANAS", align="left", font="Arial", size= 90)



















