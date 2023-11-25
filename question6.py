"""Write a python program to check whether a given string is a multiword string or single
word string using match case statement"""

n=(input("Enter a string:"))
n=n.strip()  #strip()  function remove stating and ending space of string
match n:
    case n if " " in n:
        print("its munlty word string")
    case _:
        print("its a single word string")
