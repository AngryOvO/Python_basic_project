t = int(input("t = "))

a = []
b = ""
b2 = ""

for i in range(0,t):
    b = input("a = ")
    for j in range(len(b)-1,-1,-1):
        b2 = b2 + (b[j])
    a.append(b2)
    b = ""
    b2 = ""


for i in range(0,len(a)):
    print("%d] %s"%(i+1,a[i]))
