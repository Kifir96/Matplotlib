import matplotlib.pyplot as plt

x_values = list(range(1, 1000))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values[:500], y_values[:500], c=y_values[:500],
           cmap=plt.cm.Wistia, s=10)
ax.scatter(x_values[500:], y_values[500:], c='green', s=10)


# Назначение заголовка диаграмм и меток осей
ax.set_title("Кубы чисел", fontsize=24)
ax.set_xlabel("Значения", fontsize=14)
ax.set_ylabel("Кубы значений", fontsize=14)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона для каждой оси
ax.axis([0, 1000, 0, 1000000000])

plt.show()
# для сохранения в файл:
# plt.savefig('имя_файла.png', bbox_inches='tight')