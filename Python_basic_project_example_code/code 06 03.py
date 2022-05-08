i, hap = 0,0

num1,num2,num3 = 0,0,0

num1 = int(input("시작값을 입력하세요 : "))
num2 = int(input("끝값을 입력하세요 : "))
num3 = int(input("중간값을 입력하세요 : "))
           

for i in range(num1,num2+1,num3):
    hap = hap + i

print("%d 부터 %d까지 %d씩 더하면 %d 입니다."%(num1,num2,num3,hap))
