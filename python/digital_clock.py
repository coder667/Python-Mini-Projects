import tkinter as tk
from time import strftime

def time():
    # Get the current time
    current_time = strftime('%H:%M:%S %p')
    # Update the label with the current time
    clock_label.config(text=current_time)
    # Call the time() function after 1000 milliseconds (1 second)
    clock_label.after(1000, time)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Create and configure the label
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='sky blue', foreground='white')
clock_label.pack(anchor='center')

# Call the time() function to update the time display
time()

# Run the main loop
root.mainloop()
