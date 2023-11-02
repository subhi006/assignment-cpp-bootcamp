"""Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""
n=complex(input("enter a complex no."))
print(max(n.imag,n.real))