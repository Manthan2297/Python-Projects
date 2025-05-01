import tkinter as tk

def button_click(row, col):
    if board[row][col] == "":
        board[row][col] = current_player.get()
        buttons[row][col].config(text=current_player.get())
        if check_winner():
            result_label.config(text=f"Player {current_player.get()} wins!")
            disable_buttons()
        else:
            toggle_player()

def toggle_player():
    current_player.set("O" if current_player.get() == "X" else "X")

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [["" for _ in range(3)] for _ in range(3)]
current_player = tk.StringVar(value="X")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=10, height=3, command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

result_label = tk.Label(root, text="Player X's turn", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
