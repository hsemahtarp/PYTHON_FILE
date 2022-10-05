# faulty calculator 45*3=555, 56+9=77, 56/6=4, 153-3=127
print("Hello Guys,\nWelcome to Calculator\n I made a faulty calculator only for some calculations which i already "
      "mentioned above.")
n1 = input("enter your number:")
operator = (input("enter your operator(+, -, *, /) :"))
n2 = input("enter your number:")

if operator == "+":
    if n1 == 56 and n2 == 9:
        print("Your Answer = 56+9=77")
    else:
        print("Your Answer =", eval(n1) + eval(n2))
elif operator == "-":
    if n1 == 153 and n2 == 3:
        print("Your Answer = 153-3=127")
    else:
        print("Your Answer =", eval(n1) - eval(n2))
elif operator == "*":
    if n1 == 45 and n2 == 3:
        print("Your Answer = 45*3=555")
    else:
        print("Your Answer =", eval(n1) * eval(n2))
elif operator == "/":
    if n1 == 56 and n2 == 6:
        print("Your Answer = 56/6=4")
    else:
        print("Your Answer = ", eval(n1) / eval(n2))
else:
    print("Error! Invalid Operation\nTyr again")
    