import turtle

## 변수 선언 부분 ##

num = 0 ## 입력 받을 정수형 변수
swidth, sheight = 1000, 300 ## 거북이가 생성될 윈도우창의 크기
curX, curY = 0,0 ## 거북이의 현재 위치

## 메인 코드 부분 ##

if __name__ == "__main__":

    ##2018038025 정하용##

    turtle.title('거북이로 2진수 표현하기') ## 거북이 그래픽 타이틀 제목
    turtle.shape('turtle')## 거북이 모양 설정
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()## 거북이 이동시 선을 그리지 않음
    turtle.left(90)##거북이 왼쪽으로 90도 회전 > 거북이가 하늘을 보게

    num = int(input("숫자를 입력하세요(10진수) : "))## 정수 입력받는 구간
    binary = bin(num)## 입력받은 정수의 2진수형을 binary 변수에 저장
    curX = swidth / 2##거북이 위치를 윈도우창의 오른쪽 끝으로 시작
    curY = 0

    for i in range(len(binary) -2):## 반복문 시작 2진수의 길이 만큼 반복
        turtle.goto(curX, curY)
        if num & 1:## 2진수의 1에 해당하는 경우
            turtle.color('red')## 거북이 색깔 빨강
            turtle.turtlesize(2)## 거북이 크기 2
        else :## 2진수의 0에 해당하는 경우
            turtle.color('blue')## 거북이 색깔 파랑
            turtle.turtlesize(1)## 거북이 크기 1
        turtle.stamp()## 거북이를 현재 위치에 찍음
        curX -= 50## 거북이의 위치를 50만큼 왼쪽으로 옮긴다
        num >>= 1## 숫자를 오른쪽을 1 시프트

turtle.done()
