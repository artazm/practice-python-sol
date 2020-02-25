# Birthday Plot
import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


with open('info.json', 'r') as f:
    birthday = json.load(f)

blist = []
for k, v in birthday.items():
    blist.append(v[0:2])
blist.sort()
c = Counter(blist)

output_file('plot.html')
x_categories = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
x = list(c.elements())
y = list(c.values())

p = figure(x_range = x_categories)
p.vbar(x = x, top = y, width = 0.5)

show(p)


