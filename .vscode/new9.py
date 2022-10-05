# Number Guessing Game.
print("This is Number Guessing Game you have to choose number between 1-100 and You Have Only 5 Guesses.\n")
num = 20.22
Number_of_Guesses = 1
while Number_of_Guesses <= 5:
    num = eval(input("Guess The Number : "))
    if num > 20.22:
        print("You Guess High Number\n")
    elif num < 20.22:
        print("You Guess Low Number\n")
    else:
        print("Congrats,You Guess The Right Number.")
        print(Number_of_Guesses, "No of Guesses you took to finish the game.")
        break
    print(5-Number_of_Guesses, "No of Guesses left")
    Number_of_Guesses = Number_of_Guesses + 1

if Number_of_Guesses > 5:
    print("Game Over.")
    