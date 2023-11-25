
"""Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""
n=int(input("Enter a year:"))
match n:
    case n if(n%100==0):
        if(n%400==0):
         print("Century leap year")
        else:
         print("Century non leap year")
    case n if(n%4==0):
      print("NOn century leap year")
    case _:
      print("NOn century non leap year")