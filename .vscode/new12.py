# Factorial Function
print("In This Function YOu Will Get Factorial OF The Number That You Want.")


def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


inp = int(input("Enter Your Number :- "))
print("Factorial = ", factorial(inp))


def FACTORIAL(n):
    if n == 1:
        return 1
    else:
        return n * FACTORIAL(n - 1)


number = int(input("Enter Your Number :- "))
print("Factorial = ", FACTORIAL(number))
