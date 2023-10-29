<<<<<<< HEAD
"""Write a python script to use IS operator to display if both variables are the same
object or not?"""
l1=["Sakshi","Mishra"]
l3=["shaloni"]
l2=l1
l4=["Sakshi","Mishra"]
print(l2 is l1)  
print(l3 is l1)  
print(l1 is l4)  # They compare by the location and both have different location
print(l1==l4)  # now they by the value
=======
"""Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
a,b,c=map(int,input("enter a three no.").split())
if(a==b and b==c):
    print(a)
elif(a>b and a>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)

print((a if a>c else c) if a>b else (b if b>c else c))
>>>>>>> 10892ea (assignment 6)
