# Fibonacci Function
print("In This Function You Will Get Fibonacci Of NUmber That You Want.")

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter Your Number :- "))
print("Fibonacci = ", fibonacci(num))
