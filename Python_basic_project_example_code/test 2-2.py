import turtle ##turtle 모듈 가져옴
import random ##random 모듈 가져옴

turtle1, turtle2, turtle3 = [None] *3 ## 거북이 정보 담을 변수 세개 선언

t1x, t1y, t2x, t2y, t3x, t3y = 0,0,0,0,0,0 ##거북이 좌표 (x y) 여섯개 선언

swidth , sheight = 300,300 ## 프로그램 사이즈


turtle.title("거북이 서로 만나게 하기") ## 거북이 타이틀 제목
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)## 스크린 사이즈

##각 거북이 정보 설정 1번 - 빨강 , 2번 - 초록, 3번 - 파랑
turtle1 = turtle.Turtle('turtle'); turtle1.color('red'); turtle1.penup()
turtle2 = turtle.Turtle('turtle'); turtle2.color('green'); turtle2.penup()
turtle3 = turtle.Turtle('turtle'); turtle3.color('blue'); turtle3.penup()

##거북이 시작위치 설정 및 거북이 속도 설정
turtle1.goto(-50,-50); turtle2.goto(0,0); turtle3.goto(50,50); 
turtle1.speed(1000000); turtle2.speed(1000000); turtle3.speed(1000000)

##무한루프 시작
##2018038025 정하용
while True:
    ##거북이들이 랜덤하게 이동하게 랜덤한 각도에 랜덤한 길이만큼 이동
    angle = random.randrange(0,360)
    dist = random.randrange(1,50)
    turtle1.left(angle); turtle1.forward(dist)
    angle = random.randrange(0,360)
    dist = random.randrange(1,50)
    turtle2.left(angle); turtle2.forward(dist)
    angle = random.randrange(0,360)
    dist = random.randrange(1,50)
    turtle3.left(angle); turtle3.forward(dist)

    ## 각 변수에 거북이 위치 저장
    t1x = turtle1.xcor(); t1y = turtle1.ycor()
    t2x = turtle2.xcor(); t2y = turtle2.ycor()
    t3x = turtle3.xcor(); t3y = turtle3.ycor()

    ##거북이 위치정보가 저장된 변수가 서로 같다면
    if (t1x == t2x and t1y == t2y) or\
       (t2x == t3x and t2y == t3y) or\
       (t3x == t1x and t3y == t1y):
        ##거북이 크기를 세배로 키우고 무한루프 종료
        turtle1.turtlesize(3); turtle2.turtlesize(3); turtle3.turtlesize(3)
        break

turtle.done()
       
    
