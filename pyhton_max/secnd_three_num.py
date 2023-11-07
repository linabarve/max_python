	# find the 2nd maximum bet'n three number.............

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
max = a
sm = b

if b > max:
    max = b
    sm = a

if c > max:
    sm = max
    max = c
elif c > sm:
    sm = c

print("The second maximum number is:", sm)
""


"""
a,b,c = map(int,input).()slipt())
max = a
sm = b

if b > max:
    max = b
    sm = a

if c > max:
    sm = max
    max = c
elif c > sm:
    sm = c

print("The second maximum number is:", sm)
"""


