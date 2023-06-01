import tkinter as tk
from tkinter import ttk

def start_button_clicked():
    # Function to handle the button click event
    text = text_entry.get("1.0", tk.END)  # Get the text from the entry widget
    words = text.split()  # Split the text into individual words

    # Define the function to display words
    def display_word(index=0):
        if index < len(words):
            word_label.config(text=words[index])
            index += 1
            delay = int(delay_slider.get())
            word_label.after(delay, lambda: display_word(index))

    display_word()

# Create the main window
window = tk.Tk()
window.title("Word Display Program")
window.geometry("800x600")  # Set a default window size
window.configure(bg="#1e1e1e")  # Set background color

# Create a frame for the text entry section
entry_frame = tk.Frame(window, bg="#1e1e1e")
entry_frame.pack(pady=20)

# Create a label for the text entry
entry_label = tk.Label(entry_frame, text="Enter Text", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
entry_label.pack()

# Create a text entry widget
text_entry = tk.Text(entry_frame, height=10, width=40, bg="#ffffff", fg="#1e1e1e", bd=0)
text_entry.pack(pady=10)

# Create a frame for the controls section
controls_frame = tk.Frame(window, bg="#1e1e1e")
controls_frame.pack(pady=20)

# Create a label for the slider
slider_label = tk.Label(controls_frame, text="Speed", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
slider_label.pack(side=tk.LEFT, padx=(10, 5))

# Create a slider to control the display rate
delay_slider = ttk.Scale(controls_frame, from_=100, to=2000, length=200)
delay_slider.set(500)  # Set the initial delay value
delay_slider.pack(side=tk.LEFT)

# Create a start button
start_button = tk.Button(window, text="Start", font=("Arial", 12), bg="#e53935", fg="#ffffff", bd=0, padx=10, pady=5,
                         command=start_button_clicked)
start_button.pack()

# Create a frame for the word display section
display_frame = tk.Frame(window, bg="#1e1e1e")
display_frame.pack(pady=20)

# Create a label to display the word
word_label = tk.Label(display_frame, text="Display word here", font=("Arial", 24), bg="#ffffff", fg="#1e1e1e", bd=0, padx=10, pady=5)
word_label.pack()

# Start the main window's event loop
window.mainloop()
