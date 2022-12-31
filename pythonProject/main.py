n=0
n1=0
n2=0
n3=0
n4=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if( i != k ) and (i != j) and (j != k)and(i != 0):
                s = i*100+j*10+k
                print("第",n+1,"组：",s)
                n = n +1
                if s % 2 == 0:
                    n1 += 1
                    if s % 4 == 0:
                        n2 += 1
                    else:
                        n3 += 1
                else:
                    n4 += 1
print("共有：",n,"种，")
print("2",n1)
print("4",n2)
print("b4",n3)
print("b2",n4)