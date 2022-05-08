import random ##랜덤 모듈 가져옴

a,b,c,d,e,f = 0,0,0,0,0,0 ## 변수 6개 선언 및 초기화
count = 0 ## 주사위 던진 횟수 카운트할 변수 선언
countonetosix = 0 ## 연속된 숫자가 나온 횟수 카운트할 변수 선언

while True:
    count = count + 1 ## 반복 횟수 카운트
    
 ## 1~6 사이의 숫자 랜덤하게 뽑음 
    a = random.randint(1,7)
    b = random.randint(1,7)
    c = random.randint(1,7)
    d = random.randint(1,7)
    e = random.randint(1,7)
    f = random.randint(1,7)
    
## 2018038025 정하용

## 1~6의 연속번호가 나왔을때 
    if(a == 1 and b == 2 and c == 3 and d == 4 and e == 5 and f == 6) or\
         (a == 2 and b == 3 and c == 4 and d == 5 and e == 6 and f == 1) or\
         (a == 3 and b == 4 and c == 5 and d == 6 and e == 1 and f == 2) or\
         (a == 4 and b == 5 and c == 6 and d == 1 and e == 2 and f == 3) or\
         (a == 5 and b == 6 and c == 1 and d == 2 and e == 3 and f == 4) or\
         (a == 6 and b == 1 and c == 2 and d == 3 and e == 4 and f == 5):
        countonetosix = countonetosix + 1 ## 연속숫자 나온 횟수 카운트

    if a == b == c == d == e == f : ## 모든 숫자가 같을때
        print("6개 주사위가 모두 동일한 숫자가 나옴 --> %d %d %d %d %d %d"%(a,b,c,d,e,f))
        print("6개가 동일한 숫자가 나올 때 까지 주사위를 던진 횟수 --> %d"%count)
        print("6개가 동일한 숫자가 나올 때 까지, 1~6의 연속번호가 나온 횟수 --> %d"%countonetosix)
        break;
    
