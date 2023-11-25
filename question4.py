"""Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same."""
n,y=map(int,input("enter a two no.").split())
print(n if(n>y) else y)
