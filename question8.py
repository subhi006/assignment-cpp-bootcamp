"""Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""

a,b,c=map(int,input("enter value of a,b,c").split())
d=b**2-4*a*c
if d>0:
    print("real and distict")
elif(d==0):
    print("real and equal")
else:
    print("imaginary")
