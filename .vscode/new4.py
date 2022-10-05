# BINARY CODE CALCULATOR
print("This Is Binary Code Calculator In This Calculator\nYou Will Get Binary Code OF Your Two Numbers")
print("And Starting of Any Binary You WIll See '0b' The Meaning Of this is That The Number Is in Binary")
print("WARNING!If Ans Will Be In Float Then The Answer Will Not Print.\n")
def binary_calculator():
    try:
        n1 = input("Enter First Number : ")
        operator = input("Enter Operator (+, -, /, *) : ")
        n2 = input("Enter Second Number : ")
        if operator == '+': print("Answer = ",int(n1) + int(n2), "\nBinary Code =", bin(int(n1) + int(n2)))
        elif operator == '-': print("Answer = ",int(n1) - int(n2), "\nBinary Code =", bin(int(n1) - int(n2)))
        elif operator == '/': print("Answer = ",int(n1) / int(n2), "\nBinary Code =", bin(int(n1) / int(n2)))
        elif operator == '*': print("Answer = ",int(n1) * int(n2), "\nBinary Code =", bin(int(n1) * int(n2)))
        else: print("Invalid Operation.")
    except Exception as b:
        print(b)  
    print("Program End")

binary_calculator()
