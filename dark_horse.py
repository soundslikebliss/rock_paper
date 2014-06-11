import sys
import random

while True:
  
  def player():
    print "Lets play a game \n"
    print "Press 'r' for Rock"
    print "Press 'p' for Paper"
    print "Press 's' for Scissors"
    print "Press 'l' for Lizard"
    print "Press 'k' for Spock"
    print "Press 'q' to quit \n"
    playerChoice = raw_input("what's it gonna' be? \n").lower()
    if playerChoice == "r":
      return "Rock"
    elif playerChoice == "p":
      return "Paper"
    elif playerChoice == "s":
      return "Scissors"
    elif playerChoice == "l":
      return "Lizard"
    elif playerChoice == "k":
      return "Spock"
    elif playerChoice == "q":
      sys.exit(0)
    else:
      player()

  def computerChoice():
    options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    computer = random.randint(0,4)
    return options[computer]

  you = player()
  hal = computerChoice()

  def battle(you, hal):
    if you == hal:
      return "Draw"
    elif you == "Rock" and hal == "Paper" or you == "Rock" and hal == "Spock":
      return "lose"
    elif you == "Paper" and hal == "Scissors" or you == "Paper" and hal == "Lizard":
      return "lose"
    elif you == "Scissors" and hal == "Rock" or you == "Scossors" and hal == "Spock":
      return "lose"
    elif you == "Lizard" and hal == "Rock" or you == "Lizard" and hal == "Scissors":
      return "lose"
    elif you == "Spock" and hal == "Lizard" or you == "Spock" and hal == "Paper":
      return "lose"
    else:
      return ""


  print "You chose: ", you
  print "Hal chose: ", hal
  outcome = battle(you, hal)
  if outcome == "Draw":
    print "It's a draw!"
  elif outcome == "lose":
    print "you lost, play again? \n"
  else:
    print "You won! Rad \n"


  








  