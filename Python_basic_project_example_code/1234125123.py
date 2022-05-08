def cal(var1, var2 , oper):

    result = 0

    if oper == '+':
        result = a + b
    elif oper == '-':
        result = a - b
    elif oper == '*':
        result = a * b
    elif oper == '/':
        result = a / b
    elif oper == '**':
        result = a ** b

    return result

a = int(input("첫 번째 수를 입력하세요 :"))
oper = input("계산을 입력하세요 (+,-,*,/,**) :")
b = int(input("두 번째 수를 입력하세요 :"))

if oper == '/' and b == 0:
    print("error! 0으로는 나누면 안됩니다~")

res = cal(a,b,oper)

print("## 계산기 : %d %s %d = %d" % (a, oper, b, res))
