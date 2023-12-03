import turtle
from tkinter import messagebox, simpledialog, Tk


"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
if __name__ == '__main__':

    score = 0

    messagebox.showinfo(title="", message="You will be given a set of riddles to answer, and your score will be shown at the end. Good luck!")
    a = simpledialog.askstring(title="", prompt='Riddle #1 : What goes up and never goes down?')
    if a == 'your age' :
        score +=1
    else :
        score +=0
    b = simpledialog.askstring(title='', prompt= 'Riddle #2 : I am the beginning of the end, and the end of time and space. I am essential to creation, and I surround every place. What am I?')
    if b == 'the letter e' :
        score +=1
    else :
        score +=0
    c = simpledialog.askstring(title='', prompt= "Riddle #3 : David's father has three sons: Snap, Crackle, and _____?")
    if c == 'David' :
        score +=1
    d = simpledialog.askstring(title='', prompt= "Riddle #4 : What has a head, a tail, is brown, and has no legs?")
    if d == 'a penny' :
        score +=1
    e = simpledialog.askstring(title='', prompt='Riddle #5 : I start with the letter e, I end with the letter e. I contain only one letter, Yet I am not the letter e! What am I?')
    if e == 'an envelope' :
        score +=1
    if e == 'an Envelope' :
        score +=1
    f = simpledialog.askstring(title='', prompt='Riddle #6 : I am white when I am dirty, and black when I am clean. What am I?')
    if f == 'a blackboard' :
        score +=1
    g = simpledialog.askstring(title='', prompt='Riddle #7 : I make two people out of one. What am I?')
    if g == 'a mirror' :
        score +=1
    h = simpledialog.askstring(title='', prompt="Riddle #8 I'm tall when I'm young and I'm short when I'm old. What am I?")
    if h == 'a candle' :
        score +=1
    if h == 'a pencil' :
        score +=1
    i = simpledialog.askstring(title='', prompt='Riddle #9 What can you catch but never throw?')
    if i == 'a cold' :
        score +=1
    j = simpledialog.askstring(title='', prompt='Riddle #10 : Before Mount Everest was discovered, what was the highest mountain on Earth?')
    if j == 'Mount Everest' :
        score +=1
     if score == 10 :
         messagebox.showinfo(title='', message='Great job!!! Your score is... '+ score +'/10')
     if score > 5 :
         messagebox.showinfo(title='', message='Good job!!! Your score is... ' + score + '/10! Try to get a perfect score next time!')










