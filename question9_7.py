#Write a python script to print first N even natural numbers in reverse order
n=int(input("Enter a number"))
i=n*2
while(n>0):
    print(i)
    i=i-2
    n=n-1