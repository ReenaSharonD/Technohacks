import tkinter as tk
import random

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    result_text.set(f"Computer chose {computer_choice}\n")
    
    if player_choice == computer_choice:
        result_text.set(result_text.get() + "It's a tie!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result_text.set(result_text.get() + "You win!")
    else:
        result_text.set(result_text.get() + "Computer wins!")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

rock_button = tk.Button(root, text="Rock", command=lambda: play_game('Rock'))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('Paper'))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('Scissors'))
scissors_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop()