import tkinter as tk

win = tk.Tk()
win.title("GUI Text Analyzer")
win.geometry("380x300")

tk.Label(win, text="ข้อความ:").pack(pady=(10, 0))
text_entry = tk.Entry(win, width=35)
text_entry.pack()

tk.Label(win, text="ตัวอักษรที่ต้องการนับ:").pack(pady=(10, 0))
char_entry = tk.Entry(win, width=5)
char_entry.pack()

result = tk.Label(win, text="", font=("Arial", 12), wraplength=340)
result.pack(pady=15)


def count_character():
    text = text_entry.get()
    ch = char_entry.get()
    if len(ch) != 1:
        result.config(text="กรุณากรอกตัวอักษรที่ต้องการนับ 1 ตัว")
        return
    n = text.lower().count(ch.lower())
    result.config(text=f'ตัวอักษร "{ch}" พบ {n} ตัว')


def count_vowels():
    text = text_entry.get().lower()
    n = sum(1 for c in text if c in "aeiou")
    result.config(text=f"จำนวนสระ (a, e, i, o, u) = {n} ตัว")


def check_palindrome():
    text = text_entry.get().lower().replace(" ", "")
    if text == "":
        result.config(text="กรุณากรอกข้อความ")
    elif text == text[::-1]:
        result.config(text="เป็น Palindrome")
    else:
        result.config(text="ไม่เป็น Palindrome")


tk.Button(win, text="Count Character", command=count_character).pack(pady=3)
tk.Button(win, text="Count Vowels", command=count_vowels).pack(pady=3)
tk.Button(win, text="Check Palindrome", command=check_palindrome).pack(pady=3)

win.mainloop()