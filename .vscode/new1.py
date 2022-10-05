print("This is binary code guessing game and binary code always in\n", "01", "or something like in this format\nAnd you only 2 chances.")
binary = 1010
number_of_Guesses = 1

while number_of_Guesses <= 2:
    binary = int(input("What Is The Binary Code For = 10\n"))
    if binary != 1010: print("Wrong!Try Again...") 
    
    else:
        print("Yes,You Enter The Right Binary Code.")
        print(number_of_Guesses, "No of Guesses you took to finish the Game.")
        break
    print(2-number_of_Guesses, "No of guesses left.")
    number_of_Guesses += 1

if number_of_Guesses > 2: print("Game Over.")
