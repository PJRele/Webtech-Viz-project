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
""""
# declare size and color
defaults = dict(width=400, height=400, padding=0.1)
hv.opts.defaults(
    opts.EdgePaths(**defaults), opts.Graph(**defaults), opts.Nodes(**defaults))
colors = ['#000000']+hv.Cycle('Category20').values
"""
##################################
# test
Data = open('Given CSVs/GephiMatrix_co-authorship.csv', "r")
next(Data, None)  # skip the first line in the input file
Graphtype = nx.Graph()

G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype,
                      nodetype=int, data=(('weight', float),))
hv_G = hv.Graph.from_networkx(G, nx.layout.circular_layout).opts(tools=['hover'])
#fig = hv.render(hv_G)
#print('Figure: ', fig)
hv.output(hv_G, fig='png')
#############################

"""
# input CSV file
df = pd.read_csv('Given CSVs/GephiMatrix_co-authorship.csv', header=0, delimiter=';')
df_shape = df.shape
print("df shape: ", df_shape)
# 1053 nodes
df_edges = pd.read_csv('Given CSVs/GephiMatrix_co-authorship.csv')
print(df_edges)


df_nodes = hv.Nodes(pd.read_csv('Given CSVs/GephiMatrix_co-authorship.csv', skiprows=[1:df_shape[1]]))

hv_graph = hv.Graph((edges_df, fb_nodes), label='Facebook Circles')


# the graph in networkx format
G = nx.from_pandas_edgelist(Data, create_using=Graphtype)


HF = hv.Graph.from_networkx(G, nx.layout.circular_layout).opts(tools=['hover'])
HF
"""