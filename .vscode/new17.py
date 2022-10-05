# ROCK PAPER SCISSOR GAME
import random
print("THIS IS ROCK PAPER SCISSOR GAME.")
Your_Score = 0
Computer_Score = 0
Round_Count = 1
cw = ["r", "p", "s"]

Your_name = input("Enter Your Name :- ")
print(Your_name, "LETS PLAY...ROCK PAPER SCISSOR.", "\n")
try:
    while Round_Count <= 10:
        print(Your_name, "This Is Round No :- ", Round_Count)
        print(Your_name, "Choose Your Weapon From Given Options :- ")
        Your_weapon = {"R or r": "ROCK", "P or p": "PAPER", "S or s": "SCISSOR"}
        for key, value in Your_weapon.items():
            print(" Press", key, "For", value, "\n", end="")
        Your_weapon = input(Your_name + " Your Weapon :- ")
        Round_Count += 1
        Computer_Weapon = random.choice(cw)
        if Your_weapon == "R" or Your_weapon == "r":
            if Computer_Weapon == "r":
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Ohhh! It's Tie...")
                print(Your_name, " Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
            elif Computer_Weapon == "s":
                Your_Score += 1
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Yehhh! You Won This Round.")
                print(Your_name, "Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
            else:
                Computer_Score += 1
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Ooops! You Loose This Round.")
                print(Your_name, " Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
        elif Your_weapon == "P" or Your_weapon == "p":
            if Computer_Weapon == "p":
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Ohhh! It's Tie...")
                print(Your_name, " Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
            elif Computer_Weapon == "r":
                Your_Score += 1
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Yehhh! You Won This Round.")
                print(Your_name, " Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
            else:
                Computer_Score += 1
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Ooops! You Loose This Round.")
                print(Your_name, " Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
        elif Your_weapon == "S" or Your_weapon == "s":
            if Computer_Weapon == "s":
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Ohhh! It's Tie...")
                print(Your_name, " Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
            elif Computer_Weapon == "p":
                Your_Score += 1
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Yehhh! You Won This Round.")
                print(Your_name, " Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
            else:
                Computer_Score += 1
                print("Computer Weapon :- ", Computer_Weapon)
                print(Your_name, " Ooops! You Loose This Round.")
                print(Your_name, " Your Score = ", Your_Score, "\nComputer Score = ", Computer_Score, "\n")
        else:
            print("You Entered Invalid Input....\nTry Entering From The Given Options.")

    print("*" * 30)
    if Computer_Score > Your_Score:
        print(Your_name, " Ooohhh....You Loose The Game.")
        print(Your_name, " Your score : ", Your_Score, "\nComputer score : ", Computer_Score,"\n",("*"*30), "\n", Your_name, " Thanks For Playing.")
    elif Computer_Score < Your_Score:
        print("CONRAGULATIONS", Your_name, "YOU ARE THE WINNER.")
        print(Your_name, " Your score : ", Your_Score, "\nComputer score : ", Computer_Score, "\n",("*"*30), "\n", Your_name, " Thanks For Playing.")
    else:
        print(Your_name, " AAhh....It's A TIE.")
        print(Your_name, " Your score : ", Your_Score, "\nComputer score : ", Computer_Score,"\n",("*"*30), "\n", Your_name, " Thanks For Playing.")

except Exception as game:
    print("Invalid Input....Try Again.")
