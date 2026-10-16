import tkinter as tk
from tkinter import messagebox

def counter_app():
    win = tk.Tk()
    win.title("Counter App")
    win.geometry("250x180")

    count = tk.IntVar(value=0)

    tk.Label(win, textvariable=count, font=("Arial", 32)).pack(pady=10)

    frame = tk.Frame(win)
    frame.pack()
    tk.Button(frame, text="Increase", command=lambda: count.set(count.get() + 1)).grid(row=0, column=0, padx=5)
    tk.Button(frame, text="Decrease", command=lambda: count.set(count.get() - 1)).grid(row=0, column=1, padx=5)

    tk.Button(win, text="Reset", command=lambda: count.set(0)).pack(pady=10)

    win.mainloop()
    
counter_app()