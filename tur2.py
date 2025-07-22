import turtle
import math
import tkinter as tk
from tkinter import messagebox

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_collision(x, y):
    # 장애물 영역 (-50,0) ~ (10,60)
    return -50 <= x <= 10 and 0 <= y <= 60

# 출발지와 목적지 좌표
start_x, start_y = -300, -300
goal_x, goal_y = 300, 300

# Turtle 설정
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

# 거북이 출발 지점으로 이동
t.goto(start_x, start_y)
t.setheading(t.towards(goal_x, goal_y))  # 목적지를 바라보도록 방향 설정
t.pendown()

# 이동 시작
while True:
    x, y = t.xcor(), t.ycor()

    # 목적지에 거의 도착했으면 종료
    if calculate_distance(x, y, goal_x, goal_y) < 20:
        break

    # 다음 위치 예상
    next_x = x + 10 * math.cos(math.radians(t.heading()))
    next_y = y + 10 * math.sin(math.radians(t.heading()))

    # 충돌 감지
    if is_collision(next_x, next_y):
        t.left(60)
        t.forward(30)
        t.right(60)
    else:
        t.forward(10)

# 목적지 좌표 찍기 (시각화용)
t.penup()
t.goto(goal_x - 10, goal_y - 10)
t.dot(20, "green")
t.goto(goal_x, goal_y)

# 거리 출력
total_distance = calculate_distance(start_x, start_y, goal_x, goal_y)
print(f"두 점 ({start_x}, {start_y}) 와 ({goal_x}, {goal_y}) 사이의 거리는 {total_distance:.2f} 입니다.")

# 도착 메시지 박스
root = tk.Tk()
root.withdraw()  # tkinter 창 숨기기
messagebox.showinfo("도착!", "도착했습니다!")
