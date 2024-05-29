import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List App")

# Create a frame for the list and the scrollbar
frame_tasks = tk.Frame(root)
frame_tasks.pack()

# Create a listbox to display tasks
listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50, selectmode=tk.SINGLE)
listbox_tasks.pack(side=tk.LEFT)

# Create a scrollbar for the listbox
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the listbox
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Function to add a task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to mark a task as completed
def mark_task_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} - Completed")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Create an entry widget for task input
entry_task = tk.Entry(root, width=50)
entry_task.pack()

# Create a frame for the buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack()

# Create buttons to add, delete, and mark tasks as completed
button_add_task = tk.Button(frame_buttons, text="Add Task", width=20, command=add_task)
button_add_task.pack(side=tk.LEFT)

button_delete_task = tk.Button(frame_buttons, text="Delete Task", width=20, command=delete_task)
button_delete_task.pack(side=tk.LEFT)

button_mark_task_completed = tk.Button(frame_buttons, text="Mark Completed", width=20, command=mark_task_completed)
button_mark_task_completed.pack(side=tk.LEFT)

# Run the main loop
root.mainloop()
