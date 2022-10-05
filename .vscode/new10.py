# Astrologer Stars
while True:
    print("Printing Star Pattern")
    num = eval(input("How Many Rows You Want TO Print : "))
    bool_val = input("Enter 1 For True Or Enter 0 For False : ")
    if bool_val == "1":
        for i in range(0,num+1):
             print("*"*int(i))
    if bool_val == "0":
        for j in range(num,0,-1):
             print("*"*int(j))
    press = input("If You Want To Do This Again\nEnter Y for Yes Or Enter N For No\nPress :- ")
    if press == "Y" or "y":
        continue
    else:
        break
    