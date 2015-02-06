__author__ = 'GilbertAlipui'

from tkinter import * # Import all definitions from tkinter

#create a window
window = Tk() # Create a window
#create a label
label = Label(window, text = "Welcome to Python" ) # Create a label
#create a button
button = Button(window, text = "Click Me" ) # Create a button
#place label
label.pack() # Place the label in the window
#place button
button.pack() # Place the button in the window

#event loop
window.mainloop() # Create an event loop