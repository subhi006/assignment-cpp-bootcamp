'''Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday'''


n=input("Enter a favorite color: with I like ______ color")
match n :
    case n if "yellow" in n:
        print("MOnday")
    case n if "blue" in n:
        print("Tuesday")
    case n if "orange " in n: 
        print("Wednesday")
    case n if "white" in n :
        print("Thursday")
    case n if "black" in n :
        print("Friday")
    case n if "red" in n :
        print("Saturday")
    case _:
        print("Sunday") 

