# import tkinter
from tkinter import *

# Create Tk object
window = Tk()

# Set the window title
window.title('GFG')

# Create a Frame for border
border_color = Frame(window, background="red")

# Label Widget inside the Frame
label = Label(border_color, text="This is a Label widget", bd=0)

# Place the widgets with border Frame
label.pack(padx=1, pady=1)
border_color.pack(padx=40, pady=40)

window.mainloop()