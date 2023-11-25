#Write a python script to display the number of days in a given month number.

#1 way of solve
n=int(input("Enter a month number:"))
match n:
    case n if n in (1,3,5,7,9,11):
        print("Number of days is 31")
    case 2:
        print("Number of days is 28 or 29 depending on leap year.")
    case n if n in (4,6,8,10,12):
        print("Number of days is 30")
    case _:
        print("Invalid Month Number")

# worst way of solve:

n=int(input("Enter a month number:"))
match n:
    case 1:
        print("30")
    case 2:
        print("28 and 29")
    case 3:
        print("30")
    case 4:
        print("31")
    case 5:
        print("30")
    case 6:
        print("31")
    case 7:
        print("30")
    case 8:
        print("31")
    case 9:
        print("30")
    case 10:
        print("31")
    case 11:
        print("30")
    case 12:
        print("31")