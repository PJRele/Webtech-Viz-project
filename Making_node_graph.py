# -*- coding: utf-8 -*-
"""
Created on Wed May  1 09:03:32 2019

@author: Asaf
"""

import numpy as np
import pandas as pd
import re
import holoviews as hv
import networkx as nx
from holoviews import opts

hv.extension('bokeh')

# declare size and color
defaults = dict(width=400, height=400, padding=0.1)
hv.opts.defaults(
    opts.EdgePaths(**defaults), opts.Graph(**defaults), opts.Nodes(**defaults))
colors = ['#000000']+hv.Cycle('Category20').values

# input CSV file
# check if csv doesn't start with a character, and delete it (i.e. delete starting ;) 
df = pd.read_csv('Given CSVs/GephiMatrix_co-authorship.csv', header=0, delimiter=';')
print(df.tail())
"""
df_edges = pd.read_csv('C:/Users/Asaf/Documents/TU Software/Y3/Q4/DBL HTI Webtevh/Given CSVs/GephiMatrix_co-authorship.csv', skiprows=[0])
df_nodes = hv.Nodes(pd.read_csv('C:/Users/Asaf/Documents/TU Software/Y3/Q4/DBL HTI Webtevh/Given CSVs/GephiMatrix_co-authorship.csv', skiprows=[1:]))
hv_graph = hv.Graph((edges_df, fb_nodes), label='Facebook Circles')

# the graph in networkx format
G = nx.from_pandas_edgelist(Data, create_using=Graphtype)


HF = hv.Graph.from_networkx(G, nx.layout.circular_layout).opts(tools=['hover'])
HF
"""