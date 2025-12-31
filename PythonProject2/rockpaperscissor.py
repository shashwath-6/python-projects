import tkinter as tk
from tkinter import messagebox
import random


# Game Instructions
def show_instructions():
    """Function to display game instructions in a message box"""
    instructions= (
        "Welcome to the Rock-Paper-Scissors Game!\n"
        "- You will play 10 rounds against the computer.\n"
        "- Choose Rock, Paper, or Scissors for each round.\n"
        "- The player with the highest score wins.\n"
        "- If the score is tied after 10 rounds, a final golden round will decide the winner.\n"
        "- If the golden round is also tied, the game will continue until a winner is determined.\n"
        "Good luck!"
    )
    messagebox.showinfo("Game Instructions", instructions)


# Main Game Class
class RockPaperScissorsGame:
    """Main game class that controls the game logic and UI"""
    def __init__(self, root):
        """used to set the game up and initialize the game variables"""
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.player_score = 0
        self.computer_score = 0
        self.round_number = 0
        self.options = ["Rock", "Paper", "Scissors"]

        self.label = tk.Label(root, text="Choose your option:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        for option in self.options:
            button = tk.Button(
                self.buttons_frame,
                text=option,
                font=("Arial", 12),
                width=10,
                command=lambda opt=option: self.play_round(opt)
            )
            button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.score_label = tk.Label(root, text=f"Player: 0  |  Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.round_label = tk.Label(root, text="Round: 1 / 10", font=("Arial", 12))
        self.round_label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)


    def play_round(self, player_choice):
        if self.round_number >= 10 and self.player_score != self.computer_score:
             return

        computer_choice = random.choice(self.options)
        result = self.determine_winner(player_choice, computer_choice)

        if result == "Player":
            self.player_score += 1
        elif result == "Computer":
            self.computer_score += 1

        self.round_number += 1

        self.update_ui(player_choice, computer_choice, result)

        # Check for golden round or continued golden rounds
        if self.round_number >= 10:
            if self.player_score == self.computer_score:
                messagebox.showwarning("Golden Round",
                                       "The game is tied! The game will continue until a winner is determined.")
                self.round_label.config(text=f"Golden Round: {self.round_number - 9}")
            else:
                self.end_game()

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Draw"
        elif (
                (player_choice == "Rock" and computer_choice == "Scissors") or
                (player_choice == "Paper" and computer_choice == "Rock") or
                (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            return "Player"
        else:
            return "Computer"

    def update_ui(self, player_choice, computer_choice, result):
        self.score_label.config(text=f"Player: {self.player_score}  |  Computer: {self.computer_score}")
        self.round_label.config(text=f"Round: {self.round_number} / 10")

        if result == "Draw":
            self.result_label.config(text=f"It's a draw! Both chose {player_choice}.")
        else:
            self.result_label.config(
                text=f"{result} wins! Player chose {player_choice}, Computer chose {computer_choice}.")

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.round_number = 0
        self.score_label.config(text="Player: 0  |  Computer: 0")
        self.round_label.config(text="Round: 1 / 10")
        self.result_label.config(text="")

    def end_game(self):
        if self.player_score > self.computer_score:
            winner = "Player"
        elif self.computer_score > self.player_score:
            winner = "Computer"
        else:
            winner = "Golden Round"

        if winner == "Golden Round":
            self.round_number = 10  # Allow continued golden rounds
        else:
            messagebox.showinfo("Game Over",
                                f"{winner} wins the game!\nFinal Score: Player {self.player_score} - Computer {self.computer_score}")



# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("900x1080")
    show_instructions()
    game = RockPaperScissorsGame(root)
    root.mainloop()
