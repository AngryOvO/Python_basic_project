import turtle ## 터틀 모듈 가져옴

i,j, turtlex, turtley = 0,0,0,0 ## 반복문용 변수 i, j 거북이 좌표 변수 선언

swidth, sheight = 800, 450 ## 프로그램 크기용 변수 선언 및 초기화

turtle.title('거북이로 구구단 출력') ## 타이틀 제목 
turtle.shape('turtle')## 거북이 모양 거북이
turtle.setup(width = swidth + 50, height = sheight +50)
turtle.screensize(swidth,sheight)
turtle.penup()

## 거북이 시작위치 설정
turtlex, turtley = -500,250 
turtle.goto(turtlex,turtley)

##2018038025 정하용

## 구구단 출력구간
for i in range(1,10): ## 1 ~ 9까지 곱할값
    for j in range(2,10):## 2단 ~ 9단까지
        ## 가로줄에 2단~9단까지의 곱이 나와야 해서 반복문을 반대로
        ## i와 j의 숫자만큼 거북이 이동
        turtle.goto(turtlex + 80 * j, turtley - 40*i)
        ## 구구단을 찍을 식
        gugu = str(j) + ' x ' + str(i) + ' =' + str(j*i)
        ## 거북이가 구구단을 찍
        turtle.write(gugu,font=('arial',12,'bold'))


turtle.done()
