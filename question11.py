"""Write a python script to take the month value in numeric format and display the
number of days in it."""
n=int(input("Enter a number of month"))
match n:
    case n if n in (1,3,5,7,9,11):
        print("Number of days in this month is 30")
    case 2:
        print("number of days is 28 and 29 dependes on leap year")
    case n if n in (2,4,6,8,10,12):
        print("Number of days in this month is 31") 
              