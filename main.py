# Импортируем библиотеку turtle
import turtle
import math


# Функция для вычисления расстояния между двумя точками
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Функция для рисования точки
def draw_point(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(5)


# Функция для рисования окружности с помощью библиотеки turtle
def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)


# Создаем экземпляр черепашки
t = turtle.Turtle()

# Устанавливаем максимальную скорость анимации
t.speed(0)

# Вводим параметры первой окружности
x1 = -50
y1 = 0
radius1 = 50
# Рисуем первую окружность
draw_circle(t, x1, y1, radius1)

# Вводим параметры второй окружности
x2 = 50
y2 = 0
radius2 = 50
draw_circle(t, x2, y2, radius2)

# Вводим параметры третьей окружности
x3 = 50
y3 = 100
radius3 = 50
draw_circle(t, x3, y3, radius3)

# Вводим параметры четвертой окружности
x4 = -50
y4 = 100
radius4 = 50
draw_circle(t, x4, y4, radius4)

# Вводим параметры первой окружности
x1 = -50
y1 = 0
radius1 = 50
# Рисуем первую окружность
draw_circle(t, x1, y1, radius1)
# Рисуем точку пересечения 1 и 2 окружностей
theta1 = math.acos(
    (radius1 ** 2 - radius2 ** 2 + distance(x1, y1, x2, y2) ** 2) / (2 * radius1 * distance(x1, y1, x2, y2)))
x_intersect_1_2 = x1 + radius1 * math.cos(theta1)
y_intersect_1_2 = y1 + radius1 * math.sin(theta1)
draw_point(t, x_intersect_1_2, y_intersect_1_2)

# Вводим параметры второй окружности
x2 = 50
y2 = 0
radius2 = 50
draw_circle(t, x2, y2, radius2)
# Рисуем точку пересечения 2 и 3 окружностей
theta2 = math.acos(
    (radius2 ** 2 - radius3 ** 2 + distance(x2, y2, x3, y3) ** 2) / (2 * radius2 * distance(x2, y2, x3, y3)))
x_intersect_2_3 = x2 + radius2 * math.cos(math.pi / 2 - theta2)
y_intersect_2_3 = y2 + radius2 * math.sin(math.pi / 2 - theta2)
draw_point(t, x_intersect_2_3, y_intersect_2_3)

# Вводим параметры третьей окружности
x3 = 50
y3 = 100
radius3 = 50
draw_circle(t, x3, y3, radius3)
# Рисуем точку пересечения 3 и 4 окружностей
theta3 = math.acos(
    (radius3 ** 2 - radius4 ** 2 + distance(x3, y3, x4, y4) ** 2) / (2 * radius3 * distance(x3, y3, x4, y4)))
x_intersect_3_4 = x3 + radius3 * math.cos(math.pi - theta3)
y_intersect_3_4 = y3 + radius3 * math.sin(math.pi - theta3)
draw_point(t, x_intersect_3_4, y_intersect_3_4)

# Вводим параметры четвертой окружности
x4 = -50
y4 = 100
radius4 = 50
draw_circle(t, x4, y4, radius4)
# Рисуем точку пересечения 4 и 1 окружностей
theta4 = math.acos(
    (radius4 ** 2 - radius1 ** 2 + distance(x4, y4, x1, y1) ** 2) / (2 * radius4 * distance(x4, y4, x1, y1)))
x_intersect_4_1 = x4 + radius4 * math.cos(-math.pi / 2 - theta4)
y_intersect_4_1 = y4 + radius4 * math.sin(-math.pi / 2 - theta4)
draw_point(t, x_intersect_4_1, y_intersect_4_1)

# t.speed(10)
# Перемещаем черепаху в точку пересечения 1 и 2 окружностей
t.penup()
t.setposition(x_intersect_1_2, y_intersect_1_2)
t.pendown()
# Устанавливаем цвет пера в красный
t.color("red")
t.begin_fill()
# Начальный угол поворота
angle = 90
# Цикл для рисования четвертей окружностей
for _ in range(4):
    # Направляем черепаху в нужное направление (против часовой стрелки)
    t.setheading(math.degrees(theta1) - angle)
    # Рисуем четверть окружности
    t.circle(radius4, - 90)
    # Уменьшаем угол на 10 градусов
    angle -= 90
t.end_fill()

# Площадь фигуры созданной окружностями
range = radius1 + radius2
print(range)
areaSquare = pow(range, 2)
print(areaSquare/4)
areaСircle = math.pi * pow(radius1,2)
print(areaСircle)
areaFigure = areaSquare - areaСircle
print(areaFigure)
turtle.done()
