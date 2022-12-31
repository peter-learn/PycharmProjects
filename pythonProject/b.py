def meiqui(a):
	x = 0
	for i in range(1,a+1):
		x = x + i
	return x
b = int(input())
ans = 0
for j in range(1,b+1):
	ans = ans + meiqui(j)
print(ans)