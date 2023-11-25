#Write a python script to check whether a given year is a leap year or not.
n=int(input("enter ano."))
if n%100==0:
    if n%400==0:
        print("leap year")
    else:
        print("not a leap year")
elif(n%4==0):
    print("leap year")
else:
    print("not a leap year")