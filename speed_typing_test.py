import time

def speed_typing_test(): #function  to test the typing speed

    sentence = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    
    print("Type the following sentence as fast as you can:")
    print(f"\n{sentence}\n") #mathi ko sentence lai print garxa

    start_time = time.time() #Start Time ko record rakhxa

    user_input = input("Start typing: ") #user sanga input mageko

    
    end_time = time.time() #end time ko record  rakhxa

    if not user_input:
        print("You didn't type anything")
        return

    
    time_taken = end_time - start_time #time taken calculate garxa

    word_count = len(sentence.split())  #sentence ma word count calculate garxa

    wpm = (word_count / time_taken) * 60 #wpm  calculate garxa

    accuracy = sum (1 for a,b in zip(sentence, user_input) if a == b ) / len(sentence) *100
    print(f"\nTime taken: {time_taken:.2f} seconds") #time taken display garxa
    print(f"Your typing speed is: {wpm:.2f} WPM") #typing speed display garxa
    print(f"Accuracy : {accuracy : .2f} % ") #accuracy Display garxa


if __name__ == "__main__": #main function 
    speed_typing_test()
    
else :
    exit()
