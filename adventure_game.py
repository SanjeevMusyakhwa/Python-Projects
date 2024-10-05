answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

name = input("Please Type your name: ")
print(f" Welcome, {name}, to this avdenture game.\n")

answer = input("""You are standing outside of your house and you see a man running towards you and asking for urgent shelter.
               Will you provide shelter to him. ( Yes / No )""")
if answer in answer_yes:
    print("\nAfter 2 minutes, the Police came to your house, and ask you that whether the thief is in your house or not. Will you say ( Yes / No ) ")
    answer1 = input(  )
    if answer1 in answer_yes:
        print("\n you are an honest person. He was a thief and You won the game.\n")
    elif answer1 in answer_no:
        print("\n you are a liar. He was a thief and You helped the thief. Now, go to jail. GameOver\n")
    else:
        print("You typed the wrong input. Goodbye!")
        exit()
elif answer in answer_no:
    print("\nNow he is trying to kill you. Will you Knock him down? ( Yes / No )")
    answer2 = input(  )
    if answer2 in answer_yes:
        print("\nYou knocked him down. and helped police to catch him with bravery.")

    elif answer2 in answer_no:
        print("\nYou are dead. Game Over\n")
    else:
        print("You typed the wrong input. Goodbye!")
        exit()
else:
    print("You typed the wrong input. Goodbye!")
    exit()