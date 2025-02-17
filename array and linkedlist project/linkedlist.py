import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def visualize_stack_linked_list(linked_list_stack, canvas_frame):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_title("Stack using Linked List", fontsize=16, color="darkgreen")

    G = nx.DiGraph()
    pos = {}

    # Create two nodes per element to represent the "Data" and "Next"
    for i, node in enumerate(linked_list_stack):
        G.add_node(f'Data_{i}', label=f'Data: {node}')  # Data node
        G.add_node(f'Next_{i}', label="Next")           # Next node
        pos[f'Data_{i}'] = (i * 2, 0)  # Data position
        pos[f'Next_{i}'] = (i * 2 + 1, 0)  # Next position

        if i > 0:
            # Connect the 'Next' of the previous node to the 'Data' of the current node
            G.add_edge(f'Next_{i-1}', f'Data_{i}')

    # Create the last connection to NULL
    if linked_list_stack:
        G.add_node("NULL", label="NULL")
        pos["NULL"] = (len(linked_list_stack) * 2, 0)
        G.add_edge(f'Next_{len(linked_list_stack)-1}', "NULL")

    nx.draw(G, pos, with_labels=False, node_color='#98FB98', node_size=2000, edge_color='black', ax=ax, arrows=True)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='black', ax=ax)

    plt.axis('off')

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def update_linked_list_visualization():
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    visualize_stack_linked_list(linked_list_stack, canvas_frame)

def push_linked_list():
    try:
        element = int(linked_list_push_entry.get())
        linked_list_stack.append(element)
        update_linked_list_visualization()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def pop_linked_list_by_index():
    try:
        index = int(linked_list_pop_index_entry.get())
        if 0 <= index < len(linked_list_stack):
            linked_list_stack.pop(index)
            update_linked_list_visualization()
        else:
            messagebox.showerror("Invalid Index", "Please enter a valid index within the range.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for index.")

def pop_last_element():
    if linked_list_stack:
        linked_list_stack.pop()
        update_linked_list_visualization()
    else:
        messagebox.showinfo("Empty Stack", "The stack is already empty.")

def pop_first_element():
    if linked_list_stack:
        linked_list_stack.pop(0)  # Remove the first element (head)
        update_linked_list_visualization()
    else:
        messagebox.showinfo("Empty Stack", "The stack is already empty.")

root = tk.Tk()
root.title("Linked List-based Stack Visualization")
root.config(bg="#f0f8ff")

heading_label = Label(root, text="Implementation of Stack using Linked List", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#000080")
heading_label.pack(pady=10)

linked_list_stack = []

# Push section
linked_list_push_label = Label(root, text="Push to Linked List-based Stack:", font=("Arial", 14), bg="#f0f8ff", fg="#32CD32")
linked_list_push_label.pack(pady=10)
linked_list_push_entry = Entry(root, width=25, font=("Arial", 14))
linked_list_push_entry.pack(pady=5)

push_linked_list_button = Button(root, text="Push to Linked List Stack", command=push_linked_list,
                                 bg="#4CAF50", fg="white", font=("Arial", 12), width=20, padx=10, pady=5, relief='flat')
push_linked_list_button.pack(pady=5)

# Pop by index section
linked_list_pop_index_label = Label(root, text="Enter index to pop element from Linked List:", font=("Arial", 14), bg="#f0f8ff", fg="#FF6347")
linked_list_pop_index_label.pack(pady=10)
linked_list_pop_index_entry = Entry(root, width=25, font=("Arial", 14))
linked_list_pop_index_entry.pack(pady=5)

pop_linked_list_by_index_button = Button(root, text="Pop by Index", command=pop_linked_list_by_index,
                                         bg="#FF4500", fg="white", font=("Arial", 12), width=20, padx=10, pady=5, relief='flat')
pop_linked_list_by_index_button.pack(pady=5)

# Pop last element button
pop_last_button = Button(root, text="Pop Last Element", command=pop_last_element,
                         bg="#FF4500", fg="white", font=("Arial", 12), width=20, padx=10, pady=5, relief='flat')
pop_last_button.pack(pady=5)

# Pop first element button
pop_first_button = Button(root, text="Pop First Element", command=pop_first_element,
                          bg="#FF4500", fg="white", font=("Arial", 12), width=20, padx=10, pady=5, relief='flat')
pop_first_button.pack(pady=5)

canvas_frame = tk.Frame(root, bg="#f0f8ff")
canvas_frame.pack(pady=20)

root.mainloop()
