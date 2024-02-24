import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import Calendar
from datetime import datetime
import time
import customtkinter as ctk
from customtkinter import CTkButton

class TaskManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Task Manager")
        self.geometry("500x500")
        self.configure(bg="black")
        self.resizable(False, False)
        self.iconbitmap("icon2.ico")


        self.tasks = []

        # Create and pack the widgets
        self.create_widgets()

    def create_widgets(self):
        # Customize button sty

        # Task Entry
        self.task_entry = tk.Entry(self, width=50, bg='black', fg='white', font=('Helvetica', 12))
        self.task_entry.pack(pady=10)

        # Buttons
        add_button = CTkButton(self, text="Add Task", command=self.add_task,hover_color="white",
                               fg_color="transparent", text_color="white", border_color="white",
                               border_width=3)
        add_button.pack(pady=5)

        remove_button = CTkButton(self, text="Remove Task", command=self.remove_task,hover_color="white",
                               fg_color="transparent", text_color="white", border_color="white",
                               border_width=3 )
        remove_button.pack(pady=5)


        clock_button = CTkButton(self, text="View Clock", command=self.view_clock,hover_color="white",
                               fg_color="transparent", text_color="white", border_color="white",
                               border_width=3)
        clock_button.pack(pady=5)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(self, width=100, height=100, bg='black', fg='white', font=('Helvetica', 12))
        self.tasks_listbox.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)  # Add task to the listbox
            messagebox.showinfo("Task Added", f"Task '{task}' added successfully.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        if self.tasks_listbox.curselection():
            selected_index = self.tasks_listbox.curselection()[0]
            selected_task = self.tasks.pop(selected_index)
            self.tasks_listbox.delete(selected_index)  # Remove task from the listbox
            messagebox.showinfo("Task Removed", f"Task '{selected_task}' removed successfully.")
        else:
            messagebox.showinfo("No Tasks", "No task selected to remove.")

    def view_clock(self):
        clock_window = tk.Toplevel(self)
        clock_window.title("Clock")
        clock_window.geometry("300x300")
        clock_label = tk.Label(clock_window, font=('sans', 30), background='black', foreground='white')
        clock_label.pack(anchor='center')
        self.update_clock(clock_label)

    def update_clock(self, label):
        tick = time.strftime("%H:%M:%S %p")
        label.config(text=tick)
        label.after(1000, lambda: self.update_clock(label))

if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()
