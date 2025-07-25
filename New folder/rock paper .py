import tkinter as tk
from tkinter import messagebox
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("✊✋✌️ Rock Paper Scissors - Advanced")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#e6f2ff")

        self.user_score = 0
        self.computer_score = 0

        self.choices = ['Rock', 'Paper', 'Scissors']

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Rock Paper Scissors Game", font=("Helvetica", 20, "bold"), bg="#e6f2ff", fg="#2b2b2b").pack(pady=20)

        # Score Frame
        score_frame = tk.Frame(self.root, bg="#e6f2ff")
        score_frame.pack()

        self.user_score_label = tk.Label(score_frame, text="🧍 You: 0", font=("Arial", 14), bg="#e6f2ff")
        self.user_score_label.grid(row=0, column=0, padx=20)

        self.computer_score_label = tk.Label(score_frame, text="💻 Computer: 0", font=("Arial", 14), bg="#e6f2ff")
        self.computer_score_label.grid(row=0, column=1, padx=20)

        # Button Frame
        button_frame = tk.Frame(self.root, bg="#e6f2ff")
        button_frame.pack(pady=30)

        tk.Button(button_frame, text="🪨 Rock", width=12, font=("Arial", 14), bg="#add8e6", command=lambda: self.play("Rock")).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="📄 Paper", width=12, font=("Arial", 14), bg="#90ee90", command=lambda: self.play("Paper")).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="✂️ Scissors", width=12, font=("Arial", 14), bg="#ffb6c1", command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=10)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 15), bg="#e6f2ff", fg="#222")
        self.result_label.pack(pady=25)

        # Status bar
        self.status = tk.Label(self.root, text="Make your move!", font=("Arial", 12, "italic"), bg="#e6f2ff", fg="gray")
        self.status.pack(side="bottom", fill="x")

        # Reset button
        tk.Button(self.root, text="🔄 Reset Game", font=("Arial", 12, "bold"), bg="#ffdddd", command=self.reset_game).pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = ""

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            self.user_score += 1
            result = "🎉 You Win!"
        else:
            self.computer_score += 1
            result = "😞 You Lose!"

        self.update_gui(user_choice, computer_choice, result)

    def update_gui(self, user_choice, computer_choice, result):
        self.result_label.config(
            text=f"🧍 You: {user_choice}\n💻 Computer: {computer_choice}\n\n📣 {result}"
        )
        self.user_score_label.config(text=f"🧍 You: {self.user_score}")
        self.computer_score_label.config(text=f"💻 Computer: {self.computer_score}")
        self.status.config(text="Play again or Reset to start fresh.")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="🧍 You: 0")
        self.computer_score_label.config(text="💻 Computer: 0")
        self.result_label.config(text="")
        self.status.config(text="Game reset! Make your move.")

# Main App
if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()
