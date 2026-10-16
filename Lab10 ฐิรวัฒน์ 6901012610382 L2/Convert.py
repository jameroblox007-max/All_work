import tkinter as tk
from tkinter import messagebox

def converter_app():
    win = tk.Tk()
    win.title("Celsius to Fahrenheit")
    win.geometry("300x180")

    tk.Label(win, text="Celsius:").pack(pady=(15, 0))
    entry = tk.Entry(win)
    entry.pack()

    result = tk.Label(win, text="", font=("Arial", 14))
    result.pack(pady=10)

    def convert():
        try:
            c = float(entry.get())
            result.config(text=f"{c * 9 / 5 + 32:.2f} °F")
        except ValueError:
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกตัวเลขเท่านั้น")

    tk.Button(win, text="Convert", command=convert).pack()

    win.mainloop()
    
converter_app()