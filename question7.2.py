#Write a menu driven program to perform following operations - Addition, Subtraction,
#Multiplication, Division

print("Operations \n","1 sum\n","2 mul\n 3 subtraction \n 4 Division\n",end= ' ')
x,y=map(int,input("enter two number").split())
n=int(input("enter a choice"))
match n:
    case 1:print("sum is", x+y)
    case 2:print("multiplication is", x*y)
    case 3:print("subtraction is",x-y)
    case 4:print("Dicision is ", x/y)
    case _:
        print("Invalid choise")