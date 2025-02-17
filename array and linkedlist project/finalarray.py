import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def visualize_stack_array(stack_array, canvas_frame):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.set_title("Stack using Array", fontsize=16, color="darkblue")

    for i, element in enumerate(stack_array):
        rect = plt.Rectangle((i, 0), 1, 1, edgecolor='black', facecolor='#87CEEB')
        ax.add_patch(rect)
        ax.text(i + 0.5, 0.5, str(element), horizontalalignment='center', verticalalignment='center', fontsize=14)

    ax.set_xlim(0, max(5, len(stack_array)))
    ax.set_ylim(0, 1)
    plt.axis('off')

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


def update_array_visualization():
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    visualize_stack_array(stack_array, canvas_frame)


def push_array():
    max_size = int(max_size_entry.get())
    if len(stack_array) < max_size:
        try:
            element = int(array_push_entry.get())
            stack_array.append(element)
            update_array_visualization()
            overflow_label.config(text="")

            # Update the first element label when the first element is pushed
            if len(stack_array) == 1:
                first_element_label.config(text=f"First element of stack is {stack_array[0]}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
    else:
        overflow_label.config(text="Stack Overflow", fg="red")


def pop_array():
    if len(stack_array) > 0:
        stack_array.pop()  # Remove the last element
        update_array_visualization()
        overflow_label.config(text="")

        # Reset first element label if stack becomes empty
        if len(stack_array) == 0:
            first_element_label.config(text="")
    else:
        overflow_label.config(text="Stack Underflow", fg="red")


root = tk.Tk()
root.title("Array-based Stack Visualization")
root.config(bg="#f0f8ff")

stack_array = []


heading_label = Label(root, text="Implementation of Stack using Array", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#000080")
heading_label.pack(pady=10)


max_size_label = Label(root, text="Enter Array Size:", font=("Arial", 14), bg="#f0f8ff", fg="#4682b4")
max_size_label.pack(pady=5)
max_size_entry = Entry(root, width=25, font=("Arial", 14))
max_size_entry.pack(pady=5)

array_push_label = Label(root, text="Push to Array-based Stack:", font=("Arial", 14), bg="#f0f8ff", fg="#4682b4")
array_push_label.pack(pady=5)

array_push_entry = Entry(root, width=25, font=("Arial", 14))
array_push_entry.pack(pady=5)

push_array_button = Button(root, text="Push to Array Stack", command=push_array,
                           bg="#4F81BD", fg="white", font=("Arial", 12), width=20, padx=10, pady=5, relief='flat')
push_array_button.pack(pady=5)


# Removed the index entry and label for popping from a specific index
pop_button = Button(root, text="Pop from Array Stack", command=pop_array,
                    bg="#4F81BD", fg="white", font=("Arial", 12), width=20, padx=10, pady=5, relief='flat')
pop_button.pack(pady=5)


overflow_label = Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f8ff")
overflow_label.pack(pady=5)

# First element label on the left side of the page
first_element_label = Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="green")
first_element_label.pack(side=tk.LEFT, padx=20, pady=5)

canvas_frame = tk.Frame(root, bg="#f0f8ff")
canvas_frame.pack(pady=20)

root.mainloop()
