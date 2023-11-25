"""Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
n,m,p=map(int,input("enter three no.").split())
if n>m and n>p:
    print(n)
elif m>p:
    print(m)
else:
    print(p)
