import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        # Labels
        self.label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.label.pack(pady=10)

        # Buttons
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play_game("rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play_game("paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(root, text="Score - You: 0, Computer: 0")
        self.score_label.pack(pady=10)

    def play_game(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        # Update result and score labels
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    rps_gui = RockPaperScissorsGUI(root)
    root.mainloop()
