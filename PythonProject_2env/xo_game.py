import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.current_player = "X"

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.window, text="", font=("Arial", 24), height=2, width=5,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

        self.reset_button = tk.Button(
            self.window, text="Reset", font=("Arial", 14), command=self.reset_game
        )
        self.reset_button.grid(row=3, column=0, columnspan=3)

        self.window.mainloop()

    def on_click(self, row, col):
        """Handle a button click"""
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                if self.current_player == "X":
                    self.current_player = "O"
                else:
                    self.current_player = "X"
                #self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Check rows, columns, and diagonals"""
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True

        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def is_draw(self):
        """Check if the game is a draw"""
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    return False
        return True

    def reset_game(self):
        """Reset the game"""
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""

if __name__ == "__main__":
    TicTacToe()
