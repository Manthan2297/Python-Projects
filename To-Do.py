import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def complete_task():
    try:
        task_index = listbox.curselection()[0]
        completed_task = listbox.get(task_index)
        listbox.delete(task_index)
        listbox.insert(task_index, completed_task + " (Completed)")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed!")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

title_label = tk.Label(root, text="To-Do List", font=("Arial", 18))
title_label.pack(pady=10)

listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 14))
listbox.pack(pady=10)

task_entry = tk.Entry(root, width=52, font=("Arial", 14))
task_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", width=15, font=("Arial", 14), command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=15, font=("Arial", 14), command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

complete_button = tk.Button(button_frame, text="Complete Task", width=15, font=("Arial", 14), command=complete_task)
complete_button.grid(row=0, column=2, padx=5)

root.mainloop()
