# OOP-VS-PROCEDEURAL-ROCK-PAPER-SCISSORS
# Using Using procedeural coding  to program Rock parper scissors


import random

# list of options
options = ['rock', 'paper', 'scissors']

# function to determine the winner
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"
  elif user_choice == 'rock':
    if computer_choice == 'paper':
      return "Computer wins!"
    else:
      return "You win!"
  elif user_choice == 'paper':
    if computer_choice == 'scissors':
      return "Computer wins!"
    else:
      return "You win!"
  elif user_choice == 'scissors':
    if computer_choice == 'rock':
      return "Computer wins!"
    else:
      return "You win!"

# main game loop
while True:
  # get user's choice
  user_choice = input("Enter your choice (rock/paper/scissors): ")
  if user_choice not in options:
    print("Invalid choice. Please try again.")
    continue

  # get computer's choice
  computer_choice = random.choice(options)
  print(f"Computer chose {computer_choice}")

  # determine the winner
  result = determine_winner(user_choice, computer_choice)
  print(result)

