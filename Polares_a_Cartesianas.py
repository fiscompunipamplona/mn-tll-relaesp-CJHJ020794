import math as mt
r=input("Radio: ")
r=float(r)
theta=input("Ángulo [Rad]: ")
theta=float(theta)
x=r*mt.cos(theta)
y=r*mt.sin(theta)
print("x es: ",x)
print("y es: ",y)
