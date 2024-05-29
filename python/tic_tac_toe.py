import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic_Tac_Toe")

# Game variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Function to check for a win or draw
def check_winner():
    for i in range(3):
        # Check rows and columns
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text']
    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']
    # Check for draw
    if all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
        return "Draw"
    return None

# Function to handle button click
def button_click(row, col):
    global current_player
    if buttons[row][col]['text'] == "" and current_player:
        buttons[row][col]['text'] = current_player
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""

# Create buttons
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", font=('normal', 40, 'bold'), width=5, height=2,
                           command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Run the main loop
root.mainloop()
