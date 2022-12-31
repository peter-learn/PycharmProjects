import math
a = []
t = 1
x = ""
maxn = []
maxm = []
ans = 0
n = int(input())

for i in range(1,int(math.sqrt(n))+1):
    if n == 1:
        break
    if n % i == 0:
        a.append(i)
print(a)
if a[0] == 1:
    a.remove(1)
for i in range(len(a)-1):
    if a[i] + 1 == a[i + 1]:
        t = t + 1
        maxm.append(a[i])
    else:
        maxm.append(a[i])
        if len(maxn) < len(maxm):
            maxn = maxm
        ans = max(ans,t)
        t = 1
        maxm = []
ans = max(ans,t)
print(ans)
for j in maxn:
    x = x + str(j) + "*"
print(x[:-1])