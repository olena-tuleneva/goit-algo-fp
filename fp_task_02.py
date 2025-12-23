import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return

    # Обчислення кінцевої точки гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малювання гілки
    plt.plot([x, x_end], [y, y_end], linewidth=depth, color="green")

    # Рекурсивне малювання лівої та правої гілок
    new_length = length * 0.7
    draw_branch(x_end, y_end, new_length, angle + np.pi / 4, depth - 1)
    draw_branch(x_end, y_end, new_length, angle - np.pi / 4, depth - 1)


# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis("off")

# Можливість задати глибину рекурсії користувачу
depth = int(input("Введіть рівень рекурсії: "))

# Початкові параметри дерева
start_x = 0
start_y = -1
start_length = 1
start_angle = np.pi / 2

draw_branch(start_x, start_y, start_length, start_angle, depth)

plt.show()
