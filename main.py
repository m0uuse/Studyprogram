import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Study App - Prototype")
root.geometry("400x250")

# Title label
title_label = ttk.Label(root, text="Concept Study App", font=("Segoe UI", 16))
title_label.pack(pady=10)

# Description text
desc_label = ttk.Label(root, text="Select a topic to begin:")
desc_label.pack(pady=5)

# Dropdown selector
topics = ["Math", "Science", "History", "Programming"]
selected_topic = tk.StringVar()

dropdown = ttk.Combobox(root, textvariable=selected_topic, values=topics, state="readonly")
dropdown.pack(pady=5)

dropdown.set("Choose a topic...")

# Placeholder button
def on_select():
    print("Selected topic:", selected_topic.get())

start_button = ttk.Button(root, text="Start", command=on_select)
start_button.pack(pady=15)

# Run app
root.mainloop()