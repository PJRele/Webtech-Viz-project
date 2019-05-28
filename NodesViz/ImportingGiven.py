# Asaf 26/5/19
import math
import bokeh  # 1.1.0
import pandas as pd  # 0.24.2
import matplotlib.pyplot as plt  # 3.0.3
import networkx as nx  # 2.2
import holoviews as hv  # 1.12.1
# import hvplot.networkx as hvnx
from holoviews import opts
from holoviews import dim
# from holoviews.operation.datashader import datashade, bundle_graph, shade, dynspread, rasterize
from holoviews.operation import decimate

hv.extension('bokeh')

""" Read File """
df = pd.read_csv(
    'C:/Users/Asaf/Documents/TU Software/Y3/Q4/DBL HTI Webtevh/Github/Webtech-Viz-project/Given CSVs/GephiMatrix_co-citation.csv',
    delimiter=';')

""" PARAMETERS """
# sample node size, len(df.columns) to get all
N = len(df.columns)
# number of max points on screen, excludes edgeless nodes
# decimate.max_samples = 1000
# fractional spread of adjacent nodes
# dynspread.max_px = 20
# dynspread.threshold = 0.5
# # bundled_boolean
# options: 'spring' 'circle'
figtype = 'spring'
BB = True  # bundle boolean
BS = False  # datashade boolean
B_edge_select = True

""" Renderer """
# renderer = hv.renderer('bokeh')


""" Edges """


# sample size edges + weights
def make_edges(dframe, sample_size, weight_threshold, B_weight):
    edges = []
    weights = []
    nodes = dframe.columns.tolist()
    # TO DO1 : instead of counting like this, put the name and its 'index'
    for row in range(0, sample_size):
        for col in range(0, sample_size):
            if B_weight & dframe.iat[row, col] > weight_threshold:
                edges.append([nodes[row], nodes[col], dframe.iat[row, col]])
                weights.append(math.sqrt(dframe.iat[row, col]) * 0.3)
            else:
                edges.append([nodes[row], nodes[col]])
    if B_weight:
        return edges, weights
    else:
        return edges


# row, column, weight
sample_edges, sample_weights = make_edges(df, N - 1, 0, True)

""" Nodes """
# the nodes, with deleted ';' in head of file
all_nodes = df.columns.tolist()
sample_nodes = all_nodes[:N - 1]

# dictionary where key is node name, value is count of edges
node_dict = {sample_nodes[0]: 0}
for node in sample_nodes:
    if node not in node_dict.keys():
        node_dict[node] = 0

# make node size based on edge count
for edge in sample_edges:
    if edge[0] in node_dict.keys():
        node_dict[edge[0]] = node_dict[edge[0]] + 1

node_sizes = []
for key in node_dict.keys():
    # +1 to show all nodes, *50 to make it larger
    node_sizes.append((node_dict[key] * 10) + 1)

weight_dimensions = [hv.Dimension(('node_sizes', 'Node Size'))]
