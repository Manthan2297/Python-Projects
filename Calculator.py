import tkinter as tk

def calculator():
    def on_click(button_text):
        if button_text == "=":
            try:
                result = str(eval(entry.get()))
                entry.delete(0, tk.END)
                entry.insert(tk.END, result)
            except Exception as e:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")
        elif button_text == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, button_text)

    app_window = tk.Tk()
    app_window.title("Simple Calculator")

    entry = tk.Entry(app_window, width=20, font=("Arial", 20), borderwidth=5, relief="solid")
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "C", "0", "=", "+"
    ]

    row, col = 1, 0
    for button in buttons:
        tk.Button(app_window, text=button, width=5, height=2, font=("Arial", 18), command=lambda text=button: on_click(text)).grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

    app_window.mainloop()

if __name__ == "__main__":
    calculator()
