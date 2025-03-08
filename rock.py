import random
import tkinter as tk
from tkinter import messagebox

def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f'Computer chose: {computer_choice}\n{result}')

def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Paper' and computer == 'Rock') or \
         (user == 'Scissors' and computer == 'Paper'):
        return "You Win!"
    else:
        return "Computer Wins!"

def exit_game():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

# Labels and Buttons
label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))
label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: play('Rock'), width=10)
paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: play('Paper'), width=10)
scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: play('Scissors'), width=10)

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

exit_button = tk.Button(root, text="Exit", command=exit_game, width=10)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()
