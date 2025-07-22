import turtle

# 스크린 생성
s = turtle.getscreen()
# 거북이 변수 지정
t = turtle.Turtle()
t.shape("turtle")
t.color("sky blue")

t.penup()
t.goto(-50, 0)  # 장애물 시작 위치 (화면 가운데)
t.pendown()
t.fillcolor("red")
t.begin_fill()
for _ in range(4):
    t.forward(60)  
    t.left(90)  # 사각형은 90
t.end_fill()

# 왼쪽 아래 (-300, -300)로 이동 (출발점)
t.penup()
t.goto(-300, -300)
t.pendown()

# 오른쪽 위(300, 300)로 이동 (목적지)
t.goto(-60, 10)
# 장애물 회피
t.goto(-100, 80)
