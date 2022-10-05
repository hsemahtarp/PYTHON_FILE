# stack the linear data structure
print("This Is A STACK Program You Can Add Numbers And Do The Things That Mentioned Below")
l = []
try:
    while True:
        num = {1:"Push Element", 2:"Pop Element", 3:"Peek Element", 4:"Bottom Element", 5:"All Element", 6:"Exit"}
        for key, value in num.items():
            print("Press", key, "For", value, "\n", end="")
        num = int(input(":- "))
        
        if num == 1:
            a= int(input("Enter The Number That You Want To Add In The Stack :- "))
            l.append(a)
            print(l)
        elif num == 2:
            if len(l) == 0:
                print("No! Elements In The Stack.")
            else:
                b = l.pop()
                print(b)
                print(l)
        elif num == 3:
            if len(l) == 0:
                print("Empty Stack.")
            else:
                print("Peek Element Of The Stack :- ",l[-1])
                print(l)
        elif num == 4:
            if len(l) == 0:
                print("Empty Stack.")
            else:
                print(l)
                print("Bottom Element Of Stack :- ",l[0])
        elif num == 5:
            print("All Element Of The Stack :- ",l)
        elif num == 6:
            print("Thanks,For Using This Program.")
            break
except Exception as S:
    print("Invalid Input")
