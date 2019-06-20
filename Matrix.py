#Paul Ter Rele
#importing various libraries
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
import scipy.sparse as sc

print('done')
#retrieving input data
author_data = pd.read_csv('databases/GephiMatrix_author_similarity.csv', na_values=[''], keep_default_na=False)

#putting all the data into a matrix m
author_list = author_data.iloc[:,0]

m = [None] * (author_list.size)
author = [None] * (author_list.size)
i = 0
while i < author_list.size:
    m[i] = author_list[i].split(";")
    i += 1
    
#erasing indeces from matrix m and puting them in list author
i = 0
while i < (author_list.size):
    n = m[i][1 :-1]
    author[i] = m[i][0]
    m[i] = n
    i += 1
    
#turning string values in matrix m into floats    
i = 0
while i< author_list.size:
    j= 0
    while j< author_list.size:
        m[i][j] = float(m[i][j])
        j += 1
    i += 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
codes = ['F','E','D','C','B','A','9','8','7','6','5','4','3','2','1','0']
colors = [None] * 4096

i = 0
j = 0
r = 0
while r < 16:
    while i < 16:
        while j < 16:
            code = codes[r] + codes[i] + codes[i] + codes[j] + codes[i] + codes[j]
            colors[j + 16*i + 256*r] = ('#' + code)
            j += 1
        i += 1
        j = 0
    r += 1
    i = 0

#print(colors)
palette = "Spectral11"
paletteRed = colors
TOOLTIPS = [
    ("value", "@image"),
    #("authors", "$xauthor"),
    #("index", "$index")
]

#turning matrix m into an Array arrayM     
arrayM = np.array(m)
cscM = sc.coo_matrix(arrayM).tocsc()
cscM = sc.csgraph.reverse_cuthill_mckee(cscM)

#creating a bokeh plot p that shows the pure data in matrix m
p = figure(x_range = (0, 2), y_range = (0, 2),tooltips = TOOLTIPS, title = "Raw data")
pReorder = figure(x_range = (0, 2), y_range = (0, 2),tooltips = TOOLTIPS, title = "Reorder data")
pAlpha = figure(x_range = (0, 2), y_range = (0, 2),tooltips = TOOLTIPS, title = "Alpha data")
pCsc = figure(x_range = (0, 2), y_range = (0, 2),tooltips = TOOLTIPS, title = "Cluster data")

pRed = figure(x_range = (0, 2), y_range = (0, 2),tooltips = TOOLTIPS, title = "Raw data")
pReorderRed = figure(x_range = (0, 2), y_range = (0, 2),tooltips = TOOLTIPS, title = "Reorder data")
pAlphaRed = figure(x_range = (0, 2), y_range = (0, 2),tooltips = TOOLTIPS, title = "Alpha data")
pCscRed = figure(x_range = (0, 2), y_range = (0, 2),tooltips = TOOLTIPS, title = "Cluster data")

p.image(image=[arrayM], x=0, y=0, dw=2, dh=2,palette=palette )
pRed.image(image=[arrayM], x=0, y=0, dw=2, dh=2,palette=paletteRed )

#turing matrix m into dataframe dfM
dfM = pd.DataFrame(m)

#adding sum column to dataframe dfM
dfM['sum'] = dfM[list(dfM.columns)].sum(axis=1)

#sorting rows of dataframe dfM by sum column
dfM = dfM.sort_values(by='sum', ascending=0)
del dfM['sum']
#del dfMFilter['sum']

#reordering columns of dataframe dfM by the indeces of the columns
dfM = dfM.reindex(columns = dfM.index)
mReorder = dfM.as_matrix(columns=None)
arrayMReorder = np.array(mReorder)

#reordering list author by the order of dfM
dfAuthor = pd.DataFrame(author)
dfAuthor = dfAuthor.reindex(index = dfM.index)
authorReorder = list(dfAuthor[0])

pReorder.image(image = [arrayMReorder], x=0, y=0, dw=2, dh=2,palette=palette )
pReorderRed.image(image = [arrayMReorder], x=0, y=0, dw=2, dh=2,palette=paletteRed )

#alphabetical reordering
dfAuthorAlpha = dfAuthor.sort_values(by = 0)
dfMAlpha = dfM.reindex(columns = dfAuthorAlpha.index, index = dfAuthorAlpha.index)
ArrayMAlpha = np.array(dfMAlpha)
pAlpha.image(image=[ArrayMAlpha], x=0, y=0, dw=2, dh=2,palette=palette )
pAlphaRed.image(image=[ArrayMAlpha], x=0, y=0, dw=2, dh=2,palette=paletteRed )

#reorder
cscM = sc.coo_matrix(arrayM).tocsc()
cscM = sc.csgraph.reverse_cuthill_mckee(cscM)
cscM = cscM.tolist()
dfMCsc = dfM.reindex(columns = cscM, index = cscM)
ArrayMCsc = np.array(dfMCsc)
pCsc.image(image=[ArrayMCsc], x=0, y=0, dw=2, dh=2,palette=palette )
pCscRed.image(image=[ArrayMCsc], x=0, y=0, dw=2, dh=2,palette=paletteRed )

#saving plot as html file
##html = file_html(pReorder, CDN, "plot")
#saveFile = open("MatrixReorder.html","w")
#saveFile.write(html)
#saveFile.close()


#display plots
show(pCsc)
show(pAlpha)
show(pReorder)
show(p)

show(pCscRed)
show(pAlphaRed)
show(pReorderRed)
show(pRed)