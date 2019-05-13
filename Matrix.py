#Paul Ter Rele
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.embed import file_html
from bokeh.resources import CDN

author_data = pd.read_csv('databases/GephiMatrix_author_similarity.csv', na_values=[''], keep_default_na=False)

author_list = author_data.iloc[:,0]

m = [None] * (author_list.size)
author = [None] * (author_list.size)
i = 0
while i < author_list.size:
    m[i] = author_list[i].split(";")
    i += 1
    
    
i = 0
while i < (author_list.size):
    n = m[i][1 :-1]
    author[i] = m[i][0]
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


dfM = pd.DataFrame(m)

dfM['sum'] = dfM[list(dfM.columns)].sum(axis=1)

minimum = 100
maximum = 150

dfMFilter =  dfM[(dfM['sum'] >= minimum ) & (dfM['sum'] <= maximum)]

dfM = dfM.sort_values(by='sum', ascending=0)
del dfM['sum']
del dfMFilter['sum']

dfM = dfM.reindex(columns = dfM.index)
mReorder = dfM.as_matrix(columns=None)
arrayMReorder = np.array(mReorder)


dfMFilter = dfMFilter.reindex(columns = dfMFilter.index)
mFilterReorder = dfMFilter.as_matrix(columns=None)
arrayMFilterReorder = np.array(mFilterReorder)

pReorder = figure(x_range = (0, 2), y_range = (0, 2))
pReorder.image(image=[arrayMReorder], x=0, y=0, dw=2, dh=2,palette="Spectral11" )


html = file_html(pReorder, CDN, "plot")
saveFile = open("MatrixReorder.html","w")
saveFile.write(html)
saveFile.close()

html = file_html(p, CDN, "plot")
saveFile = open("MatrixPlain.html","w")
saveFile.write(html)
saveFile.close()

dfAuthor = pd.DataFrame(author)
dfAuthor = dfAuthor.reindex(index = dfM.index)
authorReorder = dfAuthor[0]
