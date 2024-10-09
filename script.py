# script.py
import tkinter as tk

def run_tkinter_app():
    root = tk.Tk()
    root.title("Tkinter App")
    label = tk.Label(root, text="Hello from Tkinter!")
    label.pack(pady=20)
    button = tk.Button(root, text="Close", command=root.destroy)
    button.pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    run_tkinter_app()
