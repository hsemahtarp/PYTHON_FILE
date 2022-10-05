print("Health Management System.")
Client_list = {1: "Prathamesh", 2: "Bhai", 3: "Jadhav"}
Health_list = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client From This.")
    for key, value in Client_list.items():
        print("Press", key, "For", value, "\n", end="")
    Client_name = int(input(":- "))

    print("Selected Client : ", Client_list[Client_name], "\n", end="" )

    print("Press 1 for Log.")
    print("Press 2 for Retrieve.")
    press = int(input(":- "))

    if press == 1:
        for key, value in Health_list.items():
            print("Press", key, "For", value, "\n", end="")
        Health_name = int(input(":- "))
        print("Selected Job : ", Health_list[Health_name], "\n", end="")
        f = open(Client_list[Client_name]+"_"+Health_list[Health_name]+"hms.txt", "a")
        k = "y"
        while k != "n":
            print("Enter :- ", Health_list[Health_name], "\n:- ", end="")
            mytext = input()
            f.write("[" + str(getdate())+"]:"+mytext+"\n")
            k = input("Want To Add More? y/n :- ")
            continue
        f.close()
    elif press == 2:
        for key, value in Health_list.items():
            print("Press", key, "For Retrieve", value, "\n", end="")
        Health_name = int(input(":- "))
        print(Client_list[Client_name], "-", Health_list[Health_name], "Report :-", "\n", end="")
        f = open(Client_list[Client_name]+"_"+Health_list[Health_name]+"hms.txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input!!!!")
except Exception as p:
    print("Wrong Input....")
