import tkinter.messagebox as messagebox
from tkinter import Tk, Button, Frame

# create the root window
root = Tk()

# set the window title
root.title("Tic Tac Toe")

# set the window size
root.geometry("300x300")

# set the window position
root.geometry("+0+0")

# create a frame to hold the buttons
button_frame = Frame(root)

# create the buttons
buttons = {}
for i in range(3):
    for j in range(3):
        button = Button(button_frame, width=10, height=5)
        button.grid(row=i, column=j)
        buttons[(i, j)] = button

# create a list to keep track of the moves
moves = ["", "", "", "", "", "", "", "", ""]

# create a function to check for a win
def check_win():
    for i in range(3):
        if moves[i*3] == moves[i*3+1] == moves[i*3+2] != "":
            return moves[i*3]
        if moves[i] == moves[i+3] == moves[i+6] != "":
            return moves[i]
    if moves[0] == moves[4] == moves[8] != "":
        return moves[0]
    if moves[2] == moves[4] == moves[6] != "":
        return moves[2]
    if "" not in moves:
        return "draw"
    return None

# create a function to handle button clicks
def button_click(row, col):
    global moves
    button = buttons[(row, col)]
    if button["text"] == "":
        button["text"] = "X" if len([m for m in moves if m != ""]) % 2 == 0 else "O"
        moves[row*3+col] = button["text"]
        winner = check_win()
        if winner:
            if winner == "draw":
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"{winner} wins!")
            root.destroy()

# add the button click handlers
for i in range(3):
    for j in range(3):
        button = buttons[(i, j)]
        button["command"] = lambda row=i, col=j: button_click(row, col)

# add the button frame to the window
button_frame.pack()

# start the main event loop
root.mainloop()
