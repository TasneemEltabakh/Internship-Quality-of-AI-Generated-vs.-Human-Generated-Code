# Python program to add padding
# to a widget only on left-side

# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Give title to your GUI app
app.title("Vinayak App")

# Maximize the window screen
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry("%dx%d" % (width, height))

# Construct the label in your app
l1 = Label(app, text='Geeks For Geeks')

# Give the leftmost padding
l1.grid(padx=(200, 0), pady=(0, 0))

# Make the loop for displaying app
app.mainloop()