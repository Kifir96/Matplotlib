import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Номера столбцев и их названия
    for x, y in enumerate(header_row):
        print(x, y)

    lats, lons, scans = [], [], []
    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        scans.append(float(row[8]))

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.1*scan for scan in scans],
        'color': scans,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Мощь пожара'}
    }
}]
my_layout = Layout(title='Пожары в мире')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')