##변수 선언 부분##

year = 0##정수형 타입으로 연도 변수 생성

##메인 코드 부분 ##
if __name__ == "__main__":
    year = int(input("연도를 입력하세요 : "))## 연도 입력 받고

    ##2018038025 정하용##

    ## 윤년 경우
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    
    
        print("%d년은 윤년입니다." % year)## 윤년이 맞을시 출력

    else :
        print("%d년은 윤년이 아닙니다." % year)## 아닐시 출력

    
    
