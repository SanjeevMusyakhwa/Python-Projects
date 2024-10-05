print ("Welcome To My Computer Quiz Game! .\n")

playing = input("Do you want to play this game? ")
if playing not in ['YES', 'yes', 'Yes']:
    print("GoodBye !\n")
    quit()
else:
    print("Let's begin the game.\n")
    score = 0
    total_questions = 5
    # 1st question
    answer = input("Who is the father of computer: ")
    if answer.casefold() == 'charles babbage'.casefold():
        score += 1
        print("Correct Answer!")
    else:
        print("Incorrect Answer! The correct answer is Charles Babbage.")
    #2nd question
    answer = input(" The Miss Porters Network is a: ")
    if answer.casefold() == 'lan'.casefold():
        score += 1
        print("Correct Answer!")
    else:
        print("Incorrect Answer! The correct answer is LAN.")
    # 3rd question
    answer = input(" Which is considered to be the computer's short-term memory? ")
    if answer.casefold() == 'ram'.casefold():
        score += 1
        print("Correct Answer!")
    else: 
        print("Incorrect Answer! The correct answer is RAM.")
    # 4th question
    answer = input(" What is the brain of the computer? ")
    if answer.casefold() == 'CPU'.casefold():
        score += 1
        print("Correct Answer!")
    else:
        print("Incorrect Answer! The correct answer is CPU.")
    # 5th question
    answer = input(" What allows multiple programs to run on a computer? ")
    if answer.casefold() == 'OS'.casefold():
        score += 1
        print("Correct Answer!")
    else:
        print("Incorrect Answer! The correct answer is OS")
print(f"Your score is {score} questions Correct in {total_questions} total questions")
    



    
