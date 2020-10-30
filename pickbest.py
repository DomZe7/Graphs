import pandas as pd
import math

data = {
    'subject': [1, 1, 1, 1, 1, 1, 2, 2, 2],
    'lesion': [1, 1, 1, 2, 2, 3, 1, 1, 2],
    'response': [0, 0, 1, 2, 2, 1, 0, 0, 0],
    'metric': [.2, .3, .1, 0, -.1, .2, -.2, -.25, 1]
}

df = pd.DataFrame(data=data)

print(df)

def picker(dataframe):
    df = dataframe.copy()
    data = {
        'subject': [],
        'lesion': [],
        'response': [],
        'metric': []
    }
    subjects = df['subject'].unique()
    for s in subjects:
        temp = df.loc[df['subject']==s]
        mini = math.inf
        for i, r in temp.iterrows():
            if r['metric'] < mini:
                mini = r['metric']
        row = temp.loc[lambda df: df['metric']==mini]
        data['subject'].append(row['subject'].item())
        data['lesion'].append(row['lesion'].item())
        data['response'].append(row['response'].item())
        data['metric'].append(row['metric'].item())
    new = pd.DataFrame(data=data)
    return new
            
picker(df)