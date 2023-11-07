	
	#  find the 2nd max bet,n 4 number......

a,b,c,d = map(int,input().split())
if a > b:
	m1 = a
	s1 = b
else:
	m1 = b
	s1 = a
if c > d:
	m2 = c
	s2 = d
else:
	m2 = d
	s2 = c
if m1 > m2:
	if m2 > s1:
		sm = m2
	else:
		sm = s1
else:
	if m1 > s2:
		sm = m2
	else:
		sm = s2
print("second max:",sm)
