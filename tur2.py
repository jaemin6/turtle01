import turtle
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_collision(x, y):
    return -50 <= x <= 10 and 0 <= y <= 60  # 장애물 범위

goal_x, goal_y = 300, 300

t = turtle.Turtle()
t.penup()
t.goto(-300, -300)
t.setheading(t.towards(goal_x, goal_y))
t.pendown()

while True:
    x, y = t.xcor(), t.ycor()
    if calculate_distance(x, y, goal_x, goal_y) < 20:
        break
    next_x = x + 10 * math.cos(math.radians(t.heading()))
    next_y = y + 10 * math.sin(math.radians(t.heading()))

    if is_collision(next_x, next_y):
        t.left(60)
        t.forward(30)
        t.right(60)
    else:
        t.forward(10)
