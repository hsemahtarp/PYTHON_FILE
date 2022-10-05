# MINI CALCULATOR
print("A mini Calculator For Some Operations.")
first = input("enter your number:")
operator = input("enter operator (+,-,*,/) :")
second = input("enter your number:")

try: 
    if operator == "+": print(eval(first) + eval(second))

    elif operator == "*": print(eval(first) * eval(second))  

    elif operator == "/": print(eval(first) / eval(second))    

    elif operator == "=": print(eval(first) - eval(second))
    
    else: print("invalid operation")   
except Exception as c:
    print(c)
print("Program End")
