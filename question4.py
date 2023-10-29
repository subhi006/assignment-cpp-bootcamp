
"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""

#one way of solve
m=int(input("Enter a age of person:"))
match m:
    case m if m in range(10):
        print("Kid")
    case m if m in range(10,20):
        print("Teen")
    case m if m in range(20,40):
        print("young")
    case m if m in range(40,60):
        print("experience")
    case _:
        print("Senior citizen")


#second way
n=int(input("Enter a age of person"))
match n:
    case n if(n<10):
       print("Kid")
    case n if(n>=10 and n<20):
     print("Teen")
    case n if(n>=20 and n<40):
     print("young")
    case n if(n>=40 and n<60):
     print("Experienced")
    case _: 
     print("Senior Citizen")