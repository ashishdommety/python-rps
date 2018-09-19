# ask user if they want to play 
# get users response
# if 'n' then say, "goodbye!"
# if 'y' then,
# get computers random response
# ask for users response
# compare both of them and display result
# Ask user if they want to play

import random 

def game():
  user = input("Do you want to play rock, paper, scissors? (y/n)\n")
  if user == "n":
    print("Goodbye!")
  else:
    userChoice = input("Choose rock, paper or scissors (r/p/s):\n ")
    compareBoth(userChoice)
    game()

def compareBoth(userPick):
  choices = ["r","p","s"]
  randomNumber = random.randrange(3)
  computerChoice = choices[randomNumber]
  print("-" * 30)
  print("You chose: " + userPick)
  print("Computer chose: " + computerChoice)

  if userPick == 'r': 
    if computerChoice == 's':
      print("You win!")
    elif computerChoice == 'p':
      print("You lose...")
  
  if userPick == 's':
    if computerChoice == 'p':
      print("You win!")
    elif computerChoice == 'r':
      print("You lose...")
  
  if userPick == 'p': 
    if computerChoice == 'r':
      print("You win!")
    elif computerChoice == 's':
      print("You lose...")
  
  if userPick == computerChoice:
    print("Draw")
  
  if userPick != 'r' and userPick != 's' and userPick != 'p':
    print("invalid character - please enter either 'r' 'p' or 's'")
  print("-" * 30)

game()

