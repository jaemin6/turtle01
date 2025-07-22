import turtle
import math
import tkinter as tk
from tkinter import messagebox

# 거리 계산
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 장애물 충돌 감지 - 범위 설정
def is_collision(x, y):
    padding = 15  # 여유 범위
    return (-50 - padding) <= x <= (10 + padding) and (0 - padding) <= y <= (60 + padding)

# 출발, 도착 좌표
start_x, start_y = -300, -300
goal_x, goal_y = 300, 300

# 터틀 설정
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("sky blue")
t.speed(1)

# 장애물 그리기
def draw_obstacle():
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(4):
        t.forward(60)
        t.left(90)
    t.end_fill()
    t.penup()

draw_obstacle()

# 출발점 이동
t.penup()
t.goto(start_x, start_y)
t.setheading(t.towards(goal_x, goal_y))
t.pendown()

# 이동
while True:
    x, y = t.xcor(), t.ycor()

    # 도착 체크
    if calculate_distance(x, y, goal_x, goal_y) < 20:
        break

    # 다음 위치 예측
    next_x = x + 10 * math.cos(math.radians(t.heading()))
    next_y = y + 10 * math.sin(math.radians(t.heading()))

    if is_collision(next_x, next_y):
        # 장애물 근처이면 오른쪽으로 우회
        t.left(90)
        t.forward(70)
        t.right(90)
        t.setheading(t.towards(goal_x, goal_y))
    else:
        t.forward(10)

# 목적지점 만들기
t.penup()
t.goto(goal_x, goal_y)
t.dot(20, "blue")

# 거리 출력
total_distance = calculate_distance(start_x, start_y, goal_x, goal_y)
print(f"총 거리: {total_distance:.2f}")

# 팝업 메시지
root = tk.Tk()
root.withdraw()
messagebox.showinfo("도착!", "도착했습니다!")

