# # 도전문제 챕터 1의 "안녕하세요?"를 화면에 출력해보자.
# print("안녕하세요?")

# # 도전문제 "Programming에 입문하신 것을 축하드립니다."를 출력해보자.
# print("Programming에 입문하신 것을 축하드립니다.")

# # 도전문제 파이썬의 IDLE를 이용하여 다음과 같은 계산을 해보자. 입니다만, VS Code를 이용해서 코딩하고 실행해보겠습니다.
# print(3.141592 * 10.0 * 10.0)

# # 도전문제 두번째.. (1/100)*1234를 계산하는 코딩을 하고 실행해보겠습니다.
# print((1/100)*1234)

#위의 코딩 한 부분을 실행시키지 않는 방법은 뭐가 있을까요?
#이렇게 마우스로 드래그해서 키보드의 Ctrl키를 누른상태에서 키보드 우측 쉬프트 좌측에 있는 슬레쉬를 누르면 전체가 주석처리됩니다.

# 실행되는 것없지요?
# 도전문제 거북이를 움직여서 정삼각형을 그려보자. 회전하는 각도를 몇 도로 하여야 하는가?
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# t.forward(100) # 100 픽셀만큼 직진(이동 길이 즉, 각 변의 길이)
# t.left(12)     # 120도 회전 (회전각도 즉, 외각이 120도를 이뤄야 정삼각형 내각 60도가 만들어지지요?)
# t.forward(100) # 100 픽셀만큼 직진 
# t.left(120)    # 120도 회전
# t.forward(100) # 100 픽셀만큼 직진
# t.left(120)    # 120도 회전
# t.exitonclick() # 이부분이 없으면 Turtle Graphic 화면이 실행되었다가 바로 닫혀서 확인하기 어렵습니다. 잠시 멈추는 부분입니다.

# 두번째 거북이를 움직여서 정사각형을 그려보자. 회전하는 각도는 몇 각도로 하여야 할까?
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# t.forward(100)    # 100 픽셀만큼 직진(이동 길이 - 각 변의 길이) 
# t.left(90)        # 90도 회전
# t.forward(100)    # 100 픽셀만큼 직진
# t.left(90)        # 90도로 회전
# t.forward(100)    # 100 픽셀만큼 직진
# t.left(90)        # 90도로 회전
# t.forward(100)    # 100 픽셀만큼 직진
# t.left(90)        # 90도로 회전
# t.exitonclick()   # 잠시 멈춤

# 도전문제 화살표를 움직여서 6각형을 그려보자. 회전하는 각도를 몇 도로  하여야 할까?
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.exitonclick()