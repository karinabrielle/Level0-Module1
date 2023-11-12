from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

if __name__ == '__main__':


# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
    messagebox.showinfo(title='', message='You have a tomato...')
    x = simpledialog.askstring(title='', prompt='What color do you want your tomato to be?')
    a = simpledialog.askstring(title='', prompt='Is there another color you want your tomato to be?')
    if a == 'yes':
        y = simpledialog.askstring(title='', prompt='What other color do you want your tomato to be?'
                                                  
'(remember to think of all the colors in a tomato, even the colors in the stem!)')
        b = simpledialog.askstring(title='', prompt='Is there one more color you want your tomato to be?')
        if b == 'yes':
            z = simpledialog.askstring(title='', prompt='What is one more color you want your tomato to be?')
    else : messagebox.showinfo(title='',message="Let's start with our tomato!")
# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
    if a == 'no':
        canvas.create_rectangle(275, 100, 300, 350, fill= x, outline="")
        canvas.create_oval(75, 200, 400, 450, fill= x, outline="")
        canvas.create_oval(200, 200, 525, 450, fill= x, outline="")
    if a == 'yes':
        if b == 'no':
            canvas.create_rectangle(275, 100, 300, 250, fill=y, outline="")
            canvas.create_oval(75, 200, 400, 450, fill=x, outline="")
            canvas.create_oval(200, 200, 525, 450, fill=x, outline="")
    if a == 'yes':
        if b == 'yes':
            canvas.create_rectangle(275, 100, 300, 250, fill=y, outline="")
            canvas.create_oval(75, 200, 400, 450, fill=x, outline="")
            canvas.create_oval(200, 200, 525, 450, fill=z, outline="")



root.mainloop()
