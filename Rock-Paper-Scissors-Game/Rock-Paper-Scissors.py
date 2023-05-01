import random

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ")

    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)

    print("You chose", user_choice)
    print("Computer chose", computer_choice)

    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
