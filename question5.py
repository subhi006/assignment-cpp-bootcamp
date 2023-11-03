"""Write a python script which takes a three digit number from the user and displays
only its first digit."""

x=int(input("Enter a no.:"))
while(x>=10):
    x=int(x/10)
print(x)