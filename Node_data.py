# Asaf 6/5/19
import bokeh # 1.1.0
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import holoviews as hv
from holoviews import opts
hv.extension('bokeh','matplotlib')
from pylab import *
# hv.extension('bokeh')


# TO DO: output location


# read file

df = pd.read_csv('Given CSVs/GephiMatrix_co-authorship.csv', delimiter=';')
# sample node size 
# len(df.columns) to get all
N = 50

# the nodes, with deleted ';' in head of file
all_nodes = df.columns.tolist()

# sample size edges + weights
def make_edges(dframe, sample_size, weight_threshold):
    edges = []
    weights = []
    nodes = dframe.columns.tolist()
    for row in range (0, sample_size):
        for col in range (0, sample_size):
            if dframe.iat[row,col] > weight_threshold:
                edges.append([nodes[row],nodes[col],dframe.iat[row,col]])
                weights.append(dframe.iat[row,col])
    return edges, weights


sample_nodes = all_nodes[:N-1]
# row, column, weight
sample_edges, sample_weights = make_edges(df, N-1, 0)

# create graph
def make_network(nodes, edges):
    graph=nx.DiGraph()
    graph.add_nodes_from(nodes)
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=float(edge[2]*5))
    return graph

# everything works until here

G = make_network(sample_nodes, sample_edges)
# TO DO : make the following into a test
# print('edges ', G.edges(data=True))

# TO DO : write about these plots in report :
# plt.figure(1,figsize=(12,12))
# nx.draw(G,with_labels=False,font_size=15,node_size=100, k=1, iterations=20)
# plt.show()
#print('edges ', G.edges(data=True))


circular_layout = hv.Graph.from_networkx(G, nx.layout.circular_layout).relabel('Circular Layout').options(width=650, height=650).opts(xaxis=None, yaxis=None, padding=0.1)
plt.show(circular_layout)
# TO DO : Add node and edge sizes

# TO DO : create option to select nodes OR edges
# TO DO : fix export name (output location)
# def export_graph(obj):
#     # Using matplotlib (check bokeh documentation instead)
#     hv.save(obj, 'plot.svg', backend='matplotlib')

