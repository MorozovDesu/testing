import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox, Button
from matplotlib.patches import PathPatch
from matplotlib.path import Path

def plot_figure_and_calculate_area(ax, r):
    ax.clear()
    
    # Центры окружностей
    centers = [(r, r), (-r, r), (-r, -r), (r, -r)]
    # Рисуем окружности
    for center in centers:
        circle = plt.Circle(center, r, edgecolor='black', facecolor='none')
        ax.add_patch(circle)
    
    # Настраиваем пределы осей и равные масштабы
    ax.set_xlim(-2*r, 2*r)
    ax.set_ylim(-2*r, 2*r)
    ax.set_aspect('equal', 'box')
    # Подписи осей
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # Координаты вершин дуг пересечения
    angles = np.linspace(0, np.pi/2, 100)
    # Верхняя левая дуга
    upper_left_arc = np.column_stack((r - r * np.cos(angles), r - r * np.sin(angles)))
    # Верхняя правая дуга
    upper_right_arc = np.column_stack((-r + r * np.cos(angles), r - r * np.sin(angles)))
    # Нижняя правая дуга
    lower_right_arc = np.column_stack((-r + r * np.cos(angles), -r + r * np.sin(angles)))
    # Нижняя левая дуга
    lower_left_arc = np.column_stack((r - r * np.cos(angles), -r + r * np.sin(angles)))
    # Создаем путь для заштрихованной области
    vertices = np.concatenate([upper_left_arc, upper_right_arc[::-1], lower_right_arc, lower_left_arc[::-1]])
    codes = [Path.MOVETO] + [Path.LINETO]*(len(vertices) - 1)
    
    path = Path(vertices, codes)
    patch = PathPatch(path, facecolor='red', alpha=0.5)
    ax.add_patch(patch)
    
    # Вычисляем площадь заштрихованной области
    area_circle = np.pi * (r / 2 )** 2
    overlap_area = r ** 2 
    shaded_area =  overlap_area - area_circle
    print(area_circle)
    print(overlap_area)
    ax.set_title(f'Заштрихованная область: {shaded_area:.2f} кв.см')
    plt.draw()
    return shaded_area

def submit_radius(event):
    try:
        r = float(text_box.text)
        if 0 < r <= 100000:
            plot_figure_and_calculate_area(ax, r)
    except ValueError:
        pass

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Начальные значения
r = 5
plot_figure_and_calculate_area(ax, r)

# Добавляем текстовое поле для ввода радиуса
axbox = plt.axes([0.2, 0.05, 0.55, 0.075])
text_box = TextBox(axbox, 'Радиус (см):', initial=str(r))

# Добавляем кнопку для подтверждения ввода
axbutton = plt.axes([0.8, 0.05, 0.15, 0.075])
button = Button(axbutton, 'Рассчитать')
button.on_clicked(submit_radius)

plt.show()



# Отображение фигур в данном коде осуществляется с использованием библиотеки Matplotlib. Более конкретно, используются следующие классы и функции из этой библиотеки:

# plt.subplots(): создает новый объект Figure и связанный с ним объект Axes, который представляет собой область построения графика.
# ax.clear(): очищает текущую область построения.
# plt.Circle(): создает объект окружности с заданными параметрами (центр, радиус, цвет границы, цвет заливки).
# ax.add_patch(): добавляет объект окружности на область построения.
# ax.set_xlim(), ax.set_ylim(): устанавливают пределы осей X и Y.
# ax.set_aspect(): устанавливает равные масштабы по осям.
# ax.set_xlabel(), ax.set_ylabel(): устанавливают подписи осей X и Y.
# np.linspace(): создает массив значений, равномерно распределенных между двумя заданными значениями.
# np.column_stack(): объединяет массивы по колонкам.
# Path(): создает объект пути, определяемый последовательностью вершин и кодами команд (MOVETO, LINETO и т. д.).
# PathPatch(): создает объект патча пути, который может быть добавлен на область построения.
# ax.set_title(): устанавливает заголовок графика.
# plt.draw(): перерисовывает график.
# plt.subplots_adjust(): настраивает расположение области построения и других элементов на холсте Figure.
# TextBox(): создает текстовое поле для ввода данных.
# Button(): создает кнопку на области построения.
# button.on_clicked(): устанавливает функцию-обработчик для события клика на кнопку.
# Таким образом, отображение фигур осуществляется при помощи классов Figure и Axes, а также методов и функций из библиотеки Matplotlib.