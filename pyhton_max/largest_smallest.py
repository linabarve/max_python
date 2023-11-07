       		
       		# largest & smallest number...........


n = int(input("enter the number:"))
m = float('-inf')  
min_val = float('inf')  

for i in range(n):
    a = int(input())
    if a > m:
        m = a
    if a < min_val:
        min_val = a

print("Maximum value:", m)
print("Minimum value:", min_val)

