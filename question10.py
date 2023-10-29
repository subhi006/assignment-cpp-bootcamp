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