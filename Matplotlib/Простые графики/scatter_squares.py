import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# # или:
# ax.scatter(x_values, y_values, c='red', s=10)
# или:
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# Назначение заголовка диаграмм и меток осей
ax.set_title("Квадраты чисел", fontsize=24)
ax.set_xlabel("Значения", fontsize=14)
ax.set_ylabel("Квадраты значений", fontsize=14)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])

plt.show()
# для сохранения в файл:
# plt.savefig('имя_файла.png', bbox_inches='tight')