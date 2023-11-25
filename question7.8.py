"""Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""

#n,m=map(str,input("Enter two strings with comma").split(","))
m=input("enter first string")
n=input("enter second string")
match (n,m): #there is (n,m) is a tuple 
    case (n,m) if n==m:
          print(" identical string")
    case (n,m) if(n>m): 
          print("{} comes after {}".format(n,m))
    case (n,m) if(n<m):
          print("{} comes after {}".format(m,n))
