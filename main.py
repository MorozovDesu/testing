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
    area_circle = np.pi * r**2
    overlap_area = 4 * (area_circle/4 - 0.5*r**2 + 0.5*r**2*np.sin(np.pi/4))
    shaded_area = 4 * area_circle - overlap_area
    
    ax.set_title(f'Заштрихованная область: {shaded_area:.2f} кв.см')
    plt.draw()
    return shaded_area

def submit_radius(event):
    try:
        r = float(text_box.text)
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
text_box = TextBox(axbox, 'Радиус:', initial=str(r))

# Добавляем кнопку для подтверждения ввода
axbutton = plt.axes([0.8, 0.05, 0.1, 0.075])
button = Button(axbutton, 'Ввод')
button.on_clicked(submit_radius)

plt.show()
