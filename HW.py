print ("give 3 numbers") 
x = int(input("Value of x:"))
y = int(input("Value of y:"))
z = int(input("Value of z:"))

t = x
t2 = y
x = z
y = t
z = t2

print ("X is now ", x,",Y is now ",y,", and Z is now ",z)