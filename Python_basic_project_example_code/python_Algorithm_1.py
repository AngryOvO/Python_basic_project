a = int(input('정수 a의 값을 입력하세요 : '))
b = int(input('정수 b의 값을 입력하세요 : '))
c = int(input('정수 c의 값을 입력하세요 : '))

maxsize = a

if maxsize < b :
    maxsize = b
if maxsize < c :
    maxsize = c

print('최댓값은 %d 입니다'%maxsize)
