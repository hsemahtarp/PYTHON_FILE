# input from user Dictionary
print("I Made a Dictionary with my own words so first read all the Dictionary and then enter the word that "
      "which Meaning you want. ")
Dict = {"finesse": "clever", "mutable": "can change", "immutable": "cannot change", "serene": "calm", "apex": "top"}
key = input("enter your word:")
if key in Dict:
    print("Value of word is in Dictionary :", (Dict[key]))
else:
    print("Error! This Word is not in Dictionary")
    