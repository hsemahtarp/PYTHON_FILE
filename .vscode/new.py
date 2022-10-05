# Movie Guessing Game.
print("This is Movie Guessing Game\nYOu have Only 3 chances to guess the movie name")

movie_name = "777Charlie"
Number_of_Chances = 1

while Number_of_Chances <= 5:
    print("This Movie Has 10 letters = 7*3", ('\N{Dog}'))
    movie_name = input("Guess Movie = ")
    if movie_name != "777Charlie":
        print("Oooops!You Guess Wrong Movie Name")
    else:
        print("Congrats,You Guess The Movie.")
        print(Number_of_Chances,"NO Of Chances You Took To Finish Game.")
        break
    print(5-Number_of_Chances,"No of Chances Left...\n")
    Number_of_Chances = Number_of_Chances + 1

if Number_of_Chances > 5:
    print("Game Over.")
