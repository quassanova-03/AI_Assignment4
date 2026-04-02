# Sudoku Solver using CSP (with tinker for GUI)

import tkinter as tk

steps = 0

#Terminal print
def print_board(board):

    for i in range(9):
        if i % 3 == 0:
            print("+-------+-------+-------+")

        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")

            value = board[i][j] if board[i][j] != 0 else "."
            print(value, end=" ")

        print("|")

    print("+-------+-------+-------+")


def is_valid(board, row, col, num):

    for j in range(9):
        if board[row][j] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row, start_col = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True


def solve(board):
    global steps
    steps += 1

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):
                    if is_valid(board, row, col, num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True

# Tinker print
def display_sudoku_gui(board, original):

    root = tk.Tk()
    root.title("Sudoku Solver (CSP)")

    frame = tk.Frame(root)
    frame.pack()

    for i in range(9):
        for j in range(9):

            value = board[i][j]

            cell = tk.Frame(
                frame,
                width=50,
                height=50,
                highlightbackground="black",
                highlightthickness=1
            )

            if i % 3 == 0:
                cell.config(highlightthickness=2)
            if j % 3 == 0:
                cell.config(highlightthickness=2)

            cell.grid(row=i, column=j)

            color = "black" if original[i][j] != 0 else "blue"

            label = tk.Label(
                cell,
                text="" if value == 0 else str(value),
                font=("Arial", 18, "bold"),
                fg=color
            )

            label.pack(expand=True)

    root.mainloop()


board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

original_board = [row[:] for row in board]


print("Initial Puzzle:")
print_board(board)

if solve(board):
    print("\nSolved Puzzle:")
    print_board(board)
    print("\nTotal Steps:", steps)

    display_sudoku_gui(board, original_board)

else:
    print("No solution exists.")