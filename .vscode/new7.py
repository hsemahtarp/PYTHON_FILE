# quiz break and continue statement
print("Quiz With While LOOP.")
while(True):
    inp = eval(input("Enter Your Number\n"))
    if inp > 100:
        print("Felicitaciones,you entered a number greater than 100")
        break
    else:
        print("Try Again!\n")
        continue
