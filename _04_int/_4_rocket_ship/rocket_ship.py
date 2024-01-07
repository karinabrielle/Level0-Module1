from tkinter import *

window_width = 800
window_height = 800
root = Tk()

if __name__ == '__main__':


    canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#000050")
    canvas.grid()


    # This code runs whenever the mouse is clicked on the window
    def mouse_pressed(event):
        # Draws a dark blue background
        canvas.create_rectangle(0, 0, window_width, window_height, fill="#000050")

        # x and y will be equal to the mouse pointer's x and y location
        x = event.x
        y = event.y

        print(x)
        print(y)


        # 406, 204
        # 257, 406
        # 529, 537
        # 537, 453
        # 188, 483



        # This defines the x and y coordinated of all three points
        # of a triangle
        points = [x, y, x - 50, y + 100, x + 50, y + 100]
        canvas.create_polygon(points, fill='gray', width=2) # draws triangle
        canvas.create_rectangle(x - 50, y + 100, x + 50, y + 200,  fill='gray')
        canvas.create_polygon(x - 48, y + 202, x - 109, y + 242, x - 98, y + 367, fill='red')
        canvas.create_polygon(x - 48, y + 202, x - 55, y + 205, x - 110, y + 330, x - 132, y + 248, fill='orange')
        canvas.create_polygon(x - 149, y + 202, x - 123, y + 333, x - 131, y + 249, fill='red')

        canvas.create_polygon(x - 48, y + 202, x - 55, y + 205, x - 110, y + 330, x - 132, y + 248, fill='orange')
        # 1. Add details to your rocket to make it look better. You can look at
        #    rocket.png for inspiration.
    
        # 2. Modify the locations of the shapes above so the rocket will be drawn
        #    where the mouse is clicked
    

# ====================== DO NOT MODIFY THE CODE BELOW ========================

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()
