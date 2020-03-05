import math as mt
c=3e8 # mts / seg
añoluz=9.461e15 # mts
print("Nave viajando desde la tierra hasta otro planeta.")
x=input("Años luz desde la tierra: ")
x=float(x)
x=x*añoluz # mts
v=input("Velocidad como fracción de 'c': ") # mts / seg
v=float(v)
t1=x/(v*c) # seg
t2=(t1-((v*x)/c))/mt.sqrt(1-(v**2)) # seg
t=t1/t2 # seg
print("Tiempo medido en la tierra: ",t1,"seg")
print("Tiempo medido en la nave",t2,"seg")
print("Tiempo Tierra / Tiempo Nave: ",t,"seg")
