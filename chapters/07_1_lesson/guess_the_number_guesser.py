# Number Guessing Game - Guesser
# The user thinks of a number between 1 and 100 and the program tries to guess it.
# The user should tell the program if the guess is too high, too low, or correct.
# The program should tell the user how many guesses it took to guess the number.

import random
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_number_feedback():
    # TODO: Implement this function 
    answer = input("Enter 'h' if the guess is too high, 'l' if it's too low, 'c' if it's correct")
    return answer 
    


def get_number():
    # TODO: Implement this function
    #return random.randint(MIN_NUMBER, MAX_NUMBER)
    return (MIN_NUMBER + MAX_NUMBER) // 2
    


def play_guesser():
    global MIN_NUMBER
    global MAX_NUMBER
    
    print('-' * 60)
    print()
    print(f"Think of a number between {MIN_NUMBER} and {MAX_NUMBER} (inclusive).")
    input("Press Enter when you have thought of a number.")
    print()
    guess_count = 0
    # TODO: Implement the rest of this function 
    while True: 
        guess_count +=1
        # computer decide guess 
        guess = get_number()
        print(f"I'm guessing {guess}")
        # asker user for feed back on geuss 
        feedback = get_number_feedback()
        if feedback == 'c': 
            print(f"I guessed your number in {guess_count} guesses") 
            return guess_count 
        elif feedback == 'h': 
            MAX_NUMBER = guess - 1
        elif feedback == 'l':
            MIN_NUMBER = guess + 1
            
        # if correct exit function
        # if incorrecr decide nect guess

    

def main():
    print('-' * 60)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    while True:
        guess_count = play_guesser()
        answer = input("Do you want to play again? (y/n) ").lower()
        if answer != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()