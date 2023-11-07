
		#  find  2nd maximum  bet'n 8 number........

a, b, c, d, e, f, g, h = map(int, input().split())

m = a
sm = b

if b > m:
    sm = m
    m = b
elif b > sm:
    sm = b

if c > m:
    sm = m
    m = c
elif c > sm:
    sm = c

if d > m:
    sm = m
    m = d
elif d > sm:
    sm = d

if e > m:
    sm = m
    m = e
elif e > sm:
    sm = e

if f > m:
    sm = m
    m = f
elif f > sm:
    sm = f

if g > m:
    sm = m
    m = g
elif g > sm:
    sm = g

if h > m:
    sm = m
    m = h
elif h > sm:
    sm = h

print("The second max is:", sm)


