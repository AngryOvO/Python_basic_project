t = int(input("t = "))

a = []
c = []

for i in range(0,t):
    a.append(int(input("a = ")))

sum = 0

for i in range(0,len(a)):
    for j in range(0,a[i]+1):
        sum = sum + j

    c.append(sum)
    sum = 0

for i in range(0,len(c)):
    print("%d] %d" % (i+1, c[i]))
