
#10. Write a python script to display all prime numbers within a range.
# range
#start = 15
#end = 45
for i in range(15,46):
     k=int(i/2)
     for j in range(2,k):
          if(i%j==0):
               break
     if(j!=k-1):
       print("not a prime no:",i)
     else:
      print("Prime no.",i)