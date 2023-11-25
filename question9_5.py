#Write a python script to print first N odd natural numbers in reverse order
n=int(input("Enter a number"))
n=n*2-1
while(n>0):
    print(n)
    #i=i+2
    n=n-2