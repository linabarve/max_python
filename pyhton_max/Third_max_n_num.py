

	# Third  max N number................



n = int(input("Enter the number of values:"))
m = float('-inf')  
Smax = float('-inf')  
Tmax = float('-inf')  

for i in range(1, n + 1):
    k = int(input())
    
    if k > m:
        Tmax = Smax
        Smax = m
        m = k
    elif k > Smax:
        Tmax = Smax
        Smax = k
    elif k > Tmax:
        Tmax = k

print("Maximum value:", m)
print("Second maximum value:", Smax)
print("Third maximum value:", Tmax)


