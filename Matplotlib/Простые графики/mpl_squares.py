import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Назначение заголовка диаграмм и меток осей
ax.set_title("Квадраты чисел", fontsize=24)
ax.set_xlabel("Значения", fontsize=14)
ax.set_ylabel("Квадраты значений", fontsize=14)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)
plt.show()