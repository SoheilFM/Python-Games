import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Create a function to handle the user's choice
def play(player_choice):
    # Convert the player's choice to lowercase
    player_choice = player_choice.lower()

    # Generate the computer's choice randomly
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner
    if player_choice == computer_choice:
        result = "Tie!"
    elif player_choice == "rock" and computer_choice == "scissors":
        result = "You Win!"
    elif player_choice == "paper" and computer_choice == "rock":
        result = "You Win!"
    elif player_choice == "scissors" and computer_choice == "paper":
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Update the label to show the result
    label_result.config(text=result)

    # Update the label to show the computer's choice
    label_computer.config(text="Computer's Choice: " + computer_choice)

# Create the label for the user's choice
label_player = tk.Label(root, text="Your Choice:")
label_player.pack()

# Create the buttons for the user's choice
button_rock = tk.Button(root, text="Rock", command=lambda: play("rock"))
button_rock.pack()

button_paper = tk.Button(root, text="Paper", command=lambda: play("paper"))
button_paper.pack()

button_scissors = tk.Button(root, text="Scissors", command=lambda: play("scissors"))
button_scissors.pack()

# Create the label for the computer's choice
label_computer = tk.Label(root, text="Computer's Choice:")
label_computer.pack()

# Create the label for the result
label_result = tk.Label(root, text="")
label_result.pack()

# Run the main loop
root.mainloop()
