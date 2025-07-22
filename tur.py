import turtle

# 스크린 생성
s = turtle.getscreen()
# 거북이 변수 지정
t = turtle.Turtle()
t.shape("turtle")
t.color("green")

# 왼쪽 아래(-300, -300)로 이동
t.penup()
t.goto(-300, -300)
t.pendown()

# 오른쪽 위(300, 300)로 이동
t.goto(300, 300)
