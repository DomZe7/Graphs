import pandas as pd
import numpy as np
import plotnine as plt

d = {
    'subject': ['a', 'b', 'c', 'd'],
    'maximal': [-.02, -.1, .05, .25],
    'perpendicular': [0, .15, .40, -.2],
    'product': [.12, .18, .34, -.16],
    'response': ['PR', 'PR', 'SD', 'PD']
}

df = pd.DataFrame(data=d)
