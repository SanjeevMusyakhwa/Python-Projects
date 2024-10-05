import random # we Import random for the randomvalue

user_wins = 0 # we assign user_wins to 0
computer_wins = 0 # we assign computer_wins to 0

options = ["rock", "paper", "scissors"] # we assign options to list 

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors  or 'Q' to quit): ").casefold()
    if user_choice == 'q'.casefold():
        break

    if user_choice not in options:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    # rock => 0, paper => 1, scrissors => 2
    random_number = random.randint(0,2)
    

    computer_choice = options[random_number]
    print(f"Computer chosse: {computer_choice} ")

    if user_choice == "rock" and computer_choice =="scissors":
        print("you won ! ")
        user_wins += 1
        continue
    
    if user_choice == "paper" and computer_choice =="rock":
        print("you won ! ")
        user_wins += 1
        continue

    if user_choice == "scissors" and computer_choice =="paper":
        print("you won ! ")
        user_wins += 1
        continue
    elif(user_choice == computer_choice):
        print("It's a tie!. Please Try again once more")
    else:
        print("you Lost! ")
        computer_wins += 1
print(f"You won {user_wins} times!\nand computer won {computer_wins} times")
print("Goodbye!")
