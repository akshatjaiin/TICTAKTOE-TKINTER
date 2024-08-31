import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return buttons[row][0]["text"]
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return buttons[0][col]["text"]
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]
    return None

def click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not winner:
        buttons[row][col]["text"] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, winner
    current_player = "X"
    winner = None
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""

app = tk.Tk()
app.title("Tic-Tac-Toe")

current_player = "X"
winner = None
buttons = [[None for _ in range(3)] for _ in range(3)]

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(app, text="", font=("Arial", 40), width=5, height=2,
                                  command=lambda r=r, c=c: click(r, c))
        buttons[r][c].grid(row=r, column=c)

reset_button = tk.Button(app, text="Reset", font=("Arial", 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

app.mainloop()
