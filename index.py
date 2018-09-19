# ask user if they want to play 
# get users response
# if 'n' then say, "goodbye!"
# if 'y' then,
# get computers random response
# ask for users response
# compare both of them and display result
# Ask user if they want to play

import random 

choices = ['r','p','s']

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

  if userPick != 'r' and userPick != 'p' and userPick != 's':
    print("Invalid Option. Please choose only 'r', 'p' or 's'")
  else: 
    print("-" * 30)
    print("You chose: " + userPick)
    print("Computer chose: " + computerChoice)
    
    userIndex = choices.index(userPick)
    computerIndex = choices.index(computerChoice)
    diff = computerIndex - userIndex

    if diff == 0:
      print("Draw")
    elif diff == -1:
      print("You win!")
    else: 
      print("You lose...")

  print("-" * 30)

game()

