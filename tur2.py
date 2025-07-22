import turtle
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_collision(x, y):
    return -50 <= x <= 10 and 0 <= y <= 60  # 장애물 범위

# 목적지 좌표
goal_x, goal_y = 300, 300

# 거북이 출발지 이
t = turtle.Turtle()
t.penup()
t.goto(-300, -300)
t.setheading(t.towards(goal_x, goal_y))  # 목적지 설정
t.pendown()

while True:
    x, y = t.xcor(), t.ycor()                                   # 현재 위치 (x, y) 저장
    if calculate_distance(x, y, goal_x, goal_y) < 20:           # 목적지와의 거리가 20보다 작으면 반복 종료
        break
    next_x = x + 10 * math.cos(math.radians(t.heading()))       # 다음 이동할 좌표 계산, 현재 방향에서 10만큼
    next_y = y + 10 * math.sin(math.radians(t.heading()))

    if is_collision(next_x, next_y):
        t.left(60)
        t.forward(30)
        t.right(60)
    else:
        t.forward(10)
