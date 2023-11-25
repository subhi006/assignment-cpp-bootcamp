"""Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""
print("Menu:")
print("1. isosceles:")
print("2. right angle triangle:")
print("3. equilateral triangle:")
n=int(input("Enter your choice:"))
x,y,z=map(float,input("Enter three numbers:").split( ))
match n:
    case 1:
          if(x==y or y==z or z==x):
               print("it is a Isosceleles Triangle")
    case 2:
          x,y,z=x*x,y*y,z*z
          if(x+y==z or x+z==y or y+z==x):
                print("it is right angle tringle")
          else:
               print("it is not a tright angle triangle")       
    case 3:
        if(x==y and y==z):
            print("yes, it is a equilateral triangle")
        else:
            print("not a equilateral tiangle")
sum=x+y+z