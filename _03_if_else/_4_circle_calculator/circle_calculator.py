# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# Iif they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
if __name__ == '__main__':
    k = simpledialog.askstring(title = "", prompt = "What is a random radius of a circle?...")
   question = simpledialog.askstring(title = "", prompt = "What would you like to calculate more, area, or circumference of a circle?")
    if question == "area" :
        math.pi * k * k

#Area = πr^2
#Circumference = 2πr 