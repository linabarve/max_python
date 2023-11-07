 
a,b,c,d,e = map(int,input().split())
if  a > b:
	m = a
if m > c:
	m2 = m
if m2 > d:
	m3 = m2
if m3 > e:
	print(m3)
else:
	print(e)
