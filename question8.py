<<<<<<< HEAD
#Write a python script to use IN operator to display the data present in the list

l1=["sakshi","saloni"]
print("sakshi" in l1)

=======
"""Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""

print("Enter a value of a,b and c")
a,b,c=map(int,input().split())
d=b**2-4*a*c
if(d>0):
    print("Real and distinct root")
elif(d==0):
    print("Real and equle root")
else:
    print("Imaginary root")
>>>>>>> 10892ea (assignment 6)
