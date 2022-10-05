# Queue The Linear Data Structure
print("This Is A QUEUE Program You Can Add The Number And Do The Things That Mentioned Below.")
l = []
try:
    while True:
        num = {1:"Enqueue Element", 2:"Dequeue Element", 3:"Rear Element", 4:"Front Element", 5:"All Element", 6:"Exit"}
        for key, value in num.items():
            print("Press", key, "For", value, "\n", end="")
        num = int(input(":- "))

        if num == 1:
            a = int(input("Enter The Number That You Want To add In The Queue :- "))
            l.append(a)
            print(l)
        elif num == 2:
            if len(l) == 0:
                print("No! Element In The Queue...")
            else:
                b = l.pop()
                print("The Dequeue Element :- ",b)
                print(l)
        elif num == 3:
            if len(l) == 0:
                print("Empty Queue...")
            else:
                print(l)
                print("Rear Element Of The Queue :- ",l[0])
        elif num == 4:
            if len(l) == 0:
                print("Empty Queue...")
            else:
                print(l)
                print("Front Element Of The Queue :- ",l[-1])
        elif num == 5:
            print("All Element Of The Queue :- ",l)
        else:
            print("Thanks,For Using This Program.")
            break
except Exception as Q:
    print("Invalid Input....")
