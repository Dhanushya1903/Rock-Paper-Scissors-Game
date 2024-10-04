import tkinter as tk
from tkinter import messagebox
import random

def decide_winner(player_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = 'You win!'
    else:
        result = 'Computer wins!'
    
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

root = tk.Tk()
root.title('Rock, Paper, Scissors')
root.geometry('400x300')

title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Arial', 14))
title_label.pack(pady=20)

computer_label = tk.Label(root, text="Computer chose: ", font=('Arial', 12))
computer_label.pack()

result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: decide_winner('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: decide_winner('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: decide_winner('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

root.mainloop()
