"""Write a python script to take the month value in numeric format and display the
number of days in it."""
n=int(input("Enter a month no."))
if n in (1,3,5,7,9,11):
    print(31)
elif(n==2):
    print("28 and 19 depends on leap year")
elif n in (4,6,8,10,12):
    print(30)
else:
    print("not a valid month")