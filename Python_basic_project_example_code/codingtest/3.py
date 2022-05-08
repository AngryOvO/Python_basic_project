t = int(input("t = "))

a = []
b = ""
b2 = ""

for i in range(0,t):
    b = input("a = ")
    b2 = b.upper()
    a.append(b2)
    b = ""
    b2 = ""


for i in range(0,len(a)):
    print("%d] %s"%(i+1,a[i]))
