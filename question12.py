"""Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""

n=complex(input())
print(n)
print("real no.",n.real,"and imag no.",n.imag)
print(max(n.real,n.imag))


"""print("enter a number \n","1 sum\n","2 mul\n",end= ' ')
n=int(input("enter a choice"))
x,y=map(int,input("enter two number").split())
match n:
    case 1:print("sum is", x+y)
    case 2:print("multiplication is", x*y)"""

x=complex(input("Enter a complex number"))
print(x.real if x.real>x.imag else x.imag)