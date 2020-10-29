import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *

path = r'C:\Users\domin\OneDrive\Desktop\Graphs\Figures\Lollipops'

d = {
    'subject': ['a', 'b', 'c', 'd'],
    'maximal': [-.02, -.1, .05, .25],
    'perpendicular': [0, .15, .40, -.2],
    'product': [.12, .18, .34, -.16],
    'response': ['PR', 'PR', 'SD', 'PD']
}

df = pd.DataFrame(data=d)
df.sort_values(by=['maximal'], inplace=True)
        
gplot = ggplot(aes(x='reorder(subject, maximal)', y='maximal', color='response', label='maximal'), df) + geom_segment(aes(x='subject', xend='subject', y=0, yend='maximal'), color='grey')+ geom_point(size=8)+scale_y_continuous(labels=lambda l: ["%d%%" % (v * 100) for v in l])+ geom_text(color='black', size=6)
color = scale_color_manual(values=['#f52525', '#59db2a', '#dbc62a'])
plot = gplot+color+xlab('Subject')+ylab('Percent Change')+ggtitle('Best Percent Changes in Maximal')
plot.save(filename='tutorial.png', path=path)