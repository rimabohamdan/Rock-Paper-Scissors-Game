import random

rock_ascii = """
    _______
---' ____)
      (______)
      (______)
      (____)
---.__(___)"""
paper_ascii = """
     _______
---' ____)____
           ______)
          _______)
         _______)
---.__________)"""
scissors_ascii = """
    _______
---' ____)____
          ______)
       __________)
      (____)
---.__(___)"""
print("\nWelcome to the Rock ,Paper ,Scissors game :")
confirm = input("Press Enter to continue or type (Help) for the rules ").lower()
if confirm == "help":
    print("""****** Rules ******
          1) You choose and the computer chooses
          2) Rock smashes Scissors ➡️ Rock Wins
          3) Scissors cut Paper ➡️ Scissors Win
          4) Paper covers Rock ➡️ Paper Wins""")
player = input("Enter your choice ( Rock ,Paper ,Scissors )\n").lower()
if player not in ["rock", "paper", "scissors"]:
    print("Invalid choice.")
    print("Please run the program again and choose Rock ,Paper ,or Scissors.")
else:
    if player == "rock":
        print(f"\n You choose:\n{rock_ascii}")
    elif player == "paper":
        print(f"\n You choose:\n{paper_ascii}")
    else:
        print(f"\n You choose:\n{scissors_ascii}")
computer_choice = random.choice(["rock", "paper", "scissors"])
if player == computer_choice:
    print("It's a tie!")
elif (
       (player == "rock" and computer_choice == "scissors")
       or
       (player == "paper" and computer_choice == "rock")
       or
       (player == "scissors" and computer_choice == "paper")
      ):
    print(f"You Win! {player} beats {computer_choice}.")
else :
    print("You lose")
  
