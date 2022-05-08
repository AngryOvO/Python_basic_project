import turtle
import random



## 2018038025 정하용 ##
def screenRightClick(x,y):

    global r, g, b

    r = random.random()
    g = random.random()
    b = random.random()

    tSize = random.randrange(1,10) ## 거북이 크기 1~10 사이 랜덤
    tAngle = random.randrange(0,361) ## 거북이 각도0도 ~ 360도로 랜덤
    
    turtle.shapesize(tSize)## 크기 설정
    turtle.color((r,g,b))## 색깔 설정
    turtle.right(tAngle)## 각도 설정

    turtle.pendown()
    turtle.goto(x,y)
    turtle.pencolor(r,g,b)
    turtle.stamp()## 거북이 찍음
    turtle.penup()


## 변수 선언 부분##

r,g,b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##

turtle.title("거북이 도장 찍기")
turtle.shape("turtle")
turtle.onscreenclick(screenRightClick,3)


turtle.done
             
