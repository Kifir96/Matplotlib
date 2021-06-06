import csv

from matplotlib import pyplot as plt

filename = 'data/diagram.csv'
with open(filename) as f:
    reader = csv.reader(f)
    percents, animal_types = [], []
    for row in reader:
        percent = row[0]
        animal_type = row[1]
        percents.append(percent)
        animal_types.append(animal_type)

plt.style.use('seaborn')
fig, ax = plt.subplots()
explode = (0, 0.2, 0, 0)
ax.pie(percents, explode=explode, labels=animal_types, autopct='%1.0f%%',
       shadow=True, startangle=90)
ax.axis('equal')

plt.show()