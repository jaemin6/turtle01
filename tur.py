import turtle
import math
import tkinter as tk
from tkinter import messagebox

# 거리 계산 함수
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 장애물 충돌 감지 (더 넓은 범위로 체크)
def is_collision(x, y):
    padding = 30  # 안전 여유 거리
    return (-50 - padding) <= x <= (10 + padding) and (0 - padding) <= y <= (60 + padding)

# 출발지와 목적지점 설정
start_x, start_y = -300, -300
goal_x, goal_y = 300, 300

# 거북이 설정
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("sky blue")

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

# 출발 위치로 이동
t.penup()
t.goto(start_x, start_y)
t.setheading(t.towards(goal_x, goal_y))
t.pendown()

# 장애물 회피 후 목적지까지 이동
while True:
    x, y = t.xcor(), t.ycor()

    # 도착 조건
    if calculate_distance(x, y, goal_x, goal_y) < 20:
        break

    # 다음 위치 계산 (작게 이동)
    next_x = x + 5 * math.cos(math.radians(t.heading()))
    next_y = y + 5 * math.sin(math.radians(t.heading()))

    if is_collision(next_x, next_y):
        # 충분히 여유 있게 장애물 우회
        t.left(90)
        t.forward(80)
        t.right(90)
        t.setheading(t.towards(goal_x, goal_y))
    else:
        t.forward(5)

# 목적지점 표시
t.penup()
t.goto(goal_x, goal_y)
t.dot(20, "green")

# 거리 출력
total_distance = calculate_distance(start_x, start_y, goal_x, goal_y)
print(f"총 거리: {total_distance:.2f}")

# 도착 표시
root = tk.Tk()
root.withdraw()
messagebox.showinfo("도착!", "도착!")
