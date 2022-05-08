i,k,heartNum = 0,0,0 ## 반복용 변수 i ,k와 하트의 개수를 담을 변수 세개 선언
numStr, ch, heartStr = "","",""##입력받은 숫자와 하트를 저장할 변수선언

numStr = input("숫자를 여러 개 입력하세요 : ") ## 숫자로 구성된 문자열 입력받음
print("")
i=0## 반복문에서 사용할 변수
ch = numStr[i]##첫 번째 숫자를 ch 저장
while True:## 무한루프 시작
    heartNum = int(ch) ## 숫자의 개수는 ch에 저장된 숫자의 정수형태
##2018038025 정하용
    heartStr = "" ## 하트를 담을 문자열 초기화
    for k in range(0, heartNum): ## 숫자의 크기만큼 반복 
        heartStr += "\u2665"## 문자열에 하트 입력
        k+=1##증감식

    print(heartStr) ## 문자열 출력

    i+=1 
    if(i>len(numStr)-1):
        break ## 문자열 길이가 i보다 작으면 루프 종료

    ch=numStr[i] ## ch에 다음 숫자 입력
