import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from bokeh.plotting import figure, show
#import seaborn as sns; sns.set()

author_data = pd.read_csv('databases/GephiMatrix_author_similarity.csv', na_values=[''], keep_default_na=False)

author_list = author_data.iloc[:,0]

m = [None] * (author_list.size)

i = 0
while i < author_list.size:
    m[i] = author_list[i].split(";")
    i += 1
#print(m[0][1 :])
#n = [None] * (author_list.size - 1)

    
i = 0
while i < (author_list.size):
    n = m[i][1 :-1]
    m[i] = n
    i += 1
    
i = 0
while i< author_list.size:
    j= 0
    while j< author_list.size:
        m[i][j] = float(m[i][j])
        j += 1
    i += 1
    

arrayM = np.array(m)
p = figure(x_range = (0, 2), y_range = (0, 2))

p.image(image=[arrayM], x=0, y=0, dw=2, dh=2,palette="Spectral11" )
show(p)


dfM = pd.DataFrame(m)

dfM['sum'] = dfM[list(dfM.columns)].sum(axis=1)

dfM = dfM.sort_values(by='sum', ascending=0)
del dfM['sum']

dfM = dfM.reindex(columns = dfM.index)
mReorder = dfM.as_matrix(columns=None)

arrayMReorder = np.array(mReorder)
arrayMReorder

pReorder = figure(x_range = (0, 2), y_range = (0, 2))
pReorder.image(image=[arrayMReorder], x=0, y=0, dw=2, dh=2,palette="Spectral11" )

show(pReorder)