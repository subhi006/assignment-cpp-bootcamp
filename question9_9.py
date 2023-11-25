#Write a python script to print cubes of first N natural numbers
n=int(input("Enter a number"))
i=1
while(n>0):
    print(i**3)
    i=i+1
    n=n-1