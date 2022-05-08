t = int(input("t = "))

a = []
b = []

for i in range(0,t):
    a.append(int(input("a = ")))

for i in range(0,t):
    b.append(int(input("b = ")))

for i in range(0,t):
    print("%d] = %d  %d" % (i+1, a[i]//b[i], a[i]%b[i]))

