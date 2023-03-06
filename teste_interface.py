import tkinter as tk

# Create the main window
root = tk.Tk()
root.title('Example GUI')
root.geometry('300x200')

# Create a label
label = tk.Label(root, text='Hello World!')
label.pack()

# Create a button
button = tk.Button(root, text='Click Me!', command=root.quit)
button.pack()

# Start the main event loop
root.mainloop()
