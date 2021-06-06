import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Даты в 0м столбце, максимальная температура в 1м, минимальная в 3м]

    # Чтение дат, максимальных и минимальных температур
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        try:
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Отсутствуют данные для {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# форматирование диаграммы
plt.title("Максимумы и минимумы температур - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Температура (Фаренгейты)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()